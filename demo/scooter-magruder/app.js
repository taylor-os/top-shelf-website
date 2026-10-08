/* Scooter Magruder demo. Every page renders from data.js (window.SM); no facts live in this file. */
(() => {
  'use strict';
  const D = window.SM;
  if (!D) return;

  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const page = document.body.dataset.page;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const EXT = 'target="_blank" rel="noopener"';
  let lenis = null;

  /* ---------- helpers ---------- */
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const fmtDate = (iso) => new Date(iso + 'T12:00:00').toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
  const fmtDur = (s) => `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;
  const compact = (n) => new Intl.NumberFormat('en-US', { notation: 'compact', maximumFractionDigits: 1 }).format(n);
  const int = (n) => Math.round(n).toLocaleString('en-US');
  const asOf = `as of ${fmtDate(D.show.statsAsOf)}`;
  const plain = (t) => t.toLowerCase().replace(/[‘’]/g, "'");
  const matches = (text, q) => plain(text).includes(plain(q.trim()));
  const pick = (path) => path.split('.').reduce((o, k) => o?.[k], D); // "show.subscribeUrl" -> value in data.js
  const uniq = (list) => [...new Set(list)];

  const SERIES = uniq(D.videos.map((v) => v.series)); // order of appearance; index picks the colour tone
  const tone = (series) => `t${SERIES.indexOf(series)}`;

  const media = (src, alt, w, h, cls, inner = '', attrs = 'loading="lazy"') =>
    `<span class="media ${cls}"><img src="${esc(src)}" alt="${esc(alt)}" width="${w}" height="${h}" decoding="async" referrerpolicy="no-referrer" ${attrs}>${inner}</span>`;

  // Hotlinked images: fall back once if a data-fallback is set, otherwise hide and let the colour block show.
  // (load/error don't bubble, so listen in the capture phase.)
  const swapOrHide = (img) => {
    if (img.dataset.fallback) { img.src = img.dataset.fallback; delete img.dataset.fallback; }
    else img.classList.add('failed');
  };
  document.addEventListener('error', (e) => { if (e.target.tagName === 'IMG') swapOrHide(e.target); }, true);
  // YouTube answers a missing thumbnail with a 120px grey placeholder instead of an error.
  document.addEventListener('load', (e) => {
    const img = e.target;
    if (img.tagName === 'IMG' && img.dataset.fallback && img.naturalWidth <= 120) swapOrHide(img);
  }, true);

  /* ---------- shared components ---------- */
  const videoCard = (v) => `
    <button type="button" class="card" data-video="${v.id}" data-reveal>
      ${media(v.thumb, '', 480, 270, 'r16', `<span class="dur">${fmtDur(v.seconds)}</span>`)}
      <span class="card-body">
        <span class="tag ${tone(v.series)}">${esc(v.series)}</span>
        <span class="card-title">${esc(v.title)}</span>
        <span class="meta">${fmtDate(v.date)} · ${compact(v.views)} views</span>
      </span>
    </button>`;

  const productCard = (p) => `
    <article class="card product" data-reveal>
      ${media(p.image, `${p.name} ${p.type}`, 800, 800, 'r11')}
      <div class="card-body">
        <p class="meta">${esc(p.name)}</p>
        <h3 class="card-title">${esc(p.type)}</h3>
        <p class="price">$${esc(p.price)}</p>
        <a class="btn sm" href="${esc(p.url)}" ${EXT}>Get it<span class="sr-only">: ${esc(p.name)} ${esc(p.type)} on the ${esc(D.merch.storeName)} store</span></a>
      </div>
    </article>`;

  const MAIL_SHORT = ['Business', 'Social', 'Film agent']; // footer link text only; the cards use his own labels from data.js

  // Blocks that appear on more than one page. A page asks for one with <div data-slot="roles">.
  const SLOTS = {
    roles: () => `<div class="roles">${D.show.roles.map((r, i) => `
      <article class="role t${i}" data-reveal><h3>${esc(r.title)}</h3><p>${esc(r.text)}</p></article>`).join('')}</div>`,
    featured: () => `
      <ul class="feat">${D.show.featuredBy.map((n) => `<li>${esc(n)}</li>`).join('')}</ul>
      <p class="fine">Outlets as listed in his bio on <a href="${D.show.website}" ${EXT}>scootermagruder.com</a>.</p>`,
    channels: () => `<div class="channels">${D.otherChannels.map((c) => `
      <a class="channel" href="${esc(c.url)}" ${EXT} data-reveal>
        <h3>${esc(c.name)}</h3><p>${esc(c.text)}</p><span class="go">Visit the channel</span>
      </a>`).join('')}</div>`,
    mail: () => `<div class="mails">${D.contact.inboxes.map((m, i) => `
      <article class="mail t${i}" data-reveal>
        <h3>${esc(m.label)}</h3>
        <a class="mail-addr" href="mailto:${esc(m.email)}">${esc(m.email)}</a>
      </article>`).join('')}</div>
      <p class="fine">${esc(D.contact.labelsSource)}</p>`,
  };

  /* Hero sticker: the channel's public subscriber count, re-read from YouTube while the page is open. */
  function subsSticker(el) {
    let shown;
    const paint = (text, live) => {
      const html = `<b>${esc(text)}</b><span>YouTube subscribers</span><small>${live ? '<i></i>Live count' : `Count ${asOf}`}</small>`;
      if (html !== shown) el.innerHTML = shown = html; // repaint only on change, so the slap animation doesn't replay every poll
    };
    paint(D.show.subscribers, false);
    const FRESH = 30 * 60 * 1000; // subs.php can serve an old cached count when YouTube is unreachable; that is not "live"
    const pull = async () => {
      let live = null;
      try {
        const r = await fetch('subs.php', { cache: 'no-store' });
        const j = await r.json();
        if (r.ok && j.count && Date.now() - Date.parse(j.fetchedAt) < FRESH) live = j.text;
      } catch { /* no PHP here (local preview) or YouTube unreachable: keep the dated number */ }
      paint(live ?? D.show.subscribers, Boolean(live));
    };
    pull();
    setInterval(pull, 5 * 60 * 1000);
  }

  // The catchphrase button: one phrase at a time, press for the next. Phrases are stacked so nothing jumps.
  function catchphrases(el) {
    const list = D.show.catchphrases;
    let i = 0;
    el.innerHTML = `
      <p class="cp-stage">${list.map((c, n) => `<span${n ? ' aria-hidden="true"' : ' class="on"'}>${esc(c)}</span>`).join('')}</p>
      <div class="btn-row"><button type="button" class="btn alt">Next one</button><span class="cp-n">1 of ${list.length}</span></div>
      <span class="sr-only" role="status"></span>`;
    const spans = $$('.cp-stage span', el);
    $('button', el).addEventListener('click', () => {
      i = (i + 1) % list.length;
      spans.forEach((s, n) => { s.classList.toggle('on', n === i); s.setAttribute('aria-hidden', String(n !== i)); });
      $('.cp-n', el).textContent = `${i + 1} of ${list.length}`;
      $('[role="status"]', el).textContent = list[i];
    });
  }

  // Filter chips: one pressed at a time. Calls onPick(label) on change.
  function chips(el, labels, active, onPick) {
    el.innerHTML = labels.map((l) => `<button type="button" class="chip" aria-pressed="${l === active}">${esc(l)}</button>`).join('');
    el.addEventListener('click', (e) => {
      const b = e.target.closest('.chip');
      if (!b) return;
      $$('.chip', el).forEach((c) => c.setAttribute('aria-pressed', String(c === b)));
      onPick(b.textContent);
    });
  }

  /* ---------- chrome ---------- */
  const NAV = [['videos.html', 'Videos', 'videos'], ['about.html', 'About', 'about'], ['press.html', 'Press', 'press'],
    ['merch.html', 'Merch', 'merch'], ['socials.html', 'Socials', 'socials'], ['partners.html', 'Work with Scooter', 'partners'],
    ['contact.html', 'Contact', 'contact']];
  const current = (key) => (key === page ? ' aria-current="page"' : '');

  function chrome() {
    const [first, last] = D.show.name.split(' ');
    const head = $('#site-head');
    head.innerHTML = `
      <div class="wrap head-in">
        <a class="brand" href="index.html" aria-label="${esc(D.show.name)} home">${esc(first)} <span>${esc(last)}</span></a>
        <button type="button" class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
        <nav class="nav" id="nav" aria-label="Main">
          ${NAV.map(([href, label, key]) => `<a href="${href}"${current(key)}>${label}</a>`).join('')}
          <a class="btn sm" href="subscribe.html"${current('subscribe')}>Get updates</a>
        </nav>
      </div>`;
    const btn = $('.menu-btn', head);
    const setOpen = (open) => { head.classList.toggle('open', open); btn.setAttribute('aria-expanded', String(open)); };
    btn.addEventListener('click', () => setOpen(!head.classList.contains('open')));
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && head.classList.contains('open')) { setOpen(false); btn.focus(); }
    });

    $('#site-foot').innerHTML = `
      <div class="wrap">
        <div class="foot-grid">
          <div>
            <p class="foot-name">${esc(D.show.name)}</p>
            <p>${esc(D.show.tagline)}</p>
          </div>
          <div>
            <p class="foot-h">Explore</p>
            <ul>${NAV.map(([href, label]) => `<li><a href="${href}">${label}</a></li>`).join('')}<li><a href="subscribe.html">Get updates</a></li></ul>
          </div>
          <div>
            <p class="foot-h">Follow</p>
            <ul>${D.socials.map((s) => `<li><a href="${esc(s.url)}" ${EXT}>${esc(s.name)}</a></li>`).join('')}</ul>
          </div>
          <div>
            <p class="foot-h">Email</p>
            <ul>${D.contact.inboxes.map((m, i) => `<li><a href="mailto:${esc(m.email)}">${MAIL_SHORT[i]}<span class="sr-only">: ${esc(m.email)}</span></a></li>`).join('')}</ul>
          </div>
        </div>
        <div class="foot-legal">
          <p>Independent creator site. Not affiliated with the NFL, the NBA, any team, or the outlets named.</p>
          <p>Concept demo by Top Shelf Business Solutions.</p>
        </div>
      </div>`;
  }

  /* ---------- video player (native <dialog>: Esc closes, focus is trapped and returned) ---------- */
  function player() {
    const dlg = document.createElement('dialog');
    dlg.className = 'player';
    dlg.setAttribute('aria-labelledby', 'player-title');
    dlg.innerHTML = `
      <div class="player-box">
        <div class="player-bar"><h2 id="player-title"></h2><button type="button" class="btn sm alt">Close</button></div>
        <div class="player-frame"></div>
        <div class="player-meta meta"></div>
      </div>`;
    document.body.append(dlg);
    const frame = $('.player-frame', dlg);
    $('button', dlg).addEventListener('click', () => dlg.close());
    dlg.addEventListener('click', (e) => { if (e.target === dlg) dlg.close(); }); // backdrop click
    dlg.addEventListener('close', () => { frame.innerHTML = ''; lenis?.start(); });
    document.addEventListener('click', (e) => {
      const v = D.videos.find((x) => x.id === e.target.closest('[data-video]')?.dataset.video);
      if (!v) return;
      $('#player-title').textContent = v.title;
      frame.innerHTML = `<iframe src="https://www.youtube-nocookie.com/embed/${v.id}?autoplay=1" title="${esc(v.title)}" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe>`;
      $('.player-meta', dlg).innerHTML = `<span>${fmtDate(v.date)} · ${int(v.views)} views · ${fmtDur(v.seconds)}</span><a href="${esc(v.url)}" ${EXT}>Watch on YouTube</a>`;
      lenis?.stop();
      dlg.showModal();
    });
  }

  /* ---------- demo signup forms: no network request, nothing stored ---------- */
  function forms() {
    const EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
    $$('form[data-demo]').forEach((form) => {
      form.noValidate = true;
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const email = form.elements.email;
        const boxes = $$('input[type="checkbox"]', form);
        const picked = boxes.filter((b) => b.checked).map((b) => b.value);
        const emailOk = EMAIL.test(email.value.trim());
        email.setAttribute('aria-invalid', String(!emailOk));
        const err = $('[data-error]', form);
        if (!emailOk) { err.textContent = 'That email address doesn’t look right. Check it and try again.'; return email.focus(); }
        if (boxes.length && !picked.length) { err.textContent = 'Pick at least one series.'; return boxes[0].focus(); }
        const name = form.elements.firstName?.value.trim();
        const wants = picked.length ? new Intl.ListFormat('en').format(picked) : 'new videos';
        const done = document.createElement('div');
        done.className = 'success';
        done.setAttribute('role', 'status');
        done.tabIndex = -1;
        done.innerHTML = `
          <p class="tag">Demo form</p>
          <p class="name">You’re in${name ? `, ${esc(name)}` : ''}.</p>
          <p>This is a demo, so nothing was sent and nothing was saved. On the live site, ${esc(email.value.trim())} would get updates for: ${esc(wants)}.</p>`;
        form.replaceWith(done);
        done.focus();
      });
    });
  }

  /* ---------- pages ---------- */
  const pages = {
    home() {
      const v = D.videos[0], s = D.show;
      $('#hero-hash').innerHTML = s.hashtags.map((h) => `<li class="tag">${esc(h)}</li>`).join('');
      $('#hero-art').innerHTML = `${media(s.hostPhoto, s.name, 754, 754, 'r11 hero-photo', '', 'fetchpriority="high"')}<div class="subs" id="subs"></div>`;
      subsSticker($('#subs'));
      $('#home-latest').innerHTML = `
        <button type="button" class="frame" data-video="${v.id}" aria-label="Play the latest video: ${esc(v.title)}">
          ${media(`https://i.ytimg.com/vi/${v.id}/maxresdefault.jpg`, '', 1280, 720, 'r16',
            `<span class="play"></span><span class="dur">${fmtDur(v.seconds)}</span>`, `data-fallback="${v.thumb}" loading="lazy"`)}
        </button>
        <div>
          <p class="tag t2 tilt">Latest video</p>
          <h2>${esc(v.title)}</h2>
          <p class="meta">${fmtDate(v.date)} · ${compact(v.views)} views · ${fmtDur(v.seconds)}</p>
          <div class="btn-row">
            <button type="button" class="btn sun" data-video="${v.id}">Play it here</button>
            <a class="btn alt" href="videos.html">All videos</a>
          </div>
        </div>`;
      $('#home-series').innerHTML = SERIES.map((name, i) => {
        const list = D.videos.filter((x) => x.series === name);
        return `
        <a class="tile t${i}" href="videos.html?series=${encodeURIComponent(name)}" data-reveal>
          ${media(list[0].thumb, '', 480, 270, 'r16')}
          <span class="tile-name">${esc(name)}</span>
          <span class="tile-count">${list.length} of the latest ${D.videos.length}</span>
          <span class="tile-new">Newest: ${esc(list[0].title)}</span>
        </a>`;
      }).join('');
      $('#home-rail').innerHTML = D.videos.slice(1, 9).map(videoCard).join('');
      catchphrases($('#home-cp'));
      $('#home-merch').innerHTML = D.merch.products.slice(0, 4).map(productCard).join('');
    },

    videos() {
      const SORT = {
        new: (a, b) => b.date.localeCompare(a.date),
        views: (a, b) => b.views - a.views,
        quick: (a, b) => a.seconds - b.seconds,
      };
      const wanted = new URLSearchParams(location.search).get('series');
      let series = SERIES.includes(wanted) ? wanted : 'All';
      const grid = $('#vid-grid'), q = $('#vid-q'), sort = $('#vid-sort'), count = $('#vid-count');
      const render = () => {
        const list = D.videos.filter((v) => (series === 'All' || v.series === series) && matches(v.title, q.value)).sort(SORT[sort.value]);
        count.textContent = `${list.length} of the ${D.videos.length} latest videos`;
        grid.innerHTML = list.map(videoCard).join('') || '<p class="empty">Nothing matches that. Try one word, like “Cowboys”.</p>';
      };
      chips($('#vid-chips'), ['All', ...SERIES], series, (s) => { series = s; render(); });
      q.addEventListener('input', render);
      sort.addEventListener('change', render);
      render();
    },

    about() {
      const s = D.show;
      $('#about-top').innerHTML = `
        ${media(s.hostPhoto, s.name, 754, 754, 'r11 hero-photo', '', 'fetchpriority="high"')}
        <div>
          <p class="tag t1 tilt">${esc(s.realName)}</p>
          <blockquote class="quote">“${esc(s.intro)}”</blockquote>
          <p class="fine">In his words, from <a href="${s.website}" ${EXT}>scootermagruder.com</a>. On YouTube since ${esc(s.joined)}.</p>
          <div class="btn-row"><a class="btn" href="${s.subscribeUrl}" ${EXT}>Subscribe on YouTube</a><a class="btn alt" href="videos.html">Watch videos</a></div>
        </div>`;
      $('#about-photos').innerHTML = s.photos.map((p) => `
        <figure data-reveal>${media(p.src, '', 768, 1024, 'r34')}<figcaption>${esc(p.alt)}</figcaption></figure>`).join('');
    },

    press() {
      $('#press-list').innerHTML = D.press.map((p) => `
        <li data-reveal><a href="${esc(p.url)}" ${EXT}>
          <span class="press-outlet">${esc(p.outlet)}</span>
          <span class="press-title">${esc(p.title)}${p.linkNote ? `<small class="press-note">${esc(p.linkNote)}</small>` : ''}</span>
          <span class="go">${p.linkNote ? 'Open his press page' : 'Read it'}</span>
        </a></li>`).join('');
    },

    partners() {
      const s = D.show;
      const avg = D.videos.reduce((sum, v) => sum + v.views, 0) / D.videos.length;
      const stat = (i, text, label, count, fmt) =>
        `<div class="stat t${i}" data-reveal><b data-count="${count}" data-fmt="${fmt}">${text}</b><span>${label}</span></div>`;
      $('#pt-stats').innerHTML = `
        <div class="stats">
          ${stat(0, esc(s.subscribers), 'YouTube subscribers', s.subscribersNum, 'compact')}
          ${stat(1, compact(s.totalViews), 'Total YouTube views', s.totalViews, 'compact')}
          ${stat(2, int(s.videoCount), 'Videos published', s.videoCount, 'int')}
          ${stat(3, compact(avg), `Average views per video, computed from the ${D.videos.length} latest uploads`, Math.round(avg), 'compact')}
        </div>
        <p class="fine">Channel numbers ${asOf}, from his public YouTube channel.</p>`;
      // The cross-platform claim is his site's, so it is attributed rather than restated as ours.
      // No quotation marks: data.js is not character-for-character his original (a dash was replaced).
      const claim = s.about.split('. ').find((x) => x.includes('followers'));
      if (claim) {
        $('#pt-stats').insertAdjacentHTML('beforeend',
          `<p class="claim">According to his bio on <a href="${s.website}" ${EXT}>scootermagruder.com</a>: ${esc(claim)}.</p>`);
      }
    },

    merch() {
      const designs = uniq(D.merch.products.map((p) => p.name));
      const grid = $('#merch-grid'), count = $('#merch-count');
      const render = (design) => {
        const list = D.merch.products.filter((p) => design === 'All' || p.name === design);
        count.textContent = `${list.length} of ${D.merch.products.length} products`;
        grid.innerHTML = list.map(productCard).join('');
      };
      chips($('#merch-chips'), ['All', ...designs], 'All', render);
      render('All');
    },

    socials() {
      $('#soc-grid').innerHTML = D.socials.map((s, i) => `
        <a class="social t${i % 3}" href="${esc(s.url)}" ${EXT} data-reveal>
          <span class="social-ic" aria-hidden="true">${esc(s.name.slice(0, 2))}</span>
          <span class="social-txt">
            <span class="social-name">${esc(s.name)}</span>
            <span class="social-handle">${esc(s.handle)}</span>
            ${s.stat ? `<span class="meta">${esc(s.stat)} ${asOf}</span>` : ''}
          </span>
          <span class="go">Follow<span class="sr-only"> on ${esc(s.name)}</span></span>
        </a>`).join('');
    },

    subscribe() {
      $('#sub-series').innerHTML = SERIES.map((name) =>
        `<label><input type="checkbox" name="series" value="${esc(name)}" checked> ${esc(name === 'More' ? 'Everything else' : name)}</label>`).join('');
    },
  };

  /* ---------- motion: enhancement only. Content is visible by default; nothing below runs without GSAP. ---------- */
  function motion() {
    if (reduced || !window.gsap || !window.ScrollTrigger) return;
    const { gsap, ScrollTrigger } = window;
    gsap.registerPlugin(ScrollTrigger);
    gsap.config({ nullTargetWarn: false }); // not every page has a hero or reveal targets
    if (window.Lenis) {
      lenis = new window.Lenis({ lerp: 0.1 });
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add((t) => lenis.raf(t * 1000));
      gsap.ticker.lagSmoothing(0);
    }
    // Everything arrives the same way: slapped on like a sticker, with a little overshoot.
    const slap = 'back.out(1.7)';
    // Opacity, never autoAlpha: visibility:hidden would take unrevealed links and buttons out of the Tab order.
    gsap.from('.hero-h1 span', { yPercent: 50, opacity: 0, duration: 0.7, ease: slap, stagger: 0.1 });
    gsap.from('.hero-photo', { scale: 0.8, opacity: 0, duration: 0.7, ease: slap, delay: 0.15 });
    gsap.from('.subs', { scale: 0, duration: 0.6, ease: 'back.out(2.4)', delay: 0.55 });
    // transition:none so the cards' CSS hover transition doesn't fight the tween; clearProps hands them back after.
    gsap.set('[data-reveal]', { opacity: 0, y: 28, scale: 0.94, transition: 'none' });
    ScrollTrigger.batch('[data-reveal]', {
      start: 'top 94%', once: true,
      onEnter: (els) => gsap.to(els, { opacity: 1, y: 0, scale: 1, duration: 0.55, ease: slap, stagger: 0.06, clearProps: 'all' }),
    });
    $$('[data-count]').forEach((el) => {
      const end = Number(el.dataset.count), final = el.textContent, fmt = el.dataset.fmt === 'int' ? int : compact;
      const n = { v: 0 };
      gsap.to(n, {
        v: end, duration: 1.4, ease: 'power2.out', scrollTrigger: { trigger: el, start: 'top 92%', once: true },
        onUpdate: () => { el.textContent = fmt(n.v); },
        onComplete: () => { el.textContent = final; },
      });
    });
  }

  chrome();
  player();
  // Static markup pulls single values and shared blocks straight from data.js.
  $$('[data-text]').forEach((el) => { el.textContent = pick(el.dataset.text); });
  $$('[data-href]').forEach((el) => { el.href = pick(el.dataset.href); });
  $$('[data-slot]').forEach((el) => { el.innerHTML = SLOTS[el.dataset.slot](); });
  pages[page]?.();
  forms();
  motion();
})();
