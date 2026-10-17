# 🔌 How to Add Any Future Feature with Immediate Firebase Backend

The **Vocab App** architecture is engineered with an **Extensible Feature Registry Pattern**. You can build any new feature (e.g., Quizzes, Spaced Repetition SRS, Audio Recordings, Social Leaderboards, Custom Word Decks) in minutes and have it **immediately backed by Google Firebase with zero backend boilerplate**.

---

## ⚡ The 3-Step Recipe

### Step 1: Create your feature service file (e.g. `src/services/quiz-service.js`)

Extend `BaseFeature` from `../core/feature-registry.js`:

```javascript
import { BaseFeature, featureRegistry } from '../core/feature-registry.js';

export class QuizService extends BaseFeature {
  constructor() {
    // 1. Give your feature a unique collection name under users/{uid}/
    super('quizzes', { isSubcollection: true });
  }

  // 2. Lifecycle hook: Automatically called when user logs in or switches accounts
  async onUserLoggedIn(user) {
    console.log(`Loading quiz history for ${user.nickname}...`);
    const history = await this.getDoc('summary');
    console.log('Quiz stats:', history);
  }

  // 3. Save feature data directly to Cloud Firestore with 1 call:
  async recordQuizScore(quizId, score, totalQuestions) {
    return await this.saveDoc(quizId, {
      quizId,
      score,
      totalQuestions,
      percentage: Math.round((score / totalQuestions) * 100),
      completedAt: new Date().toISOString()
    });
  }

  // 4. Retrieve data from Firestore (with automatic offline cache fallback):
  async getQuizScore(quizId) {
    return await this.getDoc(quizId);
  }

  // 5. Real-time multi-device subscription (optional):
  onQuizUpdated(quizId, callback) {
    return this.subscribeDoc(quizId, callback);
  }
}

// Export singleton instance and register into the Extensibility Engine:
export const quizService = new QuizService();
featureRegistry.register(quizService);
```

### Step 2: Use your feature in any UI component

```javascript
import { quizService } from './services/quiz-service.js';

// When the user finishes a quiz:
await quizService.recordQuizScore('greek_unit_1', 9, 10);
// That's it! It is saved to Firestore under users/{uid}/quizzes/greek_unit_1
// with automatic offline IndexedDB caching and event broadcasting.
```

### Step 3: Listen to reactive events anywhere (optional)

```javascript
import { eventBus } from './core/event-bus.js';

eventBus.on('feature:quizzes:updated', ({ docId, data }) => {
  console.log(`Quiz ${docId} updated! Score:`, data.score);
});
```

---

## 🛡️ Built-in Capabilities Inherited by Every Feature

When you extend `BaseFeature`, your feature automatically inherits:
1. **0ms UI Latency**: Local in-memory and `localStorage` cache update immediately, so your UI feels instantaneous (60fps).
2. **Cloud Firestore Sync**: Changes are written over secure TLS to your Firebase project.
3. **Offline-First Resilience**: If the user is on an airplane, in a subway, or offline, data is cached locally in IndexedDB and automatically pushes to the cloud once reconnected.
4. **Tenant Security**: Protected by `firestore.rules`—users can strictly only access their own documents (`users/{userId}/{featureName}/*`).
5. **Multi-Tab Sync**: Changes made in one browser tab automatically sync to other open tabs in real-time via `onSnapshot`.
