/**
 * Vocab App — Firebase Client SDK Initializer
 * Initializes Firebase App, Auth, and Cloud Firestore with offline IndexedDB persistence.
 * Supports both online live Firebase and automatic local fallback mode.
 */

import { firebaseConfig, isFirebaseConfigured } from './firebase-config.js';
import { eventBus } from './event-bus.js';

const FIREBASE_VERSION = '10.14.0';
const CDN_BASE = `https://www.gstatic.com/firebasejs/${FIREBASE_VERSION}`;

let app = null;
let auth = null;
let db = null;
let isLive = false;
let isInitialized = false;

// Dynamic import helpers to support offline / fallback gracefully
let firebaseModules = {
  app: null,
  auth: null,
  firestore: null
};

export async function initFirebase() {
  if (isInitialized) {
    return { app, auth, db, isLive };
  }

  const configured = isFirebaseConfigured();

  if (configured) {
    try {
      console.log('🔥 Initializing Google Firebase...');
      const [appMod, authMod, firestoreMod] = await Promise.all([
        import(`${CDN_BASE}/firebase-app.js`),
        import(`${CDN_BASE}/firebase-auth.js`),
        import(`${CDN_BASE}/firebase-firestore.js`)
      ]);

      firebaseModules.app = appMod;
      firebaseModules.auth = authMod;
      firebaseModules.firestore = firestoreMod;

      app = appMod.initializeApp(firebaseConfig);
      auth = authMod.getAuth(app);

      // Initialize Cloud Firestore with offline persistence
      try {
        db = firestoreMod.initializeFirestore(app, {
          localCache: firestoreMod.persistentLocalCache({
            tabManager: firestoreMod.persistentMultipleTabManager()
          })
        });
      } catch (cacheErr) {
        console.warn('Firestore multi-tab cache notice, using standard getFirestore:', cacheErr);
        db = firestoreMod.getFirestore(app);
      }

      isLive = true;
      console.log('✅ Google Firebase live connection established!');
      eventBus.emit('firebase:ready', { isLive: true });
    } catch (err) {
      console.warn('⚠️ Could not connect to live Firebase (network or configuration). Using offline local simulation:', err.message);
      isLive = false;
      eventBus.emit('firebase:ready', { isLive: false, error: err.message });
    }
  } else {
    console.info('ℹ️ Firebase credentials not configured yet. Running in offline/mock mode.');
    isLive = false;
    eventBus.emit('firebase:ready', { isLive: false, unconfigured: true });
  }

  isInitialized = true;
  return { app, auth, db, isLive, modules: firebaseModules };
}

export function getFirebaseInstance() {
  return { app, auth, db, isLive, modules: firebaseModules };
}

export function getFirebaseModules() {
  return firebaseModules;
}
