/* Scooter Magruder demo, Cowboys theme. Every page renders from data.js (window.SM); no facts live in this file. */
(() => {
  'use strict';
  const D = window.SM;
  if (!D) return;

  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const page = document.body.dataset.page;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const EXT = 'target="_blank" rel="noopener"';
  const S = D.season, TZ = esc(D.team.timezoneLabel);
  let lenis = null;

  /* ---------- helpers ---------- */
  function esc(s) { return String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c])); }
  const noon = (iso) => new Date(iso + 'T12:00:00');
  const fmtDate = (iso) => noon(iso).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
  const fmtDay = (iso) => noon(iso).toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' });
  const fmtDur = (s) => `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;
  const compact = (n) => new Intl.NumberFormat('en-US', { notation: 'compact', maximumFractionDigits: 1 }).format(n);
  const int = (n) => Math.round(n).toLocaleString('en-US');
  const asOf = `as of ${fmtDate(D.show.statsAsOf)}`;
  const plain = (t) => t.toLowerCase().replace(/[‘’]/g, "'");
  const matches = (text, q) => plain(text).includes(plain(q.trim()));
  const pick = (path) => path.split('.').reduce((o, k) => o?.[k], D); // "show.subscribeUrl" -> value in data.js
  const uniq = (list) => [...new Set(list)];

  // Series in order of appearance, with any series named after the team moved to the front. LEAD is the one this theme opens on.
  const teamFirst = (name) => (name.startsWith(D.team.short) ? 0 : 1);
  const SERIES = uniq(D.videos.map((v) => v.series)).sort((a, b) => teamFirst(a) - teamFirst(b));
  const LEAD = SERIES[0];
  const inSeries = (name) => D.videos.filter((v) => v.series === name);
  const tag = (series) => `<span class="tag${series === LEAD ? ' hot' : ''}">${esc(series)}</span>`;

  const media = (src, alt, w, h, cls, inner = '', attrs = 'loading="lazy"') =>
    `<span class="media ${cls}"><img src="${esc(src)}" alt="${esc(alt)}" width="${w}" height="${h}" decoding="async" referrerpolicy="no-referrer" ${attrs}>${inner}</span>`;

  // Hotlinked images: fall back once if a data-fallback is set, otherwise hide and let the panel colour show.
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
        ${tag(v.series)}
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

  /* ---------- season: one ordered list of games, and the clock decides where each one shows ---------- */
  const GAMES = [S.next, ...S.schedule];
  const scored = new Set(S.games.map((g) => g.week));
  const lastScored = Math.max(...scored);

  // next: the first kickoff still ahead. rest: every game still to play, starting with that one
  // (the bye and undated games keep their place).
  // pending: kicked off, but no result in data yet.
  function seasonState(now) {
    const past = (g) => Boolean(g.kickoff) && new Date(g.kickoff).getTime() <= now;
    const i = GAMES.findIndex((g) => g.kickoff && !past(g));
    return {
      next: GAMES[i],
      rest: GAMES.slice(i >= 0 ? i : GAMES.findLastIndex(past) + 1),
      pending: GAMES.filter((g) => past(g) && !scored.has(g.week)),
    };
  }

  const versus = (g) => `${g.home ? 'vs.' : 'at'} ${esc(g.opp)}`;
  const wk = (g) => `<span class="wk"><span>Week</span> <b>${g.week}</b></span>`;
  const place = (g) => `<span class="place"><span class="opp">${versus(g)}</span><span class="site">@ ${esc(g.site)}</span></span>`;

  const schedRow = (g) => (g.bye
    ? `<li class="row bye">${wk(g)}<span class="opp">Bye week</span></li>`
    : `<li class="row sched">${wk(g)}${place(g)}
        <span class="when">${g.date ? `${fmtDay(g.date)} · ${esc(g.time)} ${TZ} · ${esc(g.tv)}` : 'Date and time TBD'}</span>
      </li>`);

  // The W/L badge is always the last cell, so every badge sits on the same right edge whatever the score width.
  const resultRow = (g) => `
    <li class="row result">${wk(g)}${place(g)}
      ${g.result
        ? `<span class="score nb">${esc(g.score)}</span><span class="wl ${g.result}">${g.result}<span class="sr-only">${g.result === 'W' ? ' win' : ' loss'}</span></span>`
        : '<span class="pending">Final pending</span><span class="wl" aria-hidden="true"></span>'}
    </li>`;

  // The next game as a ticket: the game on the body, the countdown on the stub.
  const ticket = (n) => {
    const k = new Date(n.kickoff);
    const local = k.toLocaleString(undefined, { weekday: 'short', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit', timeZoneName: 'short' });
    return `
    <article class="ticket" data-reveal>
      <div class="tk-main">
        <p class="kicker">Next game · Week ${n.week}</p>
        <p class="tk-opp"><span>${esc(D.team.short)}</span> ${versus(n)}</p>
        <p class="site">@ ${esc(n.site)}</p>
        <dl class="tk-facts">
          <div><dt>Date</dt><dd>${fmtDay(n.date)}</dd></div>
          <div><dt>Kickoff</dt><dd>${esc(n.time)} ${TZ}</dd></div>
          <div><dt>TV</dt><dd>${esc(n.tv)}</dd></div>
        </dl>
        <p class="fine">${esc(local)}, your time</p>
      </div>
      <div class="tk-stub">
        <p class="kicker">Kickoff in</p>
        <div class="cd" data-countdown="${k.getTime()}" role="timer" aria-label="Countdown to kickoff">
          ${['days', 'hrs', 'min', 'sec'].map((u) => `<span><b>--</b><i>${u}</i></span>`).join('')}
        </div>
      </div>
    </article>`;
  };

  // Paints the next-game ticket (home and season pages), then the results and remaining schedule (season page).
  function paintSeason() {
    const { next, rest, pending } = seasonState(Date.now());
    const slot = $('#next-game');
    if (slot) {
      slot.innerHTML = next ? ticket(next) : '';
      slot.closest('[data-if-next]').hidden = !next;
    }
    const results = $('#results');
    if (results) {
      results.innerHTML = `
        <ol class="rows">${[...S.games, ...pending].map(resultRow).join('')}</ol>
        <p class="fine">${esc(S.scoreNote)}${pending.length ? ' “Final pending” means the game has kicked off and its score isn’t in this demo yet.' : ''}</p>`;
    }
    const sched = $('#sched');
    if (sched) {
      sched.innerHTML = `
        ${rest.length ? `<ol class="rows">${rest.map(schedRow).join('')}</ol>` : ''}
        <p class="fine">${rest.length ? `Kickoff times are Central (${TZ}). ` : 'No games left to list. '}Schedule from ${esc(S.source)}, as of ${fmtDate(S.scheduleAsOf)}. Later games can be moved by the league.</p>`;
    }
    tick();
  }

  // Runs every second: counts down, and when the kickoff passes repaints so the next game takes over.
  function tick() {
    const el = $('[data-countdown]');
    if (!el) return;
    const left = Number(el.dataset.countdown) - Date.now();
    if (left <= 0) return paintSeason();
    const s = Math.floor(left / 1000);
    const parts = [Math.floor(s / 86400), Math.floor((s % 86400) / 3600), Math.floor((s % 3600) / 60), s % 60];
    $$('b', el).forEach((b, i) => { b.textContent = String(parts[i]).padStart(2, '0'); });
  }

  // Blocks that appear on more than one page. A page asks for one with <div data-slot="roles">.
  const SLOTS = {
    roles: () => `<div class="roles">${D.show.roles.map((r) => `
      <article class="panel" data-reveal><h3>${esc(r.title)}</h3><p>${esc(r.text)}</p></article>`).join('')}</div>`,
    featured: () => `
      <ul class="feat">${D.show.featuredBy.map((n) => `<li>${esc(n)}</li>`).join('')}</ul>
      <p class="fine">Outlets as listed in his bio on <a href="${D.show.website}" ${EXT}>scootermagruder.com</a>.</p>`,
    channels: () => `<div class="channels">${D.otherChannels.map((c) => `
      <a class="panel link" href="${esc(c.url)}" ${EXT} data-reveal>
        <h3>${esc(c.name)}</h3><p>${esc(c.text)}</p><span class="go">Visit the channel</span>
      </a>`).join('')}</div>`,
    mail: () => `<div class="mails">${D.contact.inboxes.map((m) => `
      <article class="panel mail" data-reveal>
        <h3>${esc(m.label)}</h3>
        <a class="mail-addr" href="mailto:${esc(m.email)}">${esc(m.email)}</a>
      </article>`).join('')}</div>
      <p class="fine">${esc(D.contact.labelsSource)}</p>`,
    record: () => `<b class="nb">${esc(S.record)}</b><span>${S.year} ${esc(D.team.name)} record, through Week ${lastScored}</span>`,
  };

  /* Scoreboard plate: the channel's public subscriber count, re-read from YouTube while the page is open. */
  function subsPlate(el) {
    let shown;
    const paint = (text, live) => {
      const html = `<b>${esc(text)}</b><span>YouTube subscribers</span><small>${live ? '<i></i>Live count' : `Count ${asOf}`}</small>`;
      if (html !== shown) el.innerHTML = shown = html; // repaint only on change
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
      <div class="btn-row"><button type="button" class="btn navy">Next one</button><span class="cp-n nb">1 of ${list.length}</span></div>
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
  const NAV = [['cowboys.html', 'Season', 'cowboys'], ['videos.html', 'Videos', 'videos'], ['about.html', 'About', 'about'],
    ['press.html', 'Press', 'press'], ['merch.html', 'Merch', 'merch'], ['socials.html', 'Socials', 'socials'],
    ['contact.html', 'Contact', 'contact'], ['partners.html', 'Work with Scooter', 'partners']];
  const current = (key) => (key === page ? ' aria-current="page"' : '');

  function chrome() {
    const [first, last] = D.show.name.split(' ');
    const head = $('#site-head');
    head.innerHTML = `
      <div class="wrap head-in">
        <a class="brand" href="index.html" aria-label="${esc(D.show.name)} home">${esc(first)} <span>${esc(last)}</span></a>
        <button type="button" class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
        <nav class="nav" id="nav" aria-label="Main">
          ${NAV.map(([href, label, key]) => `<a class="nav-${key}" href="${href}"${current(key)}>${label}</a>`).join('')}
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
            <p class="fine">${esc(D.team.note)}</p>
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
          <p>Independent creator site. Not affiliated with the NFL, the Dallas Cowboys, any team, or the outlets named.</p>
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
        <div class="player-bar"><h2 id="player-title"></h2><button type="button" class="btn sm ghost">Close</button></div>
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
          <p class="kicker">Demo form</p>
          <p class="name">You’re in${name ? `, ${esc(name)}` : ''}.</p>
          <p>This is a demo, so nothing was sent and nothing was saved. On the live site, ${esc(email.value.trim())} would get updates for: ${esc(wants)}.</p>`;
        form.replaceWith(done);
        done.focus();
      });
    });
  }

  /* ---------- pages ---------- */
  // The big playable frame for one video, with its title beside it.
  const feature = (v, label) => `
    <button type="button" class="frame" data-video="${v.id}" aria-label="Play: ${esc(v.title)}">
      ${media(`https://i.ytimg.com/vi/${v.id}/maxresdefault.jpg`, '', 1280, 720, 'r16',
        `<span class="play"></span><span class="dur">${fmtDur(v.seconds)}</span>`, `data-fallback="${v.thumb}" loading="lazy"`)}
    </button>
    <div>
      <p class="kicker">${label}</p>
      <h3 class="feature-title">${esc(v.title)}</h3>
      <p class="meta">${fmtDate(v.date)} · ${compact(v.views)} views · ${fmtDur(v.seconds)}</p>
      <div class="btn-row">
        <button type="button" class="btn" data-video="${v.id}">Play it here</button>
        <a class="btn ghost" href="videos.html?series=${encodeURIComponent(v.series)}">All ${esc(v.series)} videos</a>
      </div>
    </div>`;

  const pages = {
    home() {
      const s = D.show, lead = inSeries(LEAD);
      $('#hero-hash').innerHTML = s.hashtags.map((h) => `<li class="tag">${esc(h)}</li>`).join('');
      $('#hero-art').innerHTML = `${media(s.hostPhoto, s.name, 754, 754, 'r11 hero-photo', '', 'fetchpriority="high"')}<div class="subs" id="subs"></div>`;
      subsPlate($('#subs'));
      $('#h-lead').textContent = LEAD;
      $('#lead-count').textContent = `${lead.length} of the latest ${D.videos.length} uploads. They play right on this page.`;
      $('#home-feature').innerHTML = feature(lead[0], 'Newest in the series');
      $('#home-lead').innerHTML = lead.slice(1, 5).map(videoCard).join('');
      $('#home-series').innerHTML = SERIES.map((name) => {
        const list = inSeries(name);
        return `
        <a class="tile" href="videos.html?series=${encodeURIComponent(name)}" data-reveal>
          ${media(list[0].thumb, '', 480, 270, 'r16')}
          <span class="tile-name">${esc(name)}</span>
          <span class="meta">${list.length} of the latest ${D.videos.length}</span>
          <span class="tile-new">Newest: ${esc(list[0].title)}</span>
        </a>`;
      }).join('');
      catchphrases($('#home-cp'));
      $('#home-merch').innerHTML = D.merch.products.slice(0, 4).map(productCard).join('');
    },

    cowboys() {
      const list = D.videos.filter((v) => v.title.includes(D.team.short));
      $('#cb-count').textContent = `${list.length} of the latest ${D.videos.length} uploads have “${D.team.short}” in the title.`;
      $('#cb-videos').innerHTML = list.map(videoCard).join('');
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
          <p class="kicker">${esc(s.realName)}</p>
          <blockquote class="quote">“${esc(s.intro)}”</blockquote>
          <p class="fine">In his words, from <a href="${s.website}" ${EXT}>scootermagruder.com</a>. On YouTube since ${esc(s.joined)}.</p>
          <div class="btn-row"><a class="btn" href="${s.subscribeUrl}" ${EXT}>Subscribe on YouTube</a><a class="btn ghost" href="videos.html">Watch videos</a></div>
        </div>`;
      $('#about-photos').innerHTML = s.photos.map((p) => `
        <figure data-reveal>${media(p.src, '', 768, 1024, 'r34')}<figcaption>${esc(p.alt)}</figcaption></figure>`).join('');
    },

    press() {
      $('#press-list').innerHTML = D.press.map((p) => `
        <li data-reveal><a href="${esc(p.url)}" ${EXT}>
          <span class="press-outlet">${esc(p.outlet)}</span>
          <span class="press-title">${esc(p.title)}</span>
          <span class="go">Read it</span>
        </a></li>`).join('');
    },

    partners() {
      const s = D.show;
      const avg = D.videos.reduce((sum, v) => sum + v.views, 0) / D.videos.length;
      const stat = (text, label, count, fmt) =>
        `<div class="stat" data-reveal><b data-count="${count}" data-fmt="${fmt}">${text}</b><span>${label}</span></div>`;
      $('#pt-stats').innerHTML = `
        <div class="stats">
          ${stat(esc(s.subscribers), 'YouTube subscribers', s.subscribersNum, 'compact')}
          ${stat(compact(s.totalViews), 'Total YouTube views', s.totalViews, 'compact')}
          ${stat(int(s.videoCount), 'Videos published', s.videoCount, 'int')}
          ${stat(compact(avg), `Average views per video, computed from the ${D.videos.length} latest uploads`, Math.round(avg), 'compact')}
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
      $('#soc-grid').innerHTML = D.socials.map((s) => `
        <a class="social" href="${esc(s.url)}" ${EXT} data-reveal>
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
    // Opacity, never autoAlpha: visibility:hidden would take unrevealed links and buttons out of the Tab order.
    gsap.from('.hero-h1 span', { xPercent: -12, opacity: 0, duration: 0.7, ease: 'power3.out', stagger: 0.1 });
    gsap.from('.hero-photo', { scale: 1.06, opacity: 0, duration: 0.9, ease: 'power3.out', delay: 0.1 });
    // transition:none so the cards' CSS hover transition doesn't fight the tween; clearProps hands them back after.
    gsap.set('[data-reveal]', { opacity: 0, y: 22, transition: 'none' });
    ScrollTrigger.batch('[data-reveal]', {
      start: 'top 94%', once: true,
      onEnter: (els) => gsap.to(els, { opacity: 1, y: 0, duration: 0.55, ease: 'power3.out', stagger: 0.06, clearProps: 'all' }),
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
  paintSeason();
  setInterval(tick, 1000);
  motion();
})();
