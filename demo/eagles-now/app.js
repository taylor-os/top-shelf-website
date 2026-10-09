/* Eagles Now demo. Every page renders from data.js (window.EN); no facts live in this file. */
(() => {
  'use strict';
  const D = window.EN;
  if (!D) return;

  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const page = document.body.dataset.page;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const EXT = 'target="_blank" rel="noopener"';
  let lenis = null;

  /* ---------- helpers ---------- */
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const noon = (iso) => new Date(iso + 'T12:00:00');
  const fmtDate = (iso) => noon(iso).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
  const fmtDay = (iso) => noon(iso).toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' });
  const ttl = (t) => esc(t).replace(/\d+-\d+/g, '<span class="nb">$&</span>'); // scores never split across lines
  const fmtDur = (s) => {
    const h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), sec = String(s % 60).padStart(2, '0');
    return h ? `${h}:${String(m).padStart(2, '0')}:${sec}` : `${m}:${sec}`;
  };
  const compact = (n) => new Intl.NumberFormat('en-US', { notation: 'compact', maximumFractionDigits: 1 }).format(n);
  const int = (n) => Math.round(n).toLocaleString('en-US');
  const asOf = `as of ${fmtDate(D.show.statsAsOf)}`;
  const plain = (t) => t.toLowerCase().replace(/[‘’]/g, "'");
  const matches = (text, q) => plain(text).includes(plain(q.trim()));
  // Breaking leads the desk order; any type that shows up in data later still gets a chip.
  const TYPES = [...new Set(['Breaking', 'Rumors', 'Reaction', 'Preview', 'News', ...D.videos.map((v) => v.type)])]
    .filter((t) => D.videos.some((v) => v.type === t));
  const LINKS = { subscribe: D.show.subscribeUrl, store: D.merch.storeUrl, chatsports: D.articles.sourceUrl };

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
  const badge = (type) => `<span class="badge" data-type="${esc(type)}">${esc(type)}</span>`;

  const row = (v) => `
    <li><button type="button" class="row" data-video="${v.id}" data-type="${esc(v.type)}" data-reveal>
      ${media(v.thumb, '', 480, 360, 'r16', `<span class="dur">${fmtDur(v.seconds)}</span>`)}
      <span class="row-body">
        <span class="row-top">${badge(v.type)}<span class="meta">${fmtDate(v.date)} · ${compact(v.views)} views</span></span>
        <span class="row-title">${ttl(v.title)}</span>
      </span>
    </button></li>`;

  // Video rows in the order given, with a date line each time the day changes when grouped.
  const feed = (list, grouped) => {
    let last = '';
    return list.map((v) => {
      const head = grouped && v.date !== last ? `<li class="day">${fmtDay(v.date)}</li>` : '';
      last = v.date;
      return head + row(v);
    }).join('');
  };

  const productCard = (p) => `
    <article class="product" data-reveal>
      ${media(p.image, p.name, 600, 600, 'r11')}
      <div class="product-body">
        <h3 class="product-name">${esc(p.name)}</h3>
        <p class="price">$${esc(p.price)}</p>
        <a class="btn sm" href="${esc(p.url)}" ${EXT}>View in shop<span class="sr-only">: ${esc(p.name)}</span></a>
      </div>
    </article>`;

  const sponsorCard = (s) => `
    <article class="sponsor" data-reveal>
      <p class="kicker">Channel sponsor</p>
      <h3 class="sponsor-name">${esc(s.name)}</h3>
      ${s.code ? `<div class="code"><span class="meta">Code</span><code>${esc(s.code)}</code><button type="button" class="btn sm" data-copy="${esc(s.code)}">Copy<span class="sr-only"> ${esc(s.name)} code</span></button></div>` : ''}
      <a class="btn ghost" href="${esc(s.url)}" ${EXT}>Go to ${esc(s.name)}</a>
      <p class="fine">The link and code are the ones the channel shares. Terms are set by ${esc(s.name)}.</p>
    </article>`;

  const stat = (text, label, count, fmt) =>
    `<div class="stat" data-reveal><b ${count ? `data-count="${count}" data-fmt="${fmt}"` : ''}>${text}</b><span class="meta">${label}</span></div>`;

  const versus = (g) => `${g.home ? 'vs.' : 'at'} ${esc(g.opp)}`;
  const place = (g) => `<span><span class="srow-opp">${versus(g)}</span><span class="srow-site">@ ${esc(g.site)}</span></span>`;

  const schedRow = (g) => (g.bye
    ? `<li class="srow bye"><span class="wk">Wk ${g.week}</span><span class="srow-opp">Bye week</span></li>`
    : `<li class="srow">
        <span class="wk">Wk ${g.week}</span>
        ${place(g)}
        <span class="srow-when">${g.date ? `${fmtDay(g.date)} · ${esc(g.time)} ET · ${esc(g.tv)}` : 'Date and time TBD'}</span>
      </li>`);

  const resultRow = (g) => `
    <li class="grow" data-reveal>
      <span class="wk">Wk ${g.week}</span>
      ${place(g)}
      ${g.result ? `<span class="score nb">${esc(g.score)}</span>` : '<span class="meta pending">Final pending</span>'}
      ${g.result
        ? `<span class="wl ${g.result}">${g.result}<span class="sr-only">${g.result === 'W' ? ' win' : ' loss'}</span></span>`
        : '<span class="wl"></span>'}
    </li>`;

  /* ---------- season: one ordered list of games, and the clock decides where each one shows ---------- */
  const GAMES = [D.season.next, ...D.season.schedule];
  const scored = new Set(D.season.games.map((g) => g.week));
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

  const bug = (n) => {
    const k = new Date(n.kickoff);
    const when = { weekday: 'short', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' };
    return `
    <div class="bug" data-reveal>
      <div>
        <p class="kicker">Next game · Week ${n.week}</p>
        <p class="bug-opp">Eagles ${versus(n)}</p>
        <p class="srow-site">@ ${esc(n.site)}</p>
        <p class="srow-when">${k.toLocaleString('en-US', { ...when, timeZone: 'America/New_York' })} ET · ${esc(n.tv)}</p>
        <p class="fine">${esc(k.toLocaleString(undefined, { ...when, timeZoneName: 'short' }))}, your time</p>
      </div>
      <div class="cd" data-countdown="${k.getTime()}" role="timer" aria-label="Countdown to kickoff">
        ${['days', 'hrs', 'min', 'sec'].map((u) => `<span><b>--</b><i>${u}</i></span>`).join('')}
      </div>
    </div>`;
  };

  // Paints the next-game block, the remaining schedule and (on the News page) the results tracker.
  function paintSeason() {
    const { next, rest, pending } = seasonState(Date.now());
    const slot = $('#home-next, #news-next');
    if (slot) {
      slot.innerHTML = `${next ? bug(next) : ''}
        <div class="sched" data-reveal>
          ${rest.length ? `<p class="kicker">Still to play</p><ol class="sched-list">${rest.map(schedRow).join('')}</ol>` : ''}
          <p class="fine">${next || rest.length ? 'Kickoff times are Eastern. ' : 'No games left to list. '}Schedule as of ${fmtDate(D.season.scheduleAsOf)}.</p>
        </div>`;
    }
    const results = $('#news-games');
    if (results) results.innerHTML = [...D.season.games, ...pending].map(resultRow).join('');
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

  // The channel's public subscriber count as a wire readout: the figure types in, a rule tracks the run
  // to the next round number (our math from the count), and the status line says how fresh the number is.
  function subsLive(el) {
    el.innerHTML = `
      <p class="subs-slug"><span class="subs-tag"></span><span class="meta">YouTube subscribers</span></p>
      <p class="subs-num"><span aria-hidden="true"></span><span class="sr-only"></span></p>
      <div class="subs-rule" aria-hidden="true"><i></i></div>
      <p class="subs-scale meta"><span></span><span></span></p>
      <p class="fine"></p>`;
    const tag = $('.subs-tag', el), num = $('.subs-num', el), [shown, spoken] = num.children;
    const bar = $('.subs-rule i', el), [from, to] = $('.subs-scale', el).children, stamp = $('.fine', el);
    let timer;

    // checked: when subs.php read the number from YouTube. Left out for the dated number from data.js.
    const paint = (text, count, checked) => {
      tag.textContent = checked ? 'Live' : asOf;
      tag.classList.toggle('on', Boolean(checked));
      stamp.textContent = checked
        ? `Checked on YouTube at ${checked.toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' })}, your time.`
        : 'Dated figure from the channel’s YouTube page.';
      const step = 10 ** Math.floor(Math.log10(count)) / 10, base = Math.floor(count / step) * step;
      from.textContent = compact(base);
      to.textContent = `Next: ${compact(base + step)}`;
      void bar.offsetWidth; // so the first paint animates from empty
      bar.style.transform = `scaleX(${(count - base) / step})`;

      const label = `${text} subscribers`;
      if (spoken.textContent === label) return; // already on screen: don't retype it
      spoken.textContent = label;
      clearInterval(timer);
      if (reduced) { shown.textContent = text; return; }
      let i = 0;
      num.classList.add('typing');
      timer = setInterval(() => {
        shown.textContent = text.slice(0, ++i);
        if (i >= text.length) { clearInterval(timer); num.classList.remove('typing'); }
      }, 110);
    };
    const dated = () => paint(D.show.subscribers, D.show.subscribersNum);
    dated();

    const pull = async () => {
      try {
        const j = await (await fetch('subs.php', { cache: 'no-store' })).json();
        const at = new Date(j.fetchedAt);
        // Live only when YouTube was read in the last 30 minutes; subs.php can hand back an older cached count.
        if (j.count && Date.now() - at < 30 * 60 * 1000) return paint(String(j.text), j.count, at);
      } catch { /* no PHP here (local preview) or YouTube unreachable */ }
      dated();
    };
    pull();
    setInterval(pull, 5 * 60 * 1000);
  }

  // Type filter chips with a count each: one pressed at a time, calls onPick(type) on change.
  function typeChips(el, active, onPick) {
    const count = (t) => D.videos.filter((v) => v.type === t).length;
    el.innerHTML = [['All', D.videos.length], ...TYPES.map((t) => [t, count(t)])].map(([t, n]) =>
      `<button type="button" class="chip" data-type="${esc(t)}" aria-pressed="${t === active}">${esc(t)}<span class="n">${n}</span></button>`).join('');
    el.addEventListener('click', (e) => {
      const b = e.target.closest('.chip');
      if (!b) return;
      $$('.chip', el).forEach((c) => c.setAttribute('aria-pressed', String(c === b)));
      onPick(b.dataset.type);
    });
  }
  const ofType = (type) => D.videos.filter((v) => type === 'All' || v.type === type);

  /* ---------- chrome ---------- */
  const NAV = [['index.html', 'Home', 'home'], ['videos.html', 'Videos', 'videos'], ['news.html', 'News', 'news'],
    ['articles.html', 'Articles', 'articles'], ['merch.html', 'Merch', 'merch'], ['sponsors.html', 'Sponsors', 'sponsors'],
    ['socials.html', 'Socials', 'socials'], ['about.html', 'About', 'about']];
  const current = (key) => (key === page ? ' aria-current="page"' : '');
  const brand = `<img src="${D.show.avatar}" alt="" width="36" height="36"><span class="brand-name">${esc(D.show.name)}<small>by ${esc(D.show.network)}</small></span>`;

  function chrome() {
    const head = $('#site-head');
    head.innerHTML = `
      <div class="wrap head-in">
        <a class="brand" href="index.html" aria-label="${esc(D.show.fullName)} home">${brand}</a>
        <button type="button" class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
        <nav class="nav" id="nav" aria-label="Main" data-lenis-prevent>
          ${NAV.map(([href, label, key]) => `<a href="${href}"${current(key)}>${label}</a>`).join('')}
          <a class="btn sm" href="subscribe.html"${current('subscribe')}>Get alerts</a>
        </nav>
      </div>`;
    const btn = $('.menu-btn', head);
    const setOpen = (open) => { head.classList.toggle('open', open); btn.setAttribute('aria-expanded', String(open)); };
    btn.addEventListener('click', () => setOpen(!head.classList.contains('open')));
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && head.classList.contains('open')) { setOpen(false); btn.focus(); }
    });

    // Headline ticker. The second set is a visual repeat for the loop: hidden from assistive tech and the tab order.
    const items = D.videos.slice(0, 8).map((v) => `<button type="button" class="tick" data-video="${v.id}">${badge(v.type)}<span>${esc(v.title)}</span></button>`).join('');
    head.insertAdjacentHTML('afterend', `
      <div class="ticker" role="region" aria-label="Latest video headlines">
        <span class="ticker-tag">The wire</span>
        <div class="ticker-view"><div class="ticker-track">
          <div class="ticker-set">${items}</div>
          <div class="ticker-set" aria-hidden="true">${items.replaceAll('<button ', '<button tabindex="-1" ')}</div>
        </div></div>
        <button type="button" class="ticker-pause" aria-pressed="false">Pause</button>
      </div>`);
    $('.ticker-pause').addEventListener('click', (e) => {
      const paused = e.target.closest('.ticker').classList.toggle('paused');
      e.target.setAttribute('aria-pressed', String(paused));
      e.target.textContent = paused ? 'Play' : 'Pause';
    });

    $('#site-foot').innerHTML = `
      <div class="wrap">
        <div class="foot-grid">
          <div class="foot-brand">
            <a class="brand" href="index.html" aria-label="${esc(D.show.fullName)} home">${brand}</a>
            <p class="foot-desks">${TYPES.map((t) => `<a class="chip" data-type="${esc(t)}" href="videos.html?type=${encodeURIComponent(t)}">${esc(t)}</a>`).join('')}</p>
          </div>
          <div>
            <p class="foot-h">Sections</p>
            <ul>${NAV.map(([href, label]) => `<li><a href="${href}">${label}</a></li>`).join('')}<li><a href="subscribe.html">Get alerts</a></li></ul>
          </div>
          <div>
            <p class="foot-h">Follow</p>
            <ul>${D.socials.map((s) => `<li><a href="${esc(s.url)}" ${EXT}>${esc(s.name)}</a></li>`).join('')}</ul>
          </div>
        </div>
        <div class="foot-legal fine">
          <p>${esc(D.show.disclaimer)}</p>
          <p>Concept demo by Top Shelf Business Solutions. Videos, headlines, merch and channel numbers come from the channel’s public pages and the Chat Sports sites it links to.</p>
        </div>
      </div>`;

    // Static anchors that point at a URL from data.js.
    $$('[data-link]').forEach((a) => { a.href = LINKS[a.dataset.link]; });
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
      $('.player-meta', dlg).innerHTML = `<span>${esc(v.type)} · ${fmtDate(v.date)} · ${int(v.views)} views · ${fmtDur(v.seconds)}</span><a href="${esc(v.url)}" ${EXT}>Watch on YouTube</a>`;
      lenis?.stop();
      dlg.showModal();
    });
  }

  /* ---------- sponsor code: copy, or select it when the clipboard is off limits ---------- */
  document.addEventListener('click', async (e) => {
    const b = e.target.closest('[data-copy]');
    if (!b) return;
    const label = b.firstChild; // the visible "Copy" text node
    try {
      await navigator.clipboard.writeText(b.dataset.copy);
      label.textContent = 'Copied';
    } catch {
      getSelection().selectAllChildren($('code', b.closest('.code'))); // so Ctrl/Cmd+C works
      label.textContent = 'Selected';
    }
    setTimeout(() => { label.textContent = 'Copy'; }, 1800);
  });

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
        if (!emailOk) { err.textContent = 'That email doesn’t look right. Check it and try again.'; return email.focus(); }
        if (boxes.length && !picked.length) { err.textContent = 'Pick at least one kind of alert.'; return boxes[0].focus(); }
        const name = form.elements.firstName?.value.trim();
        const wants = picked.length ? new Intl.ListFormat('en').format(picked) : 'every alert';
        const done = document.createElement('div');
        done.className = 'success';
        done.setAttribute('role', 'status');
        done.tabIndex = -1;
        done.innerHTML = `
          <p class="kicker">Demo form</p>
          <p class="name">You’re on the list${name ? `, ${esc(name)}` : ''}.</p>
          <p>This is a demo, so nothing was sent and nothing was saved. On the live site, <span class="addr">${esc(email.value.trim())}</span> would get ${esc(wants)}.</p>`;
        form.replaceWith(done);
        done.focus();
      });
    });
  }

  /* ---------- pages ---------- */
  const pages = {
    home() {
      const s = D.show, v = D.videos[0];
      $('#mast-kicker').textContent = `${s.fullName} · Hosted by ${s.host}`;
      $('#home-lead').innerHTML = `
        <button type="button" class="lead-media" data-video="${v.id}" aria-label="Play: ${esc(v.title)}">
          ${media(`https://i.ytimg.com/vi/${v.id}/maxresdefault.jpg`, '', 1280, 720, 'r16',
            `<span class="play"></span><span class="dur">${fmtDur(v.seconds)}</span>`,
            `data-fallback="${v.thumb}" fetchpriority="high"`)}
        </button>
        <div class="lead-body">
          <p class="row-top">${badge(v.type)}<span class="meta">Latest upload · ${fmtDate(v.date)} · ${compact(v.views)} views</span></p>
          <h2 class="lead-title">${ttl(v.title)}</h2>
          <div class="btn-row">
            <button type="button" class="btn" data-video="${v.id}">Watch now</button>
            <a class="btn ghost" href="videos.html">All videos</a>
          </div>
        </div>`;
      $('#home-desk').innerHTML = `
        <div class="subs" id="subs"></div>
        <dl class="facts">
          <div><dt>Total views</dt><dd>${int(s.totalViews)}</dd></div>
          <div><dt>Videos</dt><dd>${int(s.videoCount)}</dd></div>
          <div><dt>On YouTube since</dt><dd>${esc(s.joined)}</dd></div>
          <div><dt>Host</dt><dd>${esc(s.host)}</dd></div>
          <div><dt>${D.season.year} Eagles record, through Week ${lastScored}</dt><dd><span class="nb">${esc(D.season.record)}</span></dd></div>
        </dl>
        <p class="fine">Channel and view numbers ${asOf}.</p>
        <div class="btn-row">
          <a class="btn" href="${s.subscribeUrl}" ${EXT}>Subscribe on YouTube</a>
          <a class="btn ghost" href="${s.membershipUrl}" ${EXT}>Become a member</a>
        </div>`;
      subsLive($('#subs'));

      const SHOW = 8;
      const render = (type) => {
        const list = ofType(type);
        $('#home-feed').innerHTML = feed(list.slice(0, SHOW), true);
        $('#home-feed-more').innerHTML = `Showing ${Math.min(SHOW, list.length)} of ${list.length}. <a href="videos.html${type === 'All' ? '' : `?type=${encodeURIComponent(type)}`}">Open the full video desk</a>`;
      };
      typeChips($('#home-chips'), 'All', render);
      render('All');

      $('#home-read').innerHTML = D.articles.items.slice(0, 6).map((a) => `<li><a href="${esc(a.url)}" ${EXT}>${ttl(a.title)}</a></li>`).join('');
      $('#home-sponsor').innerHTML = D.sponsors.map(sponsorCard).join('');
      $('#home-merch').innerHTML = D.merch.products.slice(0, 4).map(productCard).join('');
    },

    videos() {
      const out = $('#vid-feed'), q = $('#vid-q'), sort = $('#vid-sort'), count = $('#vid-count');
      const wanted = new URLSearchParams(location.search).get('type');
      let type = TYPES.includes(wanted) ? wanted : 'All';
      const render = () => {
        const list = ofType(type).filter((v) => matches(v.title, q.value))
          .sort((a, b) => (sort.value === 'views' ? b.views - a.views : b.date.localeCompare(a.date)));
        count.textContent = `${list.length} of the ${D.videos.length} latest uploads`;
        out.innerHTML = feed(list, false) || '<li class="empty">No videos match that. Try a shorter search or another type.</li>';
      };
      typeChips($('#vid-chips'), type, (t) => { type = t; render(); });
      q.addEventListener('input', render);
      sort.addEventListener('change', render);
      render();
    },

    news() {
      const s = D.season;
      $('#news-year').textContent = `${s.year} season`;
      $('#news-record').textContent = s.record;
      $('#news-record-label').textContent = `Record through Week ${lastScored}`;
      $('#news-feed').innerHTML = feed(D.videos.filter((v) => v.type === 'Preview' || v.type === 'Reaction'), false);
    },

    articles() {
      const q = $('#art-q'), out = $('#art-list'), count = $('#art-count'), items = D.articles.items;
      const render = () => {
        const list = items.filter((a) => matches(a.title, q.value));
        count.textContent = `${list.length} of ${items.length} headlines`;
        out.innerHTML = list.map((a) => `
          <li><a class="art" href="${esc(a.url)}" ${EXT}>
            <span class="art-title">${ttl(a.title)}</span>
            <span class="art-go">Read on ${esc(D.articles.sourceName)}</span>
          </a></li>`).join('') || '<li class="empty">No headline matches that. Try a player’s last name.</li>';
      };
      q.addEventListener('input', render);
      render();
    },

    merch() {
      $('#merch-count').textContent = `${D.merch.products.length} items on ${D.merch.storeName}`;
      $('#merch-grid').innerHTML = D.merch.products.map(productCard).join('');
    },

    sponsors() {
      const s = D.show;
      $('#sp-grid').innerHTML = D.sponsors.map(sponsorCard).join('');
      const avg = D.videos.reduce((sum, v) => sum + v.views, 0) / D.videos.length;
      $('#sp-stats').innerHTML = `
        ${stat(esc(s.subscribers), 'YouTube subscribers', s.subscribersNum, 'compact')}
        ${stat(compact(s.totalViews), 'Total views', s.totalViews, 'compact')}
        ${stat(int(s.videoCount), 'Videos published', s.videoCount, 'int')}
        ${stat(compact(avg), `Average views on the ${D.videos.length} latest uploads (our math)`, Math.round(avg), 'compact')}`;
      $('#sp-asof').textContent = `Channel and view numbers ${asOf}.`;
    },

    socials() {
      $('#soc-grid').innerHTML = D.socials.map((s) => `
        <a class="social" href="${esc(s.url)}" ${EXT} data-reveal>
          <span class="social-name">${esc(s.name)}</span>
          <span class="social-handle">${esc(s.handle)}</span>
          ${s.stat ? `<span class="meta">${esc(s.stat)} ${asOf}</span>` : ''}
          <span class="go">Open ${esc(s.name)}</span>
        </a>`).join('');
      const o = D.host.otherShow;
      $('#soc-other').innerHTML = `
        <div>
          <p class="kicker">Also from ${esc(D.host.name)}</p>
          <h2>${esc(o.name)}</h2>
          <p>${esc(o.note)}</p>
        </div>
        <a class="btn light" href="${esc(o.url)}" ${EXT}>Watch ${esc(o.name)}</a>`;
    },

    about() {
      const s = D.show, h = D.host;
      $('#about-show').innerHTML = `
        <blockquote class="quote">${esc(s.about)}</blockquote>
        <p class="fine">From the channel’s own description.</p>
        <p class="lede">In the channel’s words: “${esc(s.networkLine)}”</p>
        <dl class="facts">
          <div><dt>On YouTube since</dt><dd>${esc(s.joined)}</dd></div>
          <div><dt>Subscribers</dt><dd>${esc(s.subscribers)}</dd></div>
          <div><dt>Videos</dt><dd>${int(s.videoCount)}</dd></div>
          <div><dt>Total views</dt><dd>${int(s.totalViews)}</dd></div>
        </dl>
        <p class="fine">Numbers ${asOf}.</p>`;
      $('#about-host').innerHTML = `
        <div class="monogram" aria-hidden="true">${h.name.split(' ').map((n) => n[0]).join('')}</div>
        <div>
          <p class="kicker">${esc(h.role)}</p>
          <h2>${esc(h.name)}</h2>
          <p class="links">${[['Instagram', h.instagram], ['TikTok', h.tiktok], ['X', h.x], ['Facebook', h.facebook]]
            .map(([n, url]) => `<a href="${esc(url)}" ${EXT}>${n}</a>`).join('')}</p>
          <p class="other">${esc(h.otherShow.note)}: <a href="${esc(h.otherShow.url)}" ${EXT}>${esc(h.otherShow.name)}</a></p>
          <div class="btn-row"><a class="btn" href="${s.subscribeUrl}" ${EXT}>Subscribe on YouTube</a><a class="btn ghost" href="videos.html">Watch the latest</a></div>
        </div>`;
      $('#about-fine').textContent = s.disclaimer;
    },
  };

  /* ---------- motion: enhancement only. Content is visible by default; nothing below runs without GSAP. ---------- */
  function motion() {
    if (reduced || !window.gsap || !window.ScrollTrigger) return;
    const { gsap, ScrollTrigger } = window;
    gsap.registerPlugin(ScrollTrigger);
    gsap.config({ nullTargetWarn: false }); // not every page has a lead story or reveal targets
    if (window.Lenis) {
      lenis = new window.Lenis({ lerp: 0.1 });
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add((t) => lenis.raf(t * 1000));
      gsap.ticker.lagSmoothing(0);
    }
    // The lead story wipes in like a feed coming up; everything else files in behind it.
    gsap.fromTo('.lead-media', { clipPath: 'inset(0 100% 0 0)' }, { clipPath: 'inset(0 0% 0 0)', duration: 0.9, ease: 'power3.out', clearProps: 'clipPath' });
    // transition:none so the rows' CSS hover transition doesn't fight the tween; clearProps hands them back after.
    // Opacity only, never visibility: rows below the fold must stay in the tab order before they are scrolled to.
    gsap.set('[data-reveal]', { opacity: 0, x: -14, transition: 'none' });
    ScrollTrigger.batch('[data-reveal]', {
      start: 'top 96%', once: true,
      onEnter: (els) => gsap.to(els, { opacity: 1, x: 0, duration: 0.5, ease: 'power3.out', stagger: 0.05, clearProps: 'all' }),
    });
    $$('[data-count]').forEach((el) => {
      const end = Number(el.dataset.count), final = el.textContent, fmt = el.dataset.fmt === 'int' ? int : compact;
      const n = { v: 0 };
      gsap.to(n, {
        v: end, duration: 1.4, ease: 'power2.out', scrollTrigger: { trigger: el, start: 'top 94%', once: true },
        onUpdate: () => { el.textContent = fmt(n.v); },
        onComplete: () => { el.textContent = final; },
      });
    });
  }

  chrome();
  player();
  pages[page]?.();
  forms();
  paintSeason();
  setInterval(tick, 1000);
  motion();
})();
