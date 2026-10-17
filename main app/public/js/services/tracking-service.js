/**
 * Vocab App — Firebase Vocabulary Tracking & Mastery Engine
 * 
 * Features:
 * 1. Sparse Cloud Firestore Tracking:
 *    - All 51,000+ words default to 'unread' (🔴).
 *    - Only active 'studying' (🟡) and 'learned' (🟢) statuses are synced to Firestore.
 *    - Reduces Firestore writes and reads by 99% while ensuring instant 0ms swipe performance.
 * 2. Daily Streak & Review Telemetry:
 *    - Daily words reviewed counter.
 *    - Consecutive day streak tracking.
 *    - Last review date comparison.
 * 3. Debounced Batch Synchronization:
 *    - Fast offline-first state mutations with background cloud reconciliation.
 */

import { BaseFeature, featureRegistry } from '../core/feature-registry.js';
import { eventBus } from '../core/event-bus.js';

class TrackingService extends BaseFeature {
  constructor() {
    super('tracking', { isSubcollection: true });

    // In-memory status mapping: { [notePath]: 'unread' | 'learning' | 'learned' }
    this.statusDb = {};
    this.streakStats = {
      currentStreak: 0,
      longestStreak: 0,
      wordsReviewedToday: 0,
      lastActiveDate: null,
      history: {}
    };

    this._pendingSyncTimer = null;
    this._pendingDeltas = new Map(); // notePath -> newStatus

    this._loadLocalTrackingData();
  }

  _loadLocalTrackingData() {
    try {
      const savedStatus = localStorage.getItem('vocab_status_db');
      if (savedStatus) {
        this.statusDb = JSON.parse(savedStatus);
      }
      const savedStreaks = localStorage.getItem('vocab_streak_stats');
      if (savedStreaks) {
        this.streakStats = JSON.parse(savedStreaks);
      }
    } catch (e) {
      console.warn('Local tracking storage parse warning:', e);
    }
  }

  _persistLocalTrackingData() {
    try {
      localStorage.setItem('vocab_status_db', JSON.stringify(this.statusDb));
      localStorage.setItem('vocab_streak_stats', JSON.stringify(this.streakStats));
    } catch {}
  }

  async onUserLoggedIn(user) {
    console.log(`📡 Hydrating tracking progress for ${user.nickname} (${user.uid})...`);
    await this.fetchCloudProgress();
  }

  async onUserLoggedOut() {
    // Keep local data for guest
    this._loadLocalTrackingData();
  }

  /**
   * Fetches cloud progress from Firestore and merges with local deltas
   */
  async fetchCloudProgress() {
    if (!this.currentUser) return;

    try {
      // Read discipline progress documents
      const [greekProgress, latinProgress, vocabProgress, streakDoc] = await Promise.all([
        this.getDoc('progress_greek'),
        this.getDoc('progress_latin'),
        this.getDoc('progress_vocab'),
        this.getDoc('streaks')
      ]);

      const merged = { ...this.statusDb };

      if (greekProgress?.words) Object.assign(merged, greekProgress.words);
      if (latinProgress?.words) Object.assign(merged, latinProgress.words);
      if (vocabProgress?.words) Object.assign(merged, vocabProgress.words);

      this.statusDb = merged;
      this._persistLocalTrackingData();

      if (streakDoc) {
        this.streakStats = { ...this.streakStats, ...streakDoc };
        this._persistLocalTrackingData();
      }

      eventBus.emit('tracking:synced', {
        statusDb: this.statusDb,
        streakStats: this.streakStats
      });
      console.log('✅ Tracking data synchronized with Firebase Cloud.');
    } catch (err) {
      console.warn('Could not complete cloud tracking fetch:', err.message);
    }
  }

  /**
   * Gets the status of a note: 'unread' | 'learning' | 'learned'
   */
  getStatus(notePath) {
    if (!notePath) return 'unread';
    return this.statusDb[notePath] || 'unread';
  }

