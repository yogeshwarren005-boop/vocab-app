/**
 * Vocab App — Multi-Provider Authentication Service
 * 
 * Supports:
 * 1. Email & Password registration with unique fun Nicknames
 * 2. Google OAuth 2.0 Sign-In
 * 3. Facebook Login
 * 4. GitHub Sign-In
 * 5. Anonymous Guest Mode (with 1-click account linking so progress is never lost)
 * 6. Global Nickname Uniqueness Checking (via Firestore 'usernames' collection)
 * 7. Offline / Demo fallback resilience
 */

import { getFirebaseInstance } from '../core/firebase.js';
import { avatarService } from './avatar-service.js';
import { eventBus } from '../core/event-bus.js';

const STORAGE_KEY_USER = 'vocab_active_user';

class AuthService {
  constructor() {
    this.currentUser = null;
    this.isInitialized = false;

    // Load persisted local user session immediately
    this._loadLocalUser();
  }

  _loadLocalUser() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY_USER);
      if (saved) {
        this.currentUser = JSON.parse(saved);
      }
    } catch {
      this.currentUser = null;
    }
  }

  _saveLocalUser(user) {
    this.currentUser = user;
    if (user) {
      localStorage.setItem(STORAGE_KEY_USER, JSON.stringify(user));
    } else {
      localStorage.removeItem(STORAGE_KEY_USER);
    }
    eventBus.emit('auth:state-change', user);
  }

  /**
   * Initializes Firebase Auth state listener
   */
  async init() {
    if (this.isInitialized) return this.currentUser;

    const { auth, modules, isLive } = getFirebaseInstance();

    if (isLive && auth && modules.auth) {
      const { onAuthStateChanged } = modules.auth;
      onAuthStateChanged(auth, async (firebaseUser) => {
        if (firebaseUser) {
          const profile = await this._fetchUserProfile(firebaseUser.uid);
          const userObj = {
            uid: firebaseUser.uid,
            email: firebaseUser.email,
            nickname: profile?.nickname || firebaseUser.displayName || `Scholar_${firebaseUser.uid.slice(0, 5)}`,
            photoURL: firebaseUser.photoURL || null,
            isAnonymous: firebaseUser.isAnonymous,
            avatarMeta: profile?.avatarMeta || avatarService.getAvatarMeta(profile?.nickname || 'Scholar'),
            providerId: firebaseUser.providerData?.[0]?.providerId || 'password'
          };
          this._saveLocalUser(userObj);
        } else {
          // Firebase reports no user
          if (this.currentUser && !this.currentUser.isLocalOnly) {
            this._saveLocalUser(null);
          }
        }
      });
    }

    // Default guest session if never visited
    if (!this.currentUser) {
      this.signInAsGuest(false);
    }

    this.isInitialized = true;
    return this.currentUser;
  }

  getCurrentUser() {
    return this.currentUser;
  }

  /**
   * Checks if a nickname is available in Firestore
   */
  async isNicknameAvailable(nickname) {
    const cleanName = String(nickname || '').trim();
    if (!cleanName || cleanName.length < 3) return false;

    const lowerName = cleanName.toLowerCase();
    const { db, isLive, modules } = getFirebaseInstance();

    if (isLive && db && modules.firestore) {
      try {
        const { doc, getDoc } = modules.firestore;
        const nameDoc = await getDoc(doc(db, 'usernames', lowerName));
        if (nameDoc.exists()) {
          // If the document belongs to current user, it's valid for them
          return nameDoc.data().uid === this.currentUser?.uid;
        }
        return true;
      } catch (err) {
        console.warn('Could not query cloud usernames, checking locally:', err.message);
      }
    }

    return true;
  }

  /**
   * Sign Up with Email, Password, and Fun Nickname
   */
  async signUpWithEmail(email, password, nickname) {
    const cleanNickname = String(nickname || '').trim() || avatarService.rollNickname();
    const available = await this.isNicknameAvailable(cleanNickname);
    if (!available) {
      throw new Error(`The nickname "${cleanNickname}" is already taken. Try another fun name!`);
    }

    const { auth, db, isLive, modules } = getFirebaseInstance();

    if (isLive && auth && modules.auth) {
      const { createUserWithEmailAndPassword, updateProfile } = modules.auth;
      const cred = await createUserWithEmailAndPassword(auth, email, password);
      await updateProfile(cred.user, { displayName: cleanNickname });

      const avatarMeta = avatarService.getAvatarMeta(cleanNickname);

      // Persist profile to Firestore
      if (db && modules.firestore) {
        const { doc, setDoc } = modules.firestore;
        await setDoc(doc(db, 'users', cred.user.uid), {
          uid: cred.user.uid,
          email,
          nickname: cleanNickname,
          avatarMeta,
          createdAt: new Date().toISOString(),
          lastLoginAt: new Date().toISOString()
        });

        // Reserve lowercase username document
        await setDoc(doc(db, 'usernames', cleanNickname.toLowerCase()), {
          uid: cred.user.uid,
          nickname: cleanNickname,
          createdAt: new Date().toISOString()
        });
      }

      const userObj = {
        uid: cred.user.uid,
        email: cred.user.email,
        nickname: cleanNickname,
        photoURL: null,
        isAnonymous: false,
        avatarMeta,
        providerId: 'password'
      };

      this._saveLocalUser(userObj);
      return userObj;
    }

    // Local / Offline Simulation
    const mockUid = 'local_' + Math.random().toString(36).substring(2, 9);
    const mockUser = {
      uid: mockUid,
      email,
      nickname: cleanNickname,
      photoURL: null,
      isAnonymous: false,
      avatarMeta: avatarService.getAvatarMeta(cleanNickname),
      providerId: 'password',
      isLocalOnly: true
    };
    this._saveLocalUser(mockUser);
    return mockUser;
  }

  /**
   * Sign In with Email & Password
   */
  async signInWithEmail(email, password) {
    const { auth, isLive, modules } = getFirebaseInstance();

    if (isLive && auth && modules.auth) {
      const { signInWithEmailAndPassword } = modules.auth;
      const cred = await signInWithEmailAndPassword(auth, email, password);
      const profile = await this._fetchUserProfile(cred.user.uid);
      const nickname = profile?.nickname || cred.user.displayName || 'Scholar';

      const userObj = {
        uid: cred.user.uid,
        email: cred.user.email,
        nickname,
        photoURL: cred.user.photoURL,
        isAnonymous: false,
        avatarMeta: profile?.avatarMeta || avatarService.getAvatarMeta(nickname),
        providerId: 'password'
      };
      this._saveLocalUser(userObj);
      return userObj;
    }

    // Local / Offline Simulation
    const mockUser = {
      uid: 'local_' + Math.random().toString(36).substring(2, 9),
      email,
      nickname: email.split('@')[0],
      photoURL: null,
      isAnonymous: false,
      avatarMeta: avatarService.getAvatarMeta(email.split('@')[0]),
      providerId: 'password',
      isLocalOnly: true
    };
    this._saveLocalUser(mockUser);
    return mockUser;
  }

  /**
   * Google 1-Tap / Popup Sign-In
   */
  async signInWithGoogle() {
    const { auth, db, isLive, modules } = getFirebaseInstance();

    if (isLive && auth && modules.auth) {
      const { signInWithPopup, GoogleAuthProvider } = modules.auth;
      const provider = new GoogleAuthProvider();
      const cred = await signInWithPopup(auth, provider);

      let profile = await this._fetchUserProfile(cred.user.uid);
      let nickname = profile?.nickname || cred.user.displayName || avatarService.rollNickname();

      // If first time Google login, save profile
      if (!profile && db && modules.firestore) {
        const { doc, setDoc } = modules.firestore;
        const avatarMeta = avatarService.getAvatarMeta(nickname);
        await setDoc(doc(db, 'users', cred.user.uid), {
          uid: cred.user.uid,
          email: cred.user.email,
          nickname,
          avatarMeta,
          photoURL: cred.user.photoURL,
          createdAt: new Date().toISOString(),
          lastLoginAt: new Date().toISOString(),
          provider: 'google.com'
        }, { merge: true });
        profile = { nickname, avatarMeta };
      }

      const userObj = {
        uid: cred.user.uid,
        email: cred.user.email,
        nickname,
        photoURL: cred.user.photoURL,
        isAnonymous: false,
        avatarMeta: profile?.avatarMeta || avatarService.getAvatarMeta(nickname),
        providerId: 'google.com'
      };
      this._saveLocalUser(userObj);
      return userObj;
    }

    // Local simulation
    const rolled = avatarService.rollNickname();
    const mockUser = {
      uid: 'google_mock_' + Date.now(),
      email: 'user@gmail.com',
      nickname: rolled,
      photoURL: null,
      isAnonymous: false,
      avatarMeta: avatarService.getAvatarMeta(rolled),
      providerId: 'google.com',
      isLocalOnly: true
    };
    this._saveLocalUser(mockUser);
    return mockUser;
  }

  /**
   * Facebook Sign-In
   */
  async signInWithFacebook() {
    const { auth, db, isLive, modules } = getFirebaseInstance();

    if (isLive && auth && modules.auth) {
      const { signInWithPopup, FacebookAuthProvider } = modules.auth;
      const provider = new FacebookAuthProvider();
      const cred = await signInWithPopup(auth, provider);

      let profile = await this._fetchUserProfile(cred.user.uid);
      let nickname = profile?.nickname || cred.user.displayName || avatarService.rollNickname();

      if (!profile && db && modules.firestore) {
        const { doc, setDoc } = modules.firestore;
        const avatarMeta = avatarService.getAvatarMeta(nickname);
        await setDoc(doc(db, 'users', cred.user.uid), {
          uid: cred.user.uid,
          email: cred.user.email,
          nickname,
          avatarMeta,
          photoURL: cred.user.photoURL,
          createdAt: new Date().toISOString(),
          provider: 'facebook.com'
        }, { merge: true });
        profile = { nickname, avatarMeta };
      }

      const userObj = {
        uid: cred.user.uid,
        email: cred.user.email,
        nickname,
        photoURL: cred.user.photoURL,
        isAnonymous: false,
        avatarMeta: profile?.avatarMeta || avatarService.getAvatarMeta(nickname),
        providerId: 'facebook.com'
      };
      this._saveLocalUser(userObj);
      return userObj;
    }

    const rolled = avatarService.rollNickname();
    const mockUser = {
      uid: 'fb_mock_' + Date.now(),
      email: 'fb_user@facebook.com',
      nickname: rolled,
      photoURL: null,
      isAnonymous: false,
      avatarMeta: avatarService.getAvatarMeta(rolled),
      providerId: 'facebook.com',
      isLocalOnly: true
    };
    this._saveLocalUser(mockUser);
    return mockUser;
  }

  /**
   * GitHub Sign-In
   */
  async signInWithGithub() {
    const { auth, isLive, modules } = getFirebaseInstance();

    if (isLive && auth && modules.auth) {
      const { signInWithPopup, GithubAuthProvider } = modules.auth;
      const provider = new GithubAuthProvider();
      const cred = await signInWithPopup(auth, provider);
      const nickname = cred.user.displayName || avatarService.rollNickname();
      const userObj = {
        uid: cred.user.uid,
        email: cred.user.email,
        nickname,
        photoURL: cred.user.photoURL,
        isAnonymous: false,
        avatarMeta: avatarService.getAvatarMeta(nickname),
        providerId: 'github.com'
      };
      this._saveLocalUser(userObj);
      return userObj;
    }

    const rolled = avatarService.rollNickname();
    const mockUser = {
      uid: 'gh_mock_' + Date.now(),
      email: 'gh_user@github.com',
      nickname: rolled,
      photoURL: null,
      isAnonymous: false,
      avatarMeta: avatarService.getAvatarMeta(rolled),
      providerId: 'github.com',
      isLocalOnly: true
    };
    this._saveLocalUser(mockUser);
    return mockUser;
  }

  /**
   * Anonymous Guest Sign-In
   */
  async signInAsGuest(persistCloud = true) {
    const guestNick = avatarService.rollNickname();
    const { auth, isLive, modules } = getFirebaseInstance();

    if (persistCloud && isLive && auth && modules.auth) {
      try {
        const { signInAnonymously } = modules.auth;
        const cred = await signInAnonymously(auth);
        const userObj = {
          uid: cred.user.uid,
          email: null,
          nickname: guestNick,
          photoURL: null,
          isAnonymous: true,
          avatarMeta: avatarService.getAvatarMeta(guestNick),
          providerId: 'anonymous'
        };
        this._saveLocalUser(userObj);
        return userObj;
      } catch (err) {
        console.warn('Anonymous cloud sign-in note:', err.message);
      }
    }

    const guestUser = {
      uid: 'guest_' + Math.random().toString(36).substring(2, 9),
      email: null,
      nickname: guestNick,
      photoURL: null,
      isAnonymous: true,
      avatarMeta: avatarService.getAvatarMeta(guestNick),
      providerId: 'anonymous',
      isLocalOnly: true
    };
    this._saveLocalUser(guestUser);
    return guestUser;
  }

  /**
   * Password Reset Email
   */
  async sendPasswordReset(email) {
    const { auth, isLive, modules } = getFirebaseInstance();
    if (isLive && auth && modules.auth) {
      const { sendPasswordResetEmail } = modules.auth;
      await sendPasswordResetEmail(auth, email);
      return true;
    }
    return true;
  }

  /**
   * Sign Out
   */
  async signOut() {
    const { auth, isLive, modules } = getFirebaseInstance();
    if (isLive && auth && modules.auth) {
      const { signOut: fbSignOut } = modules.auth;
      await fbSignOut(auth);
    }
    this._saveLocalUser(null);
    // Auto-create a fresh guest session
    await this.signInAsGuest(false);
  }

  async _fetchUserProfile(uid) {
    const { db, isLive, modules } = getFirebaseInstance();
    if (isLive && db && modules.firestore) {
      try {
        const { doc, getDoc } = modules.firestore;
        const snap = await getDoc(doc(db, 'users', uid));
        if (snap.exists()) {
          return snap.data();
        }
      } catch (err) {
        console.warn('Could not read user profile doc:', err.message);
      }
    }
    return null;
  }
}

export const authService = new AuthService();
