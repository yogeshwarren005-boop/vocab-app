/**
 * Vocab App — Top Navigation Bar Component
 * Displays:
 * - Back button (dynamic for subpage drill-down)
 * - Navigation breadcrumbs
 * - User Profile Pill with animated mini-avatar & live sync dot
 */

import { authService } from '../services/auth-service.js';
import { avatarService } from '../services/avatar-service.js';
import { authModal } from './auth-modal.js';
import { eventBus } from '../core/event-bus.js';

export class TopBar {
  constructor(elementId = 'mobile-top-bar') {
    this.elementId = elementId;
    this.el = null;

    eventBus.on('auth:state-change', () => this.updateUserPill());
    eventBus.on('sync:state', (s) => this.updateSyncState(s));
  }

  mount(el) {
    this.el = el || document.getElementById(this.elementId);
    this.updateUserPill();
    this._bindEvents();
  }

  updateUserPill() {
    if (!this.el) {
      this.el = document.getElementById(this.elementId);
      if (!this.el) return;
    }

    const user = authService.getCurrentUser() || {
      nickname: 'Scholar',
      isAnonymous: true
    };

    let userPill = this.el.querySelector('#top-user-pill');
    if (!userPill) {
      const rightContainer = this.el.querySelector('.top-bar-right');
      if (rightContainer) {
        userPill = document.createElement('button');
        userPill.id = 'top-user-pill';
        userPill.className = 'top-user-pill-btn';
        userPill.title = 'User Profile & Cloud Sync';
        rightContainer.prepend(userPill);
      }
    }

    if (userPill) {
      const miniAvatar = avatarService.generateAvatarSvg(user.nickname, { size: 28, animated: true });
      userPill.innerHTML = `
        <div class="mini-avatar-holder">${miniAvatar}</div>
        <span class="mini-nickname">${user.nickname}</span>
        <span class="mini-sync-dot live" id="mini-sync-dot" title="Cloud Synced"></span>
      `;
    }
  }

  updateSyncState({ state }) {
    const dot = this.el?.querySelector('#mini-sync-dot');
    if (!dot) return;
    if (state === 'synced') {
      dot.className = 'mini-sync-dot live';
    } else if (state === 'syncing') {
      dot.className = 'mini-sync-dot syncing';
    } else {
      dot.className = 'mini-sync-dot offline';
    }
  }

  _bindEvents() {
    const userPill = this.el?.querySelector('#top-user-pill');
    if (userPill) {
      userPill.addEventListener('click', () => {
        const user = authService.getCurrentUser();
        if (user && user.isAnonymous) {
          authModal.show('signup');
        } else {
          const tabBtn = document.querySelector('[data-tab="settings"]');
          if (tabBtn) tabBtn.click();
        }
      });
    }
  }
}

export const topBar = new TopBar();
