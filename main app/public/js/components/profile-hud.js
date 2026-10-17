/**
 * Vocab App — Profile HUD & Account Management Component
 * 
 * Displays:
 * - Large animated SVG Avatar with glowing aura
 * - Unique Nickname & Scholar Archetype badge
 * - Account Provider Badge (Google, Facebook, Email, Guest)
 * - Live Vocabulary Mastery Stats (Learned, Studying, Unread)
 * - Daily Streak Counter & Fire Telemetry
 * - Account Actions (Sign In / Register / Sign Out)
 */

import { authService } from '../services/auth-service.js';
import { avatarService } from '../services/avatar-service.js';
import { trackingService } from '../services/tracking-service.js';
import { authModal } from './auth-modal.js';
import { eventBus } from '../core/event-bus.js';

export class ProfileHUD {
  constructor(containerId = 'profile-hud-container') {
    this.containerId = containerId;
    this.container = null;

    eventBus.on('auth:state-change', () => this.render());
    eventBus.on('tracking:status-changed', () => this.updateStats());
    eventBus.on('tracking:synced', () => this.updateStats());
    eventBus.on('sync:state', (s) => this.updateSyncState(s));
  }

  mount(containerEl) {
    this.container = containerEl || document.getElementById(this.containerId);
    this.render();
  }

  render() {
    if (!this.container) {
      this.container = document.getElementById(this.containerId);
      if (!this.container) return;
    }

    const user = authService.getCurrentUser() || {
      nickname: 'Scholar',
      email: null,
      isAnonymous: true,
      providerId: 'anonymous'
    };

    const counts = trackingService.getCounts();
    const streaks = trackingService.getStreakStats();
    const meta = avatarService.getAvatarMeta(user.nickname);

    let providerBadge = '<span class="provider-pill guest">👤 Guest</span>';
    if (user.providerId === 'google.com') {
      providerBadge = '<span class="provider-pill google">🔵 Google</span>';
    } else if (user.providerId === 'facebook.com') {
      providerBadge = '<span class="provider-pill facebook">🔷 Facebook</span>';
    } else if (user.providerId === 'github.com') {
      providerBadge = '<span class="provider-pill github">🖤 GitHub</span>';
    } else if (!user.isAnonymous) {
      providerBadge = '<span class="provider-pill email">✉️ Verified Email</span>';
    }

    this.container.innerHTML = `
      <div class="profile-card-modern">
        <!-- Top Banner / Stage -->
        <div class="profile-header-banner">
          <div class="profile-avatar-wrapper" id="profile-avatar-holder">
            ${avatarService.generateAvatarSvg(user.nickname, { size: 104, animated: true })}
          </div>
          <div class="profile-user-info">
            <div class="profile-nickname-row">
              <h2 class="profile-nickname">${user.nickname}</h2>
              ${providerBadge}
            </div>
            <div class="profile-archetype-label">${meta.archetype}</div>
            <div class="profile-email-label">${user.email || 'Offline Guest Account'}</div>
          </div>
        </div>

        <!-- Telemetry & Streak HUD -->
        <div class="profile-stats-grid">
          <div class="stat-pill-box">
            <span class="stat-icon">🔥</span>
            <div class="stat-num" id="stat-current-streak">${streaks.currentStreak || 0}</div>
            <div class="stat-label">Day Streak</div>
          </div>
          <div class="stat-pill-box">
            <span class="stat-icon">🟢</span>
            <div class="stat-num" id="stat-learned-count">${counts.learned || 0}</div>
            <div class="stat-label">Learned</div>
          </div>
          <div class="stat-pill-box">
            <span class="stat-icon">🟡</span>
            <div class="stat-num" id="stat-studying-count">${counts.learning || 0}</div>
            <div class="stat-label">Studying</div>
          </div>
          <div class="stat-pill-box">
            <span class="stat-icon">🏆</span>
            <div class="stat-num" id="stat-longest-streak">${streaks.longestStreak || 0}</div>
            <div class="stat-label">Best Streak</div>
          </div>
        </div>

        <!-- Account Controls -->
        <div class="profile-actions-row">
          ${user.isAnonymous ? `
            <button class="profile-btn primary" id="btn-profile-join">
              <span>🚀 Link Account &amp; Save Progress</span>
            </button>
          ` : `
            <button class="profile-btn secondary" id="btn-profile-switch">
              <span>🔄 Switch Account</span>
            </button>
            <button class="profile-btn danger" id="btn-profile-signout">
              <span>🚪 Sign Out</span>
            </button>
          `}
        </div>

        <!-- Cloud Sync HUD -->
        <div class="profile-sync-footer">
          <div class="sync-indicator-group">
            <span class="sync-dot live" id="profile-sync-dot"></span>
            <span class="sync-text" id="profile-sync-text">Cloud Storage: Connected to Firebase</span>
          </div>
        </div>

      </div>
    `;

    this._bindEvents();
  }

  updateStats() {
    if (!this.container) return;
    const counts = trackingService.getCounts();
    const streaks = trackingService.getStreakStats();

    const elLearned = this.container.querySelector('#stat-learned-count');
    const elStudying = this.container.querySelector('#stat-studying-count');
    const elStreak = this.container.querySelector('#stat-current-streak');
    const elBest = this.container.querySelector('#stat-longest-streak');

    if (elLearned) elLearned.textContent = counts.learned;
    if (elStudying) elStudying.textContent = counts.learning;
    if (elStreak) elStreak.textContent = streaks.currentStreak;
    if (elBest) elBest.textContent = streaks.longestStreak;
  }

  updateSyncState({ state }) {
    if (!this.container) return;
    const dot = this.container.querySelector('#profile-sync-dot');
    const text = this.container.querySelector('#profile-sync-text');
    if (dot && text) {
      if (state === 'synced') {
        dot.className = 'sync-dot live';
        text.textContent = 'Cloud Storage: Synced with Firebase';
      } else if (state === 'syncing') {
        dot.className = 'sync-dot syncing';
        text.textContent = 'Cloud Storage: Syncing changes...';
      } else {
        dot.className = 'sync-dot offline';
        text.textContent = 'Cloud Storage: Offline / Local Mode';
      }
    }
  }

  _bindEvents() {
    const btnJoin = this.container.querySelector('#btn-profile-join');
    const btnSwitch = this.container.querySelector('#btn-profile-switch');
    const btnSignOut = this.container.querySelector('#btn-profile-signout');

    if (btnJoin) {
      btnJoin.addEventListener('click', () => authModal.show('signup'));
    }
    if (btnSwitch) {
      btnSwitch.addEventListener('click', () => authModal.show('login'));
    }
    if (btnSignOut) {
      btnSignOut.addEventListener('click', async () => {
        if (confirm('Are you sure you want to sign out?')) {
          await authService.signOut();
        }
      });
    }
  }
}

export const profileHUD = new ProfileHUD();
