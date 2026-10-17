// src/services/MobileUpdater.ts
import { initializeApp } from 'firebase/app';
import { getFirestore, doc, onSnapshot } from 'firebase/firestore';
import { Filesystem, Directory } from '@capacitor/filesystem';
import { FileOpener } from '@capacitor-community/file-opener';
import pkg from '../../package.json';

const firebaseConfig = {
  apiKey: import.meta.env.VITE_FIREBASE_API_KEY || "AIzaSyD4uOmCgfr98wAKhxNhc_D59bJf30pq5V0",
  authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN || "vocabapp-fdf4f.firebaseapp.com",
  projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID || "vocabapp-fdf4f",
  storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET || "vocabapp-fdf4f.firebasestorage.app",
  messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGING_SENDER_ID || "65485068665",
  appId: import.meta.env.VITE_FIREBASE_APP_ID || "1:65485068665:web:dc6211f1a877a71fc637a8",
};

const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);

export function listenForInstantMobileUpdates(
  onUpdateAvailable: (data: { version: string; downloadUrl: string; releaseNotes: string }) => void
) {
  const releaseRef = doc(db, 'app_meta', 'mobile_release');
  return onSnapshot(releaseRef, (snapshot) => {
    if (!snapshot.exists()) return;
    const data = snapshot.data();
    if (data.version && isNewerVersion(pkg.version, data.version)) {
      onUpdateAvailable({
        version: data.version,
        downloadUrl: data.downloadUrl,
        releaseNotes: data.releaseNotes || 'New update available'
      });
    }
  });
}

export async function downloadAndInstallApk(
  downloadUrl: string,
  onProgress: (percent: number) => void
) {
  const fileName = 'update-release.apk';

  const progressListener = await Filesystem.addListener('progress', (status: any) => {
    if (status.contentLength > 0) {
      onProgress(Math.round((status.bytes / status.contentLength) * 100));
    }
  });

  try {
    const result = await Filesystem.downloadFile({
      url: downloadUrl,
      path: fileName,
      directory: Directory.Cache,
      progress: true
    });

    if (!result.path) throw new Error('Download failed: no file path returned');

    // Immediately trigger the native Android APK package installer over the current app
    await FileOpener.open({
      filePath: result.path,
      contentType: 'application/vnd.android.package-archive',
      openWithDefault: true
    });
  } finally {
    progressListener.remove();
  }
}

function isNewerVersion(local: string, remote: string): boolean {
  const l = local.replace(/^v/, '').split('.').map(Number);
  const r = remote.replace(/^v/, '').split('.').map(Number);
  for (let i = 0; i < Math.max(l.length, r.length); i++) {
    if ((r[i] || 0) > (l[i] || 0)) return true;
    if ((r[i] || 0) < (l[i] || 0)) return false;
  }
  return false;
}
