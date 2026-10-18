(() => {
  'use strict';

  document.querySelectorAll('[data-year]').forEach((element) => {
    element.textContent = String(new Date().getFullYear());
  });

  const menuButton = document.querySelector('.menu-toggle');
  const mobileNav = document.querySelector('#mobile-nav');
  const header = document.querySelector('.site-header');
  const setMenu = (open, restoreFocus = false) => {
    if (!menuButton || !mobileNav) return;
    menuButton.setAttribute('aria-expanded', String(open));
    menuButton.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
    mobileNav.hidden = !open;
    document.body.classList.toggle('menu-open', open);
    updateScrollUI();
    if (restoreFocus) menuButton.focus();
  };

  if (menuButton && mobileNav) {
    menuButton.addEventListener('click', () => {
      setMenu(menuButton.getAttribute('aria-expanded') !== 'true');
    });
    mobileNav.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => setMenu(false));
    });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && !mobileNav.hidden) setMenu(false, true);
    });
    document.addEventListener('click', (event) => {
      if (!mobileNav.hidden && !mobileNav.contains(event.target) && !menuButton.contains(event.target)) {
        setMenu(false);
      }
    });
    const desktop = window.matchMedia('(min-width: 961px)');
    desktop.addEventListener('change', (event) => { if (event.matches) setMenu(false); });
  }

  const mobileCta = document.querySelector('.mobile-contact');
  const heroButton = document.querySelector('.hero-action .button');
  const form = document.querySelector('#conversation-form');
  const sectionLinks = Array.from(document.querySelectorAll('.desktop-nav a[href^="#"], .header-contact[href="#conversation"]'));
  const sectionTargets = sectionLinks.map((link) => document.querySelector(link.getAttribute('href')));
  let scrollFrame = null;

  function updateScrollUI() {
    scrollFrame = null;
    const headerBottom = header ? header.getBoundingClientRect().bottom : 0;
    if (mobileCta && heroButton && form) {
      const buttonBottom = heroButton.getBoundingClientRect().bottom;
      const formRect = form.getBoundingClientRect();
      const formUsable = formRect.top < window.innerHeight - 100 && formRect.bottom > headerBottom;
      const editing = /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement?.tagName || '');
      const menuOpen = menuButton?.getAttribute('aria-expanded') === 'true';
      mobileCta.classList.toggle('is-visible', buttonBottom <= headerBottom && !formUsable && !editing && !menuOpen);
    }
    let current = -1;
    sectionTargets.forEach((section, index) => {
      if (section && section.getBoundingClientRect().top <= headerBottom + 135) current = index;
    });
    sectionLinks.forEach((link, index) => {
      if (index === current) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  }

  const requestScrollUI = () => {
    if (scrollFrame === null) scrollFrame = window.requestAnimationFrame(updateScrollUI);
  };
  window.addEventListener('scroll', requestScrollUI, { passive: true });
  window.addEventListener('resize', requestScrollUI);
  window.addEventListener('load', requestScrollUI);
  document.addEventListener('focusin', requestScrollUI);
  document.addEventListener('focusout', requestScrollUI);
  window.visualViewport?.addEventListener('resize', requestScrollUI);
  updateScrollUI();

  const situations = Array.from(document.querySelectorAll('.situations details'));
  situations.forEach((detail) => {
    detail.addEventListener('toggle', () => {
      if (detail.open) situations.forEach((other) => { if (other !== detail) other.open = false; });
      requestScrollUI();
    });
  });

  if (!form) return;
  const submitButton = document.querySelector('#submit-request');
  const buttonLabel = submitButton.querySelector('.button-label');
  const errorBox = document.querySelector('#form-error');

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    if (submitButton.disabled || !form.reportValidity()) return;
    submitButton.disabled = true;
    submitButton.setAttribute('aria-busy', 'true');
    buttonLabel.textContent = 'Sending your request…';
    errorBox.hidden = true;

    const controller = new AbortController();
    const timeout = window.setTimeout(() => controller.abort(), 15000);
    try {
      const response = await fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' },
        signal: controller.signal
      });
      if (!response.ok) throw new Error('Request not confirmed');
      window.location.assign('/thankyou.html');
    } catch (_error) {
      errorBox.hidden = false;
      errorBox.focus();
      submitButton.disabled = false;
      submitButton.removeAttribute('aria-busy');
      buttonLabel.textContent = 'Request my conversation';
    } finally {
      window.clearTimeout(timeout);
    }
  });
})();