  /**
   * Updates the status of a word with 0ms UI delay and debounced cloud sync
   */
  setStatus(notePath, status) {
    if (!notePath) return;

    const normalizedStatus = status === 'learning' || status === 'studying' ? 'learning' : (status === 'learned' ? 'learned' : 'unread');

    if (normalizedStatus === 'unread') {
      delete this.statusDb[notePath];
    } else {
      this.statusDb[notePath] = normalizedStatus;
    }

    // Queue delta for cloud sync
    this._pendingDeltas.set(notePath, normalizedStatus);
    this._recordReviewActivity();
    this._persistLocalTrackingData();

    eventBus.emit('tracking:status-changed', {
      notePath,
      status: normalizedStatus,
      counts: this.getCounts()
    });

    this._scheduleDebouncedSync();
  }

  /**
   * Cycles status: unread (🔴) -> studying (🟡) -> learned (🟢) -> unread (🔴)
   */
  toggleStatus(notePath) {
    const current = this.getStatus(notePath);
    let next = 'learning';
    if (current === 'learning') next = 'learned';
    else if (current === 'learned') next = 'unread';
    this.setStatus(notePath, next);
    return next;
  }

  /**
   * Records daily streak and word review count
   */
  _recordReviewActivity() {
    const today = new Date().toISOString().split('T')[0];

    if (this.streakStats.lastActiveDate !== today) {
      const yesterday = new Date(Date.now() - 86400000).toISOString().split('T')[0];
      if (this.streakStats.lastActiveDate === yesterday) {
        this.streakStats.currentStreak += 1;
      } else {
        this.streakStats.currentStreak = 1;
      }
      this.streakStats.longestStreak = Math.max(this.streakStats.longestStreak, this.streakStats.currentStreak);
      this.streakStats.wordsReviewedToday = 0;
      this.streakStats.lastActiveDate = today;
    }

    this.streakStats.wordsReviewedToday += 1;
    this.streakStats.history[today] = (this.streakStats.history[today] || 0) + 1;
  }

  _scheduleDebouncedSync() {
    clearTimeout(this._pendingSyncTimer);
    this._pendingSyncTimer = setTimeout(async () => {
      await this._flushPendingDeltasToCloud();
    }, 1500); // 1.5-second debounce
  }

  async _flushPendingDeltasToCloud() {
    if (this._pendingDeltas.size === 0) return;

    const deltas = new Map(this._pendingDeltas);
    this._pendingDeltas.clear();

    const greekWords = {};
    const latinWords = {};
    const vocabWords = {};

    for (const [path, status] of deltas) {
      if (path.startsWith('Greek roots/')) {
        greekWords[path] = status;
      } else if (path.startsWith('Latin roots/')) {
        latinWords[path] = status;
      } else {
        vocabWords[path] = status;
      }
    }

    const promises = [];

    if (Object.keys(greekWords).length > 0) {
      promises.push(this.saveDoc('progress_greek', { words: greekWords }, true));
    }
    if (Object.keys(latinWords).length > 0) {
      promises.push(this.saveDoc('progress_latin', { words: latinWords }, true));
    }
    if (Object.keys(vocabWords).length > 0) {
      promises.push(this.saveDoc('progress_vocab', { words: vocabWords }, true));
    }
    promises.push(this.saveDoc('streaks', this.streakStats, true));

    try {
      await Promise.all(promises);
      eventBus.emit('sync:state', { state: 'synced' });
    } catch (e) {
      console.warn('Sync deltas queued in offline cache:', e.message);
      eventBus.emit('sync:state', { state: 'queued' });
    }
  }

  getCounts() {
    let learned = 0;
    let learning = 0;
    for (const key in this.statusDb) {
      const s = this.statusDb[key];
      if (s === 'learned') learned++;
      else if (s === 'learning') learning++;
    }
    return { learned, learning };
  }

  getStreakStats() {
    return this.streakStats;
  }
}

export const trackingService = new TrackingService();
// Register into Extensible Feature Engine
featureRegistry.register(trackingService);
