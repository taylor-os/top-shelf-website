/* The Thomas Mott Show demo. Every page renders from data.js (window.TMS); no facts live in this file. */
(() => {
  'use strict';
  const D = window.TMS;
  if (!D) return;

  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const page = document.body.dataset.page;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const EXT = 'target="_blank" rel="noopener"';
  let lenis = null;

  /* ---------- helpers ---------- */
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const day = (iso, opts) => new Date(iso + 'T12:00:00').toLocaleDateString('en-US', opts);
  const fmtDate = (iso) => day(iso, { month: 'short', day: 'numeric', year: 'numeric' });
  const fmtDay = (iso) => day(iso, { weekday: 'short', month: 'short', day: 'numeric' });
  const fmtDur = (s) => `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;
  const compact = (n) => new Intl.NumberFormat('en-US', { notation: 'compact', maximumFractionDigits: 1 }).format(n);
  const int = (n) => Math.round(n).toLocaleString('en-US');
  const asOf = `as of ${fmtDate(D.show.statsAsOf)}`;
  const plain = (t) => t.toLowerCase().replace(/[‘’]/g, "'");
  const mailto = (addr, subject) => `mailto:${addr}${subject ? `?subject=${encodeURIComponent(subject)}` : ''}`;

  const media = (src, alt, w, h, cls, inner = '', attrs = 'loading="lazy"') =>
    `<span class="media ${cls}"><img src="${esc(src)}" alt="${esc(alt)}" width="${w}" height="${h}" decoding="async" referrerpolicy="no-referrer" ${attrs}>${inner}</span>`;

  // Hotlinked images: fall back once if a data-fallback is set, otherwise hide and let the tinted box show.
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
  const story = (v) => `
    <li><button type="button" class="story" data-video="${v.id}" data-reveal>
      ${media(v.thumb, '', 480, 360, 'r16', `<span class="dur">${fmtDur(v.seconds)}</span>`)}
      <span class="story-body">
        <span class="meta">${fmtDate(v.date)} · ${compact(v.views)} views</span>
        <span class="story-title">${esc(v.title)}</span>
      </span>
    </button></li>`;

  const stat = (text, label) => `<div class="stat" data-reveal><b>${text}</b><span class="meta">${label}</span></div>`;

  const schedRow = (g) => (g.bye
    ? `<li class="srow"><span class="srow-wk">Week ${g.week}</span><span class="srow-opp">Bye week</span></li>`
    : `<li class="srow">
        <span class="srow-wk">Week ${g.week}</span>
        <span class="srow-opp">${g.home ? 'vs.' : 'at'} ${esc(g.opp)}</span>
        <span class="srow-when">${g.date ? `${fmtDay(g.date)} · ${g.time} ET · ${esc(g.tv)}` : 'Date and time TBD'}</span>
        <span class="srow-site">@ ${esc(g.site)}</span>
      </li>`);

  const trackRow = (g) => `
    <li class="srow">
      <span class="srow-wk">Week ${g.week}</span>
      <span class="srow-opp">${g.home ? 'vs.' : 'at'} ${esc(g.opp)}</span>
      ${g.result
        ? `<span class="srow-res">${esc(g.score)}<span class="wl ${g.result}">${g.result}<span class="sr-only">${g.result === 'W' ? ' win' : ' loss'}</span></span></span>`
        : '<span class="srow-res tbd">Result pending</span>'}
      <span class="srow-site">@ ${esc(g.site)}</span>
    </li>`;

  /* The channel's public subscriber count: the figure sets itself digit by digit, a hairline rule fills toward
     the next round number, and the status line only says "live" when YouTube was read in the last 30 minutes. */
  function subsLine(el) {
    el.innerHTML = `
      <p class="subs-top"><b class="subs-num"></b><span>subscribers on YouTube</span></p>
      <div class="subs-rule" aria-hidden="true"><i></i></div>
      <p class="subs-foot fine"><span data-status></span><span data-next></span></p>`;
    const num = $('.subs-num', el), bar = $('.subs-rule i', el), status = $('[data-status]', el), next = $('[data-next]', el);
    let shown;
    const paint = (text, count, live) => {
      status.innerHTML = live ? '<i class="dot on"></i>Live from YouTube' : `<i class="dot"></i>Count ${asOf}`;
      if (text === shown) return;
      shown = text;
      num.innerHTML = `<span class="sr-only">${esc(text)}</span><span class="roll" aria-hidden="true">${[...text].map((ch, i) => `<i style="--i:${i}">${esc(ch)}</i>`).join('')}</span>`;
      const step = 10 ** Math.floor(Math.log10(count)) / 10; // 123,000 counts in 10,000s
      const floor = Math.floor(count / step) * step;
      bar.style.setProperty('--fill', (count - floor) / step);
      next.textContent = `Next round number: ${compact(floor + step)}`;
    };
    const dated = () => paint(D.show.subscribers, D.show.subscribersNum, false);
    dated();
    const pull = async () => {
      let j;
      try {
        const r = await fetch('subs.php', { cache: 'no-store' });
        if (r.ok) j = await r.json();
      } catch { /* no PHP here (local preview) or YouTube unreachable */ }
      // subs.php can answer with an old cached count; only a recent read is called live.
      if (j?.count && Date.now() - Date.parse(j.fetchedAt) < 30 * 60 * 1000) paint(j.text, j.count, true);
      else dated();
    };
    pull();
    setInterval(pull, 5 * 60 * 1000);
  }

  /* ---------- season: one ordered slate (the next game, then the schedule); the clock decides where "next" is ---------- */
  // Preview knob: ?now=2026-10-11T14:00:00-04:00 shows the page as it will look at that moment.
  const SHIFT = Date.parse(new URLSearchParams(location.search).get('now')) - Date.now() || 0;
  const clock = () => Date.now() + SHIFT;
  const slate = [D.season.next, ...D.season.schedule];
  const slateAt = (now) => {
    const kicked = (g) => g.kickoff && Date.parse(g.kickoff) <= now;
    const last = slate.findLastIndex(kicked);
    const next = slate.find((g, i) => i > last && g.kickoff);
    return {
      next,
      rest: slate.slice(last + 1).filter((g) => g !== next),
      pending: slate.filter((g) => kicked(g) && !D.season.games.some((p) => p.week === g.week)),
    };
  };

  const nextGame = ({ next: n, rest }) => `
    ${n ? `<div class="kick" data-reveal>
      <div>
        <p class="eyebrow">Next kickoff · Week ${n.week}</p>
        <p class="kick-opp">Eagles ${n.home ? 'vs.' : 'at'} ${esc(n.opp)}</p>
        <p class="meta">@ ${esc(n.site)} · ${fmtDay(n.date)} · ${n.time} ET · ${esc(n.tv)}</p>
        <p class="fine">${esc(new Date(n.kickoff).toLocaleString(undefined, { weekday: 'long', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit', timeZoneName: 'short' }))}, your time</p>
      </div>
      <div class="cd" data-countdown role="timer" aria-label="Countdown to kickoff">
        ${['Days', 'Hrs', 'Min', 'Sec'].map((u) => `<span><b>--</b><i>${u}</i></span>`).join('')}
      </div>
    </div>` : ''}
    ${rest.length ? `<ol class="sched-list" data-reveal>${rest.map(schedRow).join('')}</ol>` : ''}
    <p class="fine">Times are Eastern. Dates, times and channels as listed on the Eagles' schedule ${fmtDate(D.season.scheduleAsOf)}.</p>`;

  function season() {
    const hosts = $$('#home-next, #news-next');
    if (!hosts.length) return;
    let target = 0; // kickoff the countdown is running to; 0 when no dated game is left
    const render = () => {
      const s = slateAt(clock());
      target = s.next ? Date.parse(s.next.kickoff) : 0;
      hosts.forEach((h) => { h.innerHTML = nextGame(s); });
      const played = $('#news-games');
      if (played) played.innerHTML = [...D.season.games, ...s.pending].map(trackRow).join('');
    };
    const tick = () => {
      if (target && target <= clock()) render(); // kickoff passed while the page was open: roll to the following game
      if (!target) return;
      const s = Math.floor((target - clock()) / 1000);
      const parts = [Math.floor(s / 86400), Math.floor((s % 86400) / 3600), Math.floor((s % 3600) / 60), s % 60];
      $$('[data-countdown] b').forEach((b, i) => { b.textContent = String(parts[i % 4]).padStart(2, '0'); });
    };
    render();
    tick();
    setInterval(tick, 1000);
  }

  /* ---------- chrome ---------- */
  const NAV = [['index.html', 'Home', 'home'], ['episodes.html', 'Episodes', 'episodes'], ['news.html', 'Eagles', 'news'],
    ['sponsors.html', 'Sponsors', 'sponsors'], ['merch.html', 'Merch', 'merch'], ['socials.html', 'Socials', 'socials'], ['about.html', 'About', 'about']];
  const current = (key) => (key === page ? ' aria-current="page"' : '');
  const wordmark = 'The Thomas <em>Mott</em> Show';

  function chrome() {
    const head = $('#site-head');
    head.innerHTML = `
      <div class="wrap">
        <div class="mast">
          <p class="mast-note meta">On YouTube since ${esc(D.show.joined)}</p>
          <a class="brand" href="index.html" aria-label="${esc(D.show.name)} home">${wordmark}</a>
          <a class="btn sm mast-cta" href="subscribe.html">Get updates</a>
          <button type="button" class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
        </div>
        <nav class="nav" id="nav" aria-label="Main">
          ${NAV.map(([href, label, key]) => `<a href="${href}"${current(key)}>${label}</a>`).join('')}
          <a class="nav-cta" href="subscribe.html"${current('subscribe')}>Get updates</a>
        </nav>
      </div>`;
    const btn = $('.menu-btn', head);
    const setOpen = (open) => { head.classList.toggle('open', open); btn.setAttribute('aria-expanded', String(open)); };
    btn.addEventListener('click', () => setOpen(!head.classList.contains('open')));
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && head.classList.contains('open')) { setOpen(false); btn.focus(); }
    });

    const c = D.contact;
    $('#site-foot').innerHTML = `
      <div class="wrap">
        <div class="foot-grid">
          <div class="foot-brand">
            <span class="brand">${wordmark}</span>
            <p>Unfiltered Eagles talk from ${esc(D.show.host)}.</p>
          </div>
          <div>
            <p class="foot-h">Explore</p>
            <ul>${NAV.slice(1).map(([href, label]) => `<li><a href="${href}">${label}</a></li>`).join('')}<li><a href="subscribe.html">Get updates</a></li></ul>
          </div>
          <div>
            <p class="foot-h">Follow</p>
            <ul>${D.socials.map((s) => `<li><a href="${esc(s.url)}" ${EXT}>${esc(s.name)}</a></li>`).join('')}</ul>
          </div>
          <div class="foot-contact">
            <p class="foot-h">Contact</p>
            <ul>
              <li><a class="email" href="${mailto(c.email)}">${c.email}</a></li>
              <li><span class="fine">Advertising</span><br><a class="email" href="${mailto(c.advertisingEmail)}">${c.advertisingEmail}</a></li>
            </ul>
          </div>
        </div>
        <div class="foot-legal fine">
          <p>${esc(D.show.name)} is an independent fan and media site. It is not affiliated with, endorsed by or sponsored by the NFL or the Philadelphia Eagles.</p>
          <p>Concept demo by Top Shelf Business Solutions. Videos, merch and channel numbers come from the show's public channel and the store it links to.</p>
        </div>
      </div>`;
  }

  /* ---------- video player (native <dialog>: Esc closes, focus is trapped and returned) ---------- */
  function player() {
    const dlg = document.createElement('dialog');
    dlg.className = 'player';
    dlg.setAttribute('aria-labelledby', 'player-title');
    dlg.innerHTML = `
      <div class="player-bar"><h2 id="player-title"></h2><button type="button" class="btn sm ghost">Close</button></div>
      <div class="player-frame"></div>
      <div class="player-meta meta"></div>`;
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
      $('.player-meta', dlg).innerHTML = `<span>${fmtDate(v.date)} · ${int(v.views)} views ${asOf} · ${fmtDur(v.seconds)}</span><a class="more" href="${esc(v.url)}" ${EXT}>Watch on YouTube</a>`;
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
        if (!emailOk) { err.textContent = 'That email doesn’t look right. Check it and try again.'; return email.focus(); }
        if (boxes.length && !picked.length) { err.textContent = 'Pick at least one thing to hear about.'; return boxes[0].focus(); }
        const name = form.elements.firstName?.value.trim();
        const wants = picked.length ? new Intl.ListFormat('en').format(picked) : 'show updates';
        const done = document.createElement('div');
        done.className = 'success';
        done.setAttribute('role', 'status');
        done.tabIndex = -1;
        done.innerHTML = `
          <p class="eyebrow">Demo form</p>
          <p class="big">You’re in${name ? `, ${esc(name)}` : ''}.</p>
          <p>Sort of. This is a demo, so nothing was sent and nothing was saved. On the live site, ${esc(email.value.trim())} would be signed up for ${esc(wants)}.</p>`;
        form.replaceWith(done);
        done.focus();
      });
    });
  }

  /* ---------- pages ---------- */
  const pages = {
    home() {
      const v = D.videos[0];
      $('#hero-cta').innerHTML = `
        <button type="button" class="btn" data-video="${v.id}">Watch the latest</button>
        <a class="btn ghost" href="${D.show.subscribeUrl}" ${EXT}>Subscribe on YouTube</a>`;
      subsLine($('#subs'));
      $('#home-lead').innerHTML = `
        <button type="button" class="frame" data-video="${v.id}" aria-label="Play the latest video: ${esc(v.title)}" data-reveal>
          ${media(`https://i.ytimg.com/vi/${v.id}/maxresdefault.jpg`, '', 1280, 720, 'r16',
            `<span class="play"></span><span class="dur">${fmtDur(v.seconds)}</span>`, `data-fallback="${v.thumb}"`)}
        </button>
        <div data-reveal>
          <p class="meta">${fmtDate(v.date)} · ${compact(v.views)} views</p>
          <p class="lead-title">${esc(v.title)}</p>
          <div class="btn-row"><button type="button" class="btn" data-video="${v.id}">Play it here</button></div>
        </div>`;
      $('#home-list').innerHTML = D.videos.slice(1, 9).map(story).join('');
      $('#home-list').insertAdjacentHTML('afterend', `<p class="fine" style="margin-top:14px">Views on this page ${asOf}.</p>`);
      $('#home-names').innerHTML = D.sponsors.map((s) => `<li>${esc(s.name)}</li>`).join('');
    },

    episodes() {
      const list = $('#ep-list'), q = $('#ep-q'), sort = $('#ep-sort'), count = $('#ep-count');
      const render = () => {
        const term = plain(q.value.trim());
        const found = D.videos.filter((v) => plain(v.title).includes(term))
          .sort((a, b) => (sort.value === 'views' ? b.views - a.views : b.date.localeCompare(a.date)));
        count.textContent = `${found.length} of ${D.videos.length} recent videos. Views ${asOf}.`;
        list.innerHTML = found.map(story).join('') || '<li class="empty">Nothing matches that. Try fewer words, or just type “Eagles”.</li>';
      };
      q.addEventListener('input', render);
      sort.addEventListener('change', render);
      render();
      $('#ep-all').innerHTML = `<a class="btn ghost" href="${D.show.youtube}" ${EXT}>Everything older is on YouTube</a>`;
    },

    news() {
      const s = D.season;
      $('#news-record').innerHTML = `<b>${esc(s.record)}</b><span class="meta">Record through Week ${s.games.at(-1).week}, ${s.year} season</span>`;
      $('#news-heads').innerHTML = D.videos.map((v) => `
        <li><button type="button" class="head" data-video="${v.id}">
          <span class="meta">${fmtDate(v.date)}</span>
          <span class="head-title">${esc(v.title)}</span>
          <span class="meta">${fmtDur(v.seconds)}</span>
        </button></li>`).join('');
    },

    sponsors() {
      const grid = $('#sp-grid');
      grid.innerHTML = D.sponsors.map((s) => `
        <article class="sponsor" data-reveal>
          <h3>${esc(s.name)}</h3>
          ${s.offer ? `<p>${esc(s.offer)}</p>` : '<p class="fine">Check the sponsor’s site for current terms.</p>'}
          ${s.terms ? `<p class="fine">${esc(s.terms)}</p>` : ''}
          <p class="fine">Sponsored ${D.videos.filter((v) => v.sponsor === s.name).length} of the last ${D.videos.length} videos</p>
          ${s.code ? `<p class="code"><span class="sr-only">Promo code </span><code>${esc(s.code)}</code></p>` : ''}
          <div class="sp-act">
            ${s.code ? `<button type="button" class="btn sm" data-copy>Copy<span class="sr-only"> ${esc(s.name)} code</span></button>` : ''}
            <a class="more" href="${esc(s.url)}" ${EXT}>Visit<span class="sr-only"> ${esc(s.name)}</span></a>
          </div>
        </article>`).join('');
      grid.addEventListener('click', async (e) => {
        const b = e.target.closest('[data-copy]');
        if (!b) return;
        const code = $('code', b.closest('.sponsor'));
        const label = b.firstChild; // the visible "Copy" text node
        try {
          await navigator.clipboard.writeText(code.textContent);
          label.textContent = 'Copied';
        } catch {
          // No clipboard permission (or not a secure origin): select the code so Ctrl/Cmd+C works.
          getSelection().selectAllChildren(code);
          label.textContent = 'Selected';
        }
        setTimeout(() => { label.textContent = 'Copy'; }, 1800);
      });
      const avg = D.videos.reduce((sum, v) => sum + v.views, 0) / D.videos.length;
      $('#sp-stats').innerHTML = `
        <div class="stats">
          ${stat(esc(D.show.subscribers), 'YouTube subscribers')}
          ${stat(compact(D.show.totalViews), 'Total views')}
          ${stat(int(D.show.videoCount), 'Videos published')}
          ${stat(compact(avg), `Average views per video, computed from the last ${D.videos.length} uploads`)}
        </div>
        <p class="fine" style="margin-top:14px">Channel numbers ${asOf}.</p>`;
      $$('[data-admail]').forEach((a) => { a.href = mailto(D.contact.advertisingEmail, `Advertising on ${D.show.name}`); });
      $('#sp-mail').textContent = D.contact.advertisingEmail;
    },

    merch() {
      const p = D.merch.products[0], store = esc(D.merch.storeName);
      const SWATCH = { Black: '#111', Natural: '#e8dfcc', White: '#fff' };
      $('#merch-product').innerHTML = `
        ${media(p.image, `${p.name} tee in black, front`, 800, 800, 'r11', '', 'fetchpriority="high"')}
        <div>
          <p class="eyebrow">Sold on ${store}</p>
          <h2 class="display">${esc(p.name)}</h2>
          <p class="price">$${esc(p.price)}</p>
          <ul class="swatches" aria-label="Colors">${p.colors.map((c) => `<li><i style="background:${SWATCH[c] || 'transparent'}"></i>${esc(c)}</li>`).join('')}</ul>
          <p class="fine" style="margin-top:14px">Pick your ${esc(new Intl.ListFormat('en').format(p.opt.map((o) => o.toLowerCase())))} on the store page.</p>
          <div class="btn-row">
            <a class="btn" href="${esc(p.url)}" ${EXT}>Buy on ${store}</a>
            <a class="btn ghost" href="${esc(D.merch.storeUrl)}" ${EXT}>Visit the store</a>
          </div>
        </div>`;
    },

    socials() {
      const card = (name, handle, note, go, url) => `
        <a class="social" href="${esc(url)}" ${EXT} data-reveal>
          <span class="social-name">${esc(name)}</span>
          <span class="social-handle">${esc(handle)}</span>
          ${note ? `<span class="meta">${esc(note)}</span>` : ''}
          <span class="go">${esc(go)}</span>
        </a>`;
      const m = D.show.community;
      $('#soc-grid').innerHTML = D.socials.map((s) => card(s.name, s.handle, s.stat && `${s.stat} ${asOf}`, `Follow on ${s.name}`, s.url)).join('')
        + card(m.name, m.note, '', 'Join on YouTube', m.url);
      $('#soc-also').innerHTML = D.alsoOn.map((a) => card(a.name, a.kind, '', 'Open on YouTube', a.url)).join('');
    },

    about() {
      const s = D.show, c = D.contact;
      $('#about-words').innerHTML = `
        <blockquote>${esc(s.about)}</blockquote>
        <p class="fine">From the channel's About page. On YouTube since ${esc(s.joined)}. ${int(s.videoCount)} videos and ${esc(s.subscribers)} subscribers ${asOf}.</p>
        <div class="btn-row"><a class="btn" href="${s.subscribeUrl}" ${EXT}>Subscribe on YouTube</a><a class="btn ghost" href="episodes.html">Watch episodes</a></div>`;
      $('#about-contact').innerHTML = `
        <div><h3>General</h3><p class="fine">For anything about the show.</p><a class="email" href="${mailto(c.email)}">${c.email}</a></div>
        <div><h3>Advertising</h3><p class="fine">Sponsorships and brand deals.</p><a class="email" href="${mailto(c.advertisingEmail, `Advertising on ${s.name}`)}">${c.advertisingEmail}</a></div>`;
    },
  };

  /* ---------- motion: enhancement only. Content is visible by default; nothing below runs without GSAP. ---------- */
  function motion() {
    if (reduced || !window.gsap || !window.ScrollTrigger) return;
    const { gsap, ScrollTrigger } = window;
    gsap.registerPlugin(ScrollTrigger);
    gsap.config({ nullTargetWarn: false }); // not every page has reveal targets
    if (window.Lenis) {
      lenis = new window.Lenis({ lerp: 0.1 });
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add((t) => lenis.raf(t * 1000));
      gsap.ticker.lagSmoothing(0);
    }
    // Signature move: the headline sets itself line by line while the portrait rises into its arch.
    const h1 = $('#hero-h1');
    if (h1) {
      h1.classList.add('masking');
      gsap.from('.ln > span', { yPercent: 105, duration: 1, ease: 'power4.out', stagger: 0.1, onComplete: () => h1.classList.remove('masking') });
      gsap.fromTo('.portrait .media', { clipPath: 'inset(100% 0% 0% 0%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: 1.2, ease: 'power3.out', delay: 0.15, clearProps: 'clipPath' });
      gsap.from('.portrait img', { scale: 1.18, duration: 1.6, ease: 'power3.out', delay: 0.15 });
      gsap.to('.portrait-back', { yPercent: -7, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true } });
    }
    // transition:none so CSS hover transitions don't fight the tween; clearProps hands the elements back after.
    // Opacity only (never visibility) so keyboard focus still reaches content that hasn't scrolled in yet.
    gsap.set('[data-reveal]', { opacity: 0, y: 22, transition: 'none' });
    ScrollTrigger.batch('[data-reveal]', {
      start: 'top 94%', once: true,
      onEnter: (els) => gsap.to(els, { opacity: 1, y: 0, duration: 0.6, ease: 'power3.out', stagger: 0.05, clearProps: 'all' }),
    });
  }

  chrome();
  player();
  pages[page]?.();
  forms();
  season();
  motion();
})();
