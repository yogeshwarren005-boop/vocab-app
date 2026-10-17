/**
 * Vocab App — Reactive Event Bus
 * Lightweight pub/sub emitter enabling loose coupling between
 * UI components, authentication, and Firebase storage services.
 */
class EventBus {
  constructor() {
    this.events = new Map();
  }

  on(event, callback) {
    if (!this.events.has(event)) {
      this.events.set(event, new Set());
    }
    this.events.get(event).add(callback);
    return () => this.off(event, callback);
  }

  off(event, callback) {
    const listeners = this.events.get(event);
    if (listeners) {
      listeners.delete(callback);
      if (listeners.size === 0) {
        this.events.delete(event);
      }
    }
  }

  emit(event, payload) {
    const listeners = this.events.get(event);
    if (listeners) {
      for (const callback of listeners) {
        try {
          callback(payload);
        } catch (err) {
          console.error(`Error in event listener for [${event}]:`, err);
        }
      }
    }
  }

  clear() {
    this.events.clear();
  }
}

export const eventBus = new EventBus();
