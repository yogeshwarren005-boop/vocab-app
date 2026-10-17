/**
 * Vocab App — Extensibility Engine & Future Feature Registry
 * 
 * Allows ANY new feature added in the future to immediately connect to
 * the Firebase backend with zero boilerplate.
 * 
 * Example usage for a new future feature (e.g. Quizzes, Spaced Repetition SRS):
 * 
 * ```javascript
 * import { BaseFeature, featureRegistry } from './core/feature-registry.js';
 * 
 * class QuizFeature extends BaseFeature {
 *   constructor() {
 *     super('quizzes', { isSubcollection: true });
 *   }
 * 
 *   async saveQuizResult(quizId, score) {
 *     return this.saveDoc(quizId, { score, completedAt: new Date().toISOString() });
 *   }
 * }
 * 
 * // Register feature in 1 line:
 * featureRegistry.register(new QuizFeature());
 * ```
 */

import { eventBus } from './event-bus.js';
import { getFirebaseInstance } from './firebase.js';

export class BaseFeature {
  /**
   * @param {string} name - Unique identifier of the feature (e.g. 'quizzes', 'bookmarks', 'srs')
   * @param {Object} options
   * @param {boolean} options.isSubcollection - If true, data resides at users/{uid}/{name}
   */
  constructor(name, options = { isSubcollection: true }) {
    this.name = name;
    this.isSubcollection = options.isSubcollection !== false;
    this.currentUser = null;
    this.localState = new Map();
    this.unsubscribes = [];
  }

  /**
   * Internal hook called by FeatureRegistry on auth change
   */
  async _onAuthChange(user) {
    this.currentUser = user;
    this.cleanupListeners();
    if (user) {
      await this.onUserLoggedIn(user);
    } else {
      await this.onUserLoggedOut();
    }
  }

  cleanupListeners() {
    this.unsubscribes.forEach(unsub => {
      try { unsub(); } catch {}
    });
    this.unsubscribes = [];
  }

  // Lifecycle hooks for subclass override
  async onUserLoggedIn(user) {}
  async onUserLoggedOut() {
    this.localState.clear();
  }

  /**
   * Universal document saver: Automatically persists to Cloud Firestore
   * with offline fallback and event notification.
   */
  async saveDoc(docId, data, merge = true) {
    const timestamp = new Date().toISOString();
    const payload = { ...data, updatedAt: timestamp };

    // Update local in-memory cache immediately (0ms UI latency)
    this.localState.set(docId, payload);
    this._saveToLocalStorage(docId, payload);
    eventBus.emit(`feature:${this.name}:updated`, { docId, data: payload });

    const { db, isLive, modules } = getFirebaseInstance();
    if (isLive && db && this.currentUser && modules.firestore) {
      try {
        const { doc, setDoc } = modules.firestore;
        let docRef;
        if (this.isSubcollection) {
          docRef = doc(db, 'users', this.currentUser.uid, this.name, docId);
        } else {
          docRef = doc(db, this.name, docId);
        }
        await setDoc(docRef, payload, { merge });
        return { success: true, cloud: true, data: payload };
      } catch (err) {
        console.warn(`[${this.name}] Cloud write queued locally:`, err.message);
        return { success: true, cloud: false, queued: true, data: payload };
      }
    }

    return { success: true, cloud: false, localOnly: true, data: payload };
  }

  /**
   * Universal document fetcher: Reads from Firestore or local cache
   */
  async getDoc(docId) {
    // Check local memory first
    if (this.localState.has(docId)) {
      return this.localState.get(docId);
    }

    // Check localStorage fallback
    const local = this._loadFromLocalStorage(docId);
    if (local) {
      this.localState.set(docId, local);
    }

    const { db, isLive, modules } = getFirebaseInstance();
    if (isLive && db && this.currentUser && modules.firestore) {
      try {
        const { doc, getDoc: fsGetDoc } = modules.firestore;
        let docRef;
        if (this.isSubcollection) {
          docRef = doc(db, 'users', this.currentUser.uid, this.name, docId);
        } else {
          docRef = doc(db, this.name, docId);
        }
        const snap = await fsGetDoc(docRef);
        if (snap.exists()) {
          const cloudData = snap.data();
          this.localState.set(docId, cloudData);
          this._saveToLocalStorage(docId, cloudData);
          return cloudData;
        }
      } catch (err) {
        console.warn(`[${this.name}] Could not fetch from cloud, returning local cache:`, err.message);
      }
    }

    return local || null;
  }

  /**
   * Real-time document subscription across all user devices
   */
  subscribeDoc(docId, callback) {
    const { db, isLive, modules } = getFirebaseInstance();
    if (isLive && db && this.currentUser && modules.firestore) {
      try {
        const { doc, onSnapshot } = modules.firestore;
        let docRef;
        if (this.isSubcollection) {
          docRef = doc(db, 'users', this.currentUser.uid, this.name, docId);
        } else {
          docRef = doc(db, this.name, docId);
        }
        const unsub = onSnapshot(docRef, (snap) => {
          if (snap.exists()) {
            const data = snap.data();
            this.localState.set(docId, data);
            this._saveToLocalStorage(docId, data);
            callback(data);
          }
        }, (err) => {
          console.warn(`[${this.name}] Snapshot listener warning:`, err.message);
        });
        this.unsubscribes.push(unsub);
        return unsub;
      } catch (err) {
        console.warn(`[${this.name}] Could not create cloud listener:`, err.message);
      }
    }

    // Local fallback listener
    return eventBus.on(`feature:${this.name}:updated`, (payload) => {
      if (payload.docId === docId) {
        callback(payload.data);
      }
    });
  }

  _getStorageKey(docId) {
    const uid = this.currentUser ? this.currentUser.uid : 'guest';
    return `vocab_feature_${this.name}_${uid}_${docId}`;
  }

  _saveToLocalStorage(docId, data) {
    try {
      localStorage.setItem(this._getStorageKey(docId), JSON.stringify(data));
    } catch {}
  }

  _loadFromLocalStorage(docId) {
    try {
      const item = localStorage.getItem(this._getStorageKey(docId));
      return item ? JSON.parse(item) : null;
    } catch {
      return null;
    }
  }
}

class FeatureRegistry {
  constructor() {
    this.features = new Map();
    this.currentUser = null;

    // Listen to global auth changes to hydrate/clean features
    eventBus.on('auth:state-change', (user) => {
      this.currentUser = user;
      for (const [name, feature] of this.features) {
        try {
          feature._onAuthChange(user);
        } catch (err) {
          console.error(`Error notifying feature [${name}] of auth change:`, err);
        }
      }
    });
  }

  register(featureInstance) {
    if (!(featureInstance instanceof BaseFeature)) {
      throw new Error('Registered feature must extend BaseFeature');
    }
    const name = featureInstance.name;
    this.features.set(name, featureInstance);
    console.log(`🔌 Feature registered: [${name}] with automatic Firebase backend integration.`);

    // If user is already authenticated, immediately initialize the feature
    if (this.currentUser) {
      featureInstance._onAuthChange(this.currentUser);
    }
    return featureInstance;
  }

  get(name) {
    return this.features.get(name);
  }

  getAll() {
    return Array.from(this.features.values());
  }
}

export const featureRegistry = new FeatureRegistry();
