/**
 * Vocab App — Multi-Provider Auth Modal Component
 * 
 * Features:
 * - Live Animated SVG Avatar Preview that dynamically updates as nickname is typed
 * - "🎲 Roll Random Nickname" button
 * - Tab switching: Join with Nickname | Sign In | Guest
 * - Social Auth: Google, Facebook, GitHub
 * - Email & Password with show/hide toggle
 */

import { authService } from '../services/auth-service.js';
import { avatarService } from '../services/avatar-service.js';
import { eventBus } from '../core/event-bus.js';

export class AuthModal {
  constructor() {
    this.isOpen = false;
    this.activeTab = 'signup'; // 'signup' | 'login'
    this.currentNickname = avatarService.rollNickname();
    this.modalEl = null;

    this._createDOM();
    this._bindEvents();
  }

  _createDOM() {
    let existing = document.getElementById('vocab-auth-modal');
    if (existing) existing.remove();

    const wrapper = document.createElement('div');
    wrapper.id = 'vocab-auth-modal';
    wrapper.className = 'auth-modal-overlay';
    wrapper.style.display = 'none';

    wrapper.innerHTML = `
      <div class="auth-modal-backdrop"></div>
      <div class="auth-modal-dialog">
        <!-- Close Button -->
        <button class="auth-modal-close" id="auth-btn-close" aria-label="Close">✕</button>

        <!-- Dynamic Avatar Preview Container -->
        <div class="auth-avatar-section">
          <div class="auth-avatar-stage" id="auth-avatar-stage">
            ${avatarService.generateAvatarSvg(this.currentNickname, { size: 96, animated: true })}
          </div>
          <div class="auth-archetype-tag" id="auth-archetype-tag">
            ${avatarService.getAvatarMeta(this.currentNickname).archetype}
          </div>
          <button type="button" class="auth-dice-btn" id="auth-btn-dice" title="Roll Random Nickname">
            <span>🎲</span> Roll Random Nickname
          </button>
        </div>

        <!-- Segmented Tab Switcher -->
        <div class="auth-tabs-row">
          <button class="auth-tab-btn active" data-tab="signup" id="auth-tab-signup">Create Account</button>
          <button class="auth-tab-btn" data-tab="login" id="auth-tab-login">Sign In</button>
        </div>

        <!-- Error / Status Notice -->
        <div class="auth-notice-banner" id="auth-notice-banner" style="display: none;"></div>

        <!-- Social Sign-In Buttons -->
        <div class="auth-social-row">
          <button class="social-btn google" id="auth-btn-google" title="Continue with Google">
            <svg width="18" height="18" viewBox="0 0 24 24"><path fill="#4285F4" d="M23.745 12.27c0-.7-.06-1.4-.19-2.07H12v4.51h6.6c-.29 1.52-1.14 2.8-2.4 3.66v3.05h3.87c2.26-2.09 3.67-5.17 3.67-9.15z"/><path fill="#34A853" d="M12 24c3.24 0 5.95-1.08 7.93-2.91l-3.87-3.05c-1.08.72-2.45 1.16-4.06 1.16-3.13 0-5.78-2.11-6.73-4.96H1.28v3.15C3.26 21.36 7.35 24 12 24z"/><path fill="#FBBC05" d="M5.27 14.24A7.18 7.18 0 0 1 4.9 12c0-.78.14-1.54.37-2.24V6.61H1.28A11.96 11.96 0 0 0 0 12c0 1.92.45 3.74 1.28 5.39l3.99-3.15z"/><path fill="#EA4335" d="M12 4.75c1.77 0 3.35.61 4.6 1.8l3.42-3.42C17.95 1.19 15.24 0 12 0 7.35 0 3.26 2.64 1.28 6.61l3.99 3.15c.95-2.85 3.6-4.96 6.73-4.96z"/></svg>
            <span>Google</span>
          </button>
          <button class="social-btn facebook" id="auth-btn-facebook" title="Continue with Facebook">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="#1877F2"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
            <span>Facebook</span>
          </button>
          <button class="social-btn github" id="auth-btn-github" title="Continue with GitHub">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/></svg>
            <span>GitHub</span>
          </button>
        </div>

        <div class="auth-divider">
          <span>or with email</span>
        </div>

        <!-- Form: Email & Password -->
        <form class="auth-form" id="auth-main-form" autocomplete="on">
          <!-- Nickname input (only in Signup mode) -->
          <div class="auth-input-group" id="auth-group-nickname">
            <label for="auth-input-nickname">Fun Nickname</label>
            <div class="auth-input-wrapper">
              <span class="auth-input-icon">👑</span>
              <input type="text" id="auth-input-nickname" placeholder="e.g. CosmicAthena" value="${this.currentNickname}" maxlength="24" autocomplete="username" spellcheck="false" required />
            </div>
            <div class="auth-input-hint">Your unique moniker and animated avatar</div>
          </div>

          <!-- Email Input -->
          <div class="auth-input-group">
            <label for="auth-input-email">Email Address</label>
            <div class="auth-input-wrapper">
              <span class="auth-input-icon">✉️</span>
              <input type="email" id="auth-input-email" placeholder="you@example.com" autocomplete="email" required />
            </div>
          </div>

          <!-- Password Input -->
          <div class="auth-input-group">
            <div class="auth-label-row">
              <label for="auth-input-password">Password</label>
              <button type="button" class="auth-forgot-btn" id="auth-btn-forgot" style="display: none;">Forgot?</button>
            </div>
            <div class="auth-input-wrapper">
              <span class="auth-input-icon">🔒</span>
              <input type="password" id="auth-input-password" placeholder="At least 6 characters" minlength="6" autocomplete="current-password" required />
              <button type="button" class="auth-eye-btn" id="auth-btn-eye">👁️</button>
            </div>
          </div>

          <!-- Primary Submit Button -->
          <button type="submit" class="auth-submit-btn" id="auth-btn-submit">
            <span id="auth-submit-label">Create Profile &amp; Start</span>
            <span class="auth-btn-spinner" id="auth-btn-spinner" style="display: none;">⏳</span>
          </button>
        </form>

        <!-- Guest Access Footer -->
        <div class="auth-guest-footer">
          <button type="button" class="auth-guest-link" id="auth-btn-guest">
            🚀 Continue as Guest (explore offline first)
          </button>
        </div>

      </div>
    `;

    document.body.appendChild(wrapper);
    this.modalEl = wrapper;
  }

