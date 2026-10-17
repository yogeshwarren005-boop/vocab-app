/**
 * Vocab App — Firebase Configuration
 * Live project credentials connected to: vocabapp-fdf4f
 */
export const firebaseConfig = {
  apiKey: "AIzaSyD4uOmCgfr98wAKhxNhc_D59bJf30pq5V0",
  authDomain: "vocabapp-fdf4f.firebaseapp.com",
  projectId: "vocabapp-fdf4f",
  storageBucket: "vocabapp-fdf4f.firebasestorage.app",
  messagingSenderId: "65485068665",
  appId: "1:65485068665:web:dc6211f1a877a71fc637a8",
  measurementId: "G-ENDQ9S3YN3"
};

/**
 * Checks if real Firebase credentials have been configured
 */
export function isFirebaseConfigured() {
  return (
    Boolean(firebaseConfig.apiKey) &&
    !firebaseConfig.apiKey.includes("DEMO-KEY") &&
    Boolean(firebaseConfig.projectId) &&
    !firebaseConfig.projectId.includes("vocab-app-project")
  );
}
