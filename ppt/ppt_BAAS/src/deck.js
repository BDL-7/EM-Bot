(() => {
  'use strict';
  const slides = Array.from(document.querySelectorAll('.slide'));
  const picker = document.getElementById('slide-picker');
  const previous = document.getElementById('previous');
  const next = document.getElementById('next');
  const status = document.getElementById('live-status');
  const sourcesDialog = document.getElementById('sources-dialog');
  const helpDialog = document.getElementById('help-dialog');
  const baseline = 'https://github.com/BDL-7/EM-Bot/blob/dc2d11fae2ecd3d6448d38b32452485fe0469107/';
  const sources = {
    E01: { title: 'Project README', url: baseline + 'README.md', detail: 'Pilot purpose and documented project status at the reviewed commit.' },
    E02: { title: 'EDAV Microbot UI Integration Guide', url: 'https://github.com/cdcent/edav-BaaS/blob/master/README.md', detail: 'Supports embedding the chat interface. It does not establish the pilot’s backend configuration or answer quality.' },
    E03: { title: 'Bot behavior requirements', url: baseline + 'PHASE_3_BEHAVIOR_CONFIGURATION.md', detail: 'Prepared requirements for grounding, citations, clarification, and evaluation. These are not live outcomes.' },
    E04: { title: 'Ten prepared behavior tests', url: baseline + 'PHASE_3_BEHAVIOR_TESTS.md', detail: 'All test-result rows were marked Not run in the inspected baseline.' },
    E05: { title: 'Host implementation and scope', url: baseline + 'README.md#temporary-flask-host', detail: 'The host embeds EDAV chat. It does not implement manual retrieval or the bot.' },
    E07: { title: 'MDN: Browsing the web', url: 'https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Environment_setup/Browsing_the_web', detail: 'Background explanation of browsers and web applications.' },
    E08: { title: 'Microsoft: Designing your bot', url: 'https://learn.microsoft.com/en-us/microsoftteams/platform/bots/design/bots', detail: 'Used for the general conversational-bot concept, not as evidence of EDAV’s internal implementation.' }
  };
  let current = 0;
  let lastDialogTrigger = null;

  function initialIndex() {
    const query = new URLSearchParams(window.location.search).get('slide');
    const hash = window.location.hash.replace(/^#/, '').replace(/^slide-/, '');
    const parsed = Number(query || hash || 1);
    return Number.isInteger(parsed) ? Math.min(slides.length - 1, Math.max(0, parsed - 1)) : 0;
  }

  function resize() {
    const scale = Math.max(0.1, Math.min((window.innerWidth - 20) / 1280, (window.innerHeight - 76) / 720));
    document.documentElement.style.setProperty('--scale', String(scale));
  }

  function show(index, updateLocation = true) {
    current = Math.max(0, Math.min(slides.length - 1, index));
    slides.forEach((slide, i) => {
      const active = i === current;
      slide.classList.toggle('active', active);
      slide.setAttribute('aria-hidden', String(!active));
      slide.inert = !active;
    });
    picker.value = String(current);
    previous.disabled = current === 0;
    next.disabled = current === slides.length - 1 && !slides[current].querySelector('.reveal[hidden]');
    status.textContent = `Slide ${current + 1} of ${slides.length}: ${slides[current].dataset.title}`;
    document.title = `${current + 1} · ${slides[current].dataset.title} · EDAV BaaS`;
    if (updateLocation) {
      try { window.history.replaceState(null, '', `#${current + 1}`); } catch (_) { /* file viewers may restrict history */ }
    }
  }

  function reveal(target) {
    if (!target) return;
    target.hidden = false;
    const trigger = document.querySelector(`[data-reveal-target="${target.id}"]`);
    if (trigger) trigger.setAttribute('aria-expanded', 'true');
    status.textContent = target.textContent.trim();
    next.disabled = current === slides.length - 1 && !slides[current].querySelector('.reveal[hidden]');
  }

  function advance() {
    const unrevealed = slides[current].querySelector('.reveal[hidden]');
    if (unrevealed) reveal(unrevealed);
    else show(current + 1);
  }

  function openDialog(dialog, trigger) {
    lastDialogTrigger = trigger || document.activeElement;
    if (!dialog.open) dialog.showModal();
  }

  function openSources(trigger) {
    const slide = slides[current];
    document.getElementById('sources-title').textContent = `Sources · slide ${current + 1}`;
    document.getElementById('source-scope').textContent = slide.dataset.scope;
    const list = document.getElementById('source-list');
    list.replaceChildren();
    for (const id of slide.dataset.sources.split(',')) {
      const source = sources[id];
      if (!source) continue;
      const item = document.createElement('li');
      const link = document.createElement('a');
      link.href = source.url;
      link.target = '_blank';
      link.rel = 'noopener noreferrer';
      link.textContent = source.title;
      const detail = document.createElement('span');
      detail.className = 'source-detail';
      detail.textContent = source.detail;
      item.append(link, detail);
      list.append(item);
    }
    openDialog(sourcesDialog, trigger);
  }

  async function fullscreen() {
    try {
      if (document.fullscreenElement) await document.exitFullscreen();
      else if (document.documentElement.requestFullscreen) await document.documentElement.requestFullscreen();
      else status.textContent = 'Fullscreen is unavailable in this viewer.';
    } catch (_) { status.textContent = 'Fullscreen is unavailable in this viewer. You can use the browser’s fullscreen control.'; }
  }

  slides.forEach((slide, index) => {
    const option = document.createElement('option');
    option.value = String(index);
    option.textContent = `${String(index + 1).padStart(2, '0')} / ${slides.length} · ${slide.dataset.title}`;
    picker.append(option);
  });
  previous.addEventListener('click', () => show(current - 1));
  next.addEventListener('click', advance);
  picker.addEventListener('change', () => show(Number(picker.value)));
  document.getElementById('sources-open').addEventListener('click', event => openSources(event.currentTarget));
  document.getElementById('help-open').addEventListener('click', event => openDialog(helpDialog, event.currentTarget));
  document.getElementById('fullscreen').addEventListener('click', fullscreen);
  document.querySelectorAll('[data-reveal-target]').forEach(button => {
    button.addEventListener('click', () => reveal(document.getElementById(button.dataset.revealTarget)));
  });
  document.querySelectorAll('[data-quiz]').forEach(button => {
    button.addEventListener('click', () => {
      document.querySelectorAll('[data-quiz]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
      document.getElementById('quiz-result').textContent = button.dataset.quiz === 'records'
        ? 'Yes—current records. A manual cannot establish what happened to this instrument today.'
        : 'Use current records. The bot should explain the gap rather than infer today’s status from a manual.';
    });
  });
  document.querySelectorAll('[data-close]').forEach(button => {
    button.addEventListener('click', () => document.getElementById(button.dataset.close).close());
  });
  [sourcesDialog, helpDialog].forEach(dialog => {
    dialog.addEventListener('close', () => {
      if (lastDialogTrigger && typeof lastDialogTrigger.focus === 'function') lastDialogTrigger.focus();
    });
  });
  document.addEventListener('keydown', event => {
    if (event.ctrlKey || event.metaKey || event.altKey || sourcesDialog.open || helpDialog.open) return;
    const target = event.target;
    if (target && (target.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(target.tagName))) return;
    if (target && target.tagName === 'BUTTON' && (event.key === ' ' || event.key === 'Enter')) return;
    const actions = {
      ArrowRight: advance, PageDown: advance, ' ': advance,
      ArrowLeft: () => show(current - 1), PageUp: () => show(current - 1),
      Home: () => show(0), End: () => show(slides.length - 1),
      f: fullscreen, F: fullscreen,
      s: () => openSources(), S: () => openSources(),
      p: () => window.print(), P: () => window.print(),
      '?': () => openDialog(helpDialog)
    };
    if (actions[event.key]) { event.preventDefault(); actions[event.key](); }
  });
  window.addEventListener('resize', resize);
  window.addEventListener('hashchange', () => {
    const parsed = Number(window.location.hash.replace(/^#/, ''));
    if (Number.isInteger(parsed) && parsed >= 1 && parsed <= slides.length) show(parsed - 1, false);
  });
  window.addEventListener('beforeprint', () => slides.forEach(slide => { slide.inert = false; slide.removeAttribute('aria-hidden'); }));
  window.addEventListener('afterprint', () => show(current, false));
  document.body.classList.remove('no-js');
  document.body.classList.add('enhanced');
  resize();
  show(initialIndex(), false);
})();