  _bindEvents() {
    const el = this.modalEl;
    if (!el) return;

    // Close on backdrop or close button
    el.querySelector('.auth-modal-backdrop').addEventListener('click', () => this.hide());
    el.querySelector('#auth-btn-close').addEventListener('click', () => this.hide());

    // Switch Tabs
    const tabSignup = el.querySelector('#auth-tab-signup');
    const tabLogin = el.querySelector('#auth-tab-login');
    const groupNickname = el.querySelector('#auth-group-nickname');
    const btnForgot = el.querySelector('#auth-btn-forgot');
    const submitLabel = el.querySelector('#auth-submit-label');

    tabSignup.addEventListener('click', () => {
      this.activeTab = 'signup';
      tabSignup.classList.add('active');
      tabLogin.classList.remove('active');
      groupNickname.style.display = 'block';
      btnForgot.style.display = 'none';
      submitLabel.textContent = 'Create Profile & Start';
      this.clearNotice();
    });

    tabLogin.addEventListener('click', () => {
      this.activeTab = 'login';
      tabLogin.classList.add('active');
      tabSignup.classList.remove('active');
      groupNickname.style.display = 'none';
      btnForgot.style.display = 'inline-block';
      submitLabel.textContent = 'Sign In to Vocab App';
      this.clearNotice();
    });

    // Roll Random Nickname
    const diceBtn = el.querySelector('#auth-btn-dice');
    const nickInput = el.querySelector('#auth-input-nickname');

    diceBtn.addEventListener('click', () => {
      const rolled = avatarService.rollNickname();
      this.currentNickname = rolled;
      nickInput.value = rolled;
      this._updateAvatarPreview(rolled);
    });

    // Dynamic Live Avatar Update as user types
    nickInput.addEventListener('input', (e) => {
      const val = e.target.value.trim() || 'Guest';
      this.currentNickname = val;
      this._updateAvatarPreview(val);
    });

    // Show/Hide Password
    const eyeBtn = el.querySelector('#auth-btn-eye');
    const passInput = el.querySelector('#auth-input-password');
    eyeBtn.addEventListener('click', () => {
      const isPass = passInput.type === 'password';
      passInput.type = isPass ? 'text' : 'password';
      eyeBtn.textContent = isPass ? '🙈' : '👁️';
    });

    // Forgot Password
    btnForgot.addEventListener('click', async () => {
      const email = el.querySelector('#auth-input-email').value.trim();
      if (!email) {
        this.showNotice('Please enter your email above to receive a password reset link.', 'info');
        return;
      }
      try {
        await authService.sendPasswordReset(email);
        this.showNotice(`Password reset email sent to ${email}! Check your inbox.`, 'success');
      } catch (err) {
        this.showNotice(err.message, 'error');
      }
    });

    // Form Submit
    const form = el.querySelector('#auth-main-form');
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const email = el.querySelector('#auth-input-email').value.trim();
      const password = passInput.value;
      const nickname = nickInput.value.trim();

      this._setLoading(true);
      this.clearNotice();

      try {
        if (this.activeTab === 'signup') {
          await authService.signUpWithEmail(email, password, nickname);
          this.showNotice(`🎉 Welcome aboard, ${nickname}!`, 'success');
        } else {
          const user = await authService.signInWithEmail(email, password);
          this.showNotice(`🎉 Welcome back, ${user.nickname}!`, 'success');
        }
        setTimeout(() => this.hide(), 700);
      } catch (err) {
        this.showNotice(err.message, 'error');
      } finally {
        this._setLoading(false);
      }
    });

    // Social Buttons
    el.querySelector('#auth-btn-google').addEventListener('click', async () => {
      this._setLoading(true);
      try {
        const u = await authService.signInWithGoogle();
        this.showNotice(`Signed in as ${u.nickname}!`, 'success');
        setTimeout(() => this.hide(), 600);
      } catch (e) {
        this.showNotice(e.message, 'error');
      } finally {
        this._setLoading(false);
      }
    });

    el.querySelector('#auth-btn-facebook').addEventListener('click', async () => {
      this._setLoading(true);
      try {
        const u = await authService.signInWithFacebook();
        this.showNotice(`Signed in as ${u.nickname}!`, 'success');
        setTimeout(() => this.hide(), 600);
      } catch (e) {
        this.showNotice(e.message, 'error');
      } finally {
        this._setLoading(false);
      }
    });

    el.querySelector('#auth-btn-github').addEventListener('click', async () => {
      this._setLoading(true);
      try {
        const u = await authService.signInWithGithub();
        this.showNotice(`Signed in as ${u.nickname}!`, 'success');
        setTimeout(() => this.hide(), 600);
      } catch (e) {
        this.showNotice(e.message, 'error');
      } finally {
        this._setLoading(false);
      }
    });

    // Guest Mode
    el.querySelector('#auth-btn-guest').addEventListener('click', async () => {
      await authService.signInAsGuest();
      this.hide();
    });
  }

  _updateAvatarPreview(nickname) {
    const stage = this.modalEl.querySelector('#auth-avatar-stage');
    const tag = this.modalEl.querySelector('#auth-archetype-tag');
    if (stage) {
      stage.innerHTML = avatarService.generateAvatarSvg(nickname, { size: 96, animated: true });
    }
    if (tag) {
      tag.textContent = avatarService.getAvatarMeta(nickname).archetype;
    }
  }

  showNotice(msg, type = 'error') {
    const banner = this.modalEl.querySelector('#auth-notice-banner');
    if (!banner) return;
    banner.textContent = msg;
    banner.className = `auth-notice-banner ${type}`;
    banner.style.display = 'block';
  }

  clearNotice() {
    const banner = this.modalEl.querySelector('#auth-notice-banner');
    if (banner) banner.style.display = 'none';
  }

  _setLoading(loading) {
    const btn = this.modalEl.querySelector('#auth-btn-submit');
    const spinner = this.modalEl.querySelector('#auth-btn-spinner');
    const label = this.modalEl.querySelector('#auth-submit-label');
    if (btn) btn.disabled = loading;
    if (spinner) spinner.style.display = loading ? 'inline-block' : 'none';
    if (label) label.style.opacity = loading ? '0.5' : '1';
  }

  show(tab = 'signup') {
    this.isOpen = true;
    this.modalEl.style.display = 'flex';
    if (tab === 'login') {
      this.modalEl.querySelector('#auth-tab-login').click();
    } else {
      this.modalEl.querySelector('#auth-tab-signup').click();
    }
  }

  hide() {
    this.isOpen = false;
    this.modalEl.style.display = 'none';
    this.clearNotice();
  }
}

export const authModal = new AuthModal();
