/* The Philly Special Show demo. Every page renders from data.js (window.PSS); no facts live in this file. */
(() => {
  'use strict';
  const D = window.PSS;
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
  const ttl = (t) => esc(t).replace(/[0-9]+[-–][0-9]+/g, '<span class="nb">$&</span>');
  const fmtDur = (s) => {
    const h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), sec = String(s % 60).padStart(2, '0');
    return h ? `${h}:${String(m).padStart(2, '0')}:${sec}` : `${m}:${sec}`;
  };
  const compact = (n) => new Intl.NumberFormat('en-US', { notation: 'compact', maximumFractionDigits: 1 }).format(n);
  const int = (n) => Math.round(n).toLocaleString('en-US');
  const slug = (a) => a.url.split('/').pop();
  const articleHref = (a) => `article.html?a=${encodeURIComponent(slug(a))}`;
  const asOf = `as of ${fmtDate(D.show.statsAsOf)}`;
  const plain = (t) => t.toLowerCase().replace(/[‘’]/g, "'");
  const matches = (text, q) => plain(text).includes(plain(q.trim()));

  const media = (src, alt, w, h, cls, inner = '', attrs = 'loading="lazy"') =>
    `<span class="media ${cls}"><img src="${esc(src)}" alt="${esc(alt)}" width="${w}" height="${h}" decoding="async" referrerpolicy="no-referrer" ${attrs}>${inner}</span>`;

  // Hotlinked images: fall back once if a data-fallback is set, otherwise hide and let the gradient show.
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
        <span class="card-title">${ttl(v.title)}</span>
        <span class="meta">${fmtDate(v.date)} · ${compact(v.views)} views</span>
      </span>
    </button>`;

  const articleCard = (a) => `
    <a class="card" href="${articleHref(a)}" data-reveal>
      ${media(a.image, '', 600, 400, 'r32')}
      <span class="card-body">
        <span><span class="tag quiet">${esc(a.series)}</span></span>
        <span class="card-title">${ttl(a.title)}</span>
        ${a.excerpt ? `<span class="clamp">${ttl(a.excerpt)}</span>` : ''}
        <span class="meta">${fmtDate(a.date)}</span>
      </span>
    </a>`;

  const leadStory = (a) => `
    <a class="lead" href="${articleHref(a)}" data-reveal>
      ${media(a.image, '', 900, 600, 'r32')}
      <span class="lead-body">
        <span><span class="tag">${esc(a.series)}</span></span>
        <span class="lead-title">${esc(a.title)}</span>
        ${a.excerpt ? `<p>${ttl(a.excerpt)}</p>` : ''}
        <span class="meta">${esc(D.writer.name)} · ${fmtDate(a.date)}</span>
      </span>
    </a>`;

  const SWATCH = { Black: '#111', Natural: '#e8dfcc', White: '#fff' };
  const productCard = (p) => `
    <article class="card product" data-reveal>
      ${media(p.image, `${p.name} tee`, 600, 600, 'r11')}
      <div class="card-body">
        <h3 class="card-title">${esc(p.name)}</h3>
        <p class="price">$${esc(p.price)}</p>
        <ul class="swatches" aria-label="Colors">${p.colors.map((c) => `<li><i style="background:${SWATCH[c] || 'transparent'}"></i>${esc(c)}</li>`).join('')}</ul>
        <a class="btn sm" href="${esc(p.url)}" ${EXT}>Buy on ${esc(D.merch.storeName)}<span class="sr-only">: ${esc(p.name)}</span></a>
      </div>
    </article>`;

  const stat = (text, label, count, fmt) =>
    `<div class="stat" data-reveal><b ${count ? `data-count="${count}" data-fmt="${fmt}"` : ''}>${text}</b><span class="meta">${label}</span></div>`;
  const channelStats = (extra = '') => `
    <div class="stats">
      ${stat(esc(D.show.subscribers), 'YouTube subscribers', D.show.subscribersNum, 'compact')}
      ${stat(compact(D.show.totalViews), 'Total views', D.show.totalViews, 'compact')}
      ${stat(int(D.show.videoCount), 'Videos published', D.show.videoCount, 'int')}
      ${extra}
    </div>
    <p class="fine" style="margin-top:14px">Channel numbers ${asOf}.</p>`;

  const fmtDay = (iso) => new Date(iso + 'T12:00:00').toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' });
  const schedRow = (g) => (g.bye
    ? `<li class="srow bye"><span class="meta">Week ${g.week}</span><span class="srow-opp">Bye week</span></li>`
    : `<li class="srow">
        <span class="meta">Week ${g.week}</span>
        <span><span class="srow-opp">${g.home ? 'vs.' : 'at'} ${esc(g.opp)}</span><span class="fine">@ ${esc(g.site)}</span></span>
        <span class="srow-when">${g.date ? `${fmtDay(g.date)} · ${g.time} ET · ${esc(g.tv)}` : 'Date and time TBD'}</span>
      </li>`);

  /* Hero scoreboard: the channel's public subscriber count, re-read from YouTube while the page is open. */
  function subsBoard(el) {
    let shown = '';
    const paint = (text, count, live) => {
      const top = `<span class="subs-dot${live ? ' on' : ''}"></span>${live ? 'Live from YouTube' : `YouTube · ${asOf}`}`;
      if (text === shown) { $('.subs-top', el).innerHTML = top; return; } // same number: leave the digits alone
      shown = text;
      el.classList.remove('in');
      const step = 10 ** (Math.floor(Math.log10(count)) - 1); // 166K counts toward 170K
      const next = (Math.floor(count / step) + 1) * step;
      el.innerHTML = `
        <p class="subs-top">${top}</p>
        <p class="subs-num" role="img" aria-label="${esc(text)} subscribers">${[...text].map((c) => (/[0-9]/.test(c)
          ? `<span class="dg" style="--d:${c}"><span>${'0123456789'.split('').join('<br>')}</span></span>`
          : `<span class="dg-x">${esc(c)}</span>`)).join('')}</p>
        <p class="subs-label">Subscribers<span>Next up: ${compact(next)}</span></p>
        <span class="subs-bar"><i style="--p:${(count % step) / step}"></i></span>`;
      requestAnimationFrame(() => requestAnimationFrame(() => el.classList.add('in'))); // digits roll up from zero
    };
    paint(D.show.subscribers, D.show.subscribersNum, false);
    const pull = async () => {
      try {
        const r = await fetch('subs.php', { cache: 'no-store' });
        const j = await r.json();
        if (r.ok && j.count) paint(j.text, j.count, true);
      } catch { /* no PHP here (local preview) or YouTube unreachable: keep the dated number */ }
    };
    pull();
    setInterval(pull, 5 * 60 * 1000);
  }

  const nextGame = () => {
    const n = D.season.next;
    const local = new Date(n.kickoff).toLocaleString(undefined, { weekday: 'long', month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit', timeZoneName: 'short' });
    return `
    <div class="bug" data-reveal>
      <div>
        <p class="eyebrow" style="margin:0">Next kickoff · Week ${n.week}</p>
        <p class="bug-opp">Eagles vs. ${esc(n.opp)}</p>
        <p class="meta">@ ${esc(n.site)} · ${esc(n.tv)}</p>
        <p class="fine" style="margin-top:6px">${esc(local)}, your time</p>
      </div>
      <div class="cd" data-countdown role="timer" aria-label="Countdown to kickoff">
        ${['Days', 'Hrs', 'Min', 'Sec'].map((u) => `<span><b>--</b><i>${u}</i></span>`).join('')}
      </div>
    </div>
    <div class="sched" data-reveal>
      <p class="eyebrow">Rest of the schedule</p>
      <ol class="sched-list">${D.season.schedule.map(schedRow).join('')}</ol>
      <p class="fine">Times are Eastern. Dates, times and channels as listed on the Eagles' official schedule ${fmtDate(D.season.scheduleAsOf)}.</p>
    </div>`;
  };

  function countdowns() {
    const els = $$('[data-countdown]');
    if (!els.length) return;
    const kickoff = new Date(D.season.next.kickoff).getTime();
    const tick = () => {
      const left = kickoff - Date.now();
      if (left <= 0) {
        els.forEach((el) => (el.closest('.bug') || el).remove()); // no next game in data to roll to
        return clearInterval(id);
      }
      const s = Math.floor(left / 1000);
      const parts = [Math.floor(s / 86400), Math.floor((s % 86400) / 3600), Math.floor((s % 3600) / 60), s % 60];
      els.forEach((el) => $$('b', el).forEach((b, i) => { b.textContent = String(parts[i]).padStart(2, '0'); }));
    };
    const id = setInterval(tick, 1000);
    tick();
  }

  // Filter chips: one pressed at a time. Returns nothing; calls onPick(label) on change.
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
  const NAV = [['index.html', 'Home', 'home'], ['episodes.html', 'Episodes', 'episodes'], ['news.html', 'Eagles News', 'news'],
    ['blog.html', 'DiBona Desk', 'blog'], ['merch.html', 'Merch', 'merch'], ['sponsors.html', 'Sponsors', 'sponsors'],
    ['socials.html', 'Socials', 'socials'], ['about.html', 'About', 'about']];
  const current = (key) => (key === (page === 'article' ? 'blog' : page) ? ' aria-current="page"' : '');

  function chrome() {
    const head = $('#site-head');
    head.innerHTML = `
      <div class="wrap head-in">
        <a class="brand" href="index.html"><img src="${D.show.logo}" alt="${esc(D.show.name)} home" width="1500" height="418"></a>
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

    const c = D.contact;
    $('#site-foot').innerHTML = `
      <div class="wrap">
        <div class="foot-grid">
          <div>
            <img src="${D.show.logo}" alt="${esc(D.show.name)}" width="1500" height="418" loading="lazy">
            <p>Eagles news from ${esc(D.show.host)}, with a side of sarcasm.</p>
          </div>
          <div>
            <p class="foot-h">Explore</p>
            <ul>${NAV.slice(1).map(([href, label]) => `<li><a href="${href}">${label}</a></li>`).join('')}<li><a href="subscribe.html">Get updates</a></li></ul>
          </div>
          <div>
            <p class="foot-h">Follow</p>
            <ul>${D.socials.map((s) => `<li><a href="${esc(s.url)}" ${EXT}>${esc(s.name)}</a></li>`).join('')}</ul>
          </div>
          <div>
            <p class="foot-h">Contact</p>
            <ul>
              <li><a href="mailto:${c.email}">${c.email}</a></li>
              <li>Advertising: <a href="mailto:${c.advertisingEmail}">${c.advertisingEmail}</a></li>
              <li><address>${c.mail.map(esc).join('<br>')}</address></li>
            </ul>
          </div>
        </div>
        <div class="foot-legal fine">
          <p>${esc(D.show.name)} is an independent fan and media site. It is not affiliated with, endorsed by or sponsored by the NFL or the Philadelphia Eagles.</p>
          <p>Concept demo by Top Shelf Business Solutions. Videos, articles, merch and channel numbers come from the show’s public channel, site and store.</p>
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
        if (!emailOk) { err.textContent = 'That email doesn’t look right. Check it and run it back.'; return email.focus(); }
        if (boxes.length && !picked.length) { err.textContent = 'Pick at least one thing to hear about.'; return boxes[0].focus(); }
        const name = form.elements.firstName?.value.trim();
        const wants = picked.length ? new Intl.ListFormat('en').format(picked) : 'show updates';
        const done = document.createElement('div');
        done.className = 'success';
        done.setAttribute('role', 'status');
        done.tabIndex = -1;
        done.innerHTML = `
          <p class="eyebrow" style="margin:0">Demo form</p>
          <p class="name">Clean snap${name ? `, ${esc(name)}` : ''}.</p>
          <p>That’s the whole signup. This is a demo, so nothing was sent and nothing was saved. On the live site, ${esc(email.value.trim())} would be signed up for ${esc(wants)}.</p>`;
        form.replaceWith(done);
        done.focus();
      });
    });
  }

  /* ---------- pages ---------- */
  const pages = {
    home() {
      const v = D.videos[0];
      $('#hero-bg').innerHTML = `<img src="${v.thumb}" alt="" width="480" height="360" referrerpolicy="no-referrer">`;
      $('#hero-h1').insertAdjacentHTML('beforeend', D.show.tagline.split(' ').map((w) => `<span><span>${esc(w)}</span></span>`).join(' '));
      $('#hero-ep').innerHTML = `
        <p class="meta">Latest episode · ${fmtDate(v.date)} · ${compact(v.views)} views</p>
        <p class="hero-title">${esc(v.title)}</p>
        <div class="btn-row">
          <button type="button" class="btn" data-video="${v.id}">Watch the latest</button>
          <a class="btn ghost" href="${D.show.subscribeUrl}" ${EXT}>Subscribe on YouTube</a>
        </div>
        <div class="subs" id="subs"></div>`;
      subsBoard($('#subs'));
      $('#hero-frame').innerHTML = `
        <button type="button" class="frame" data-video="${v.id}" aria-label="Play the latest episode: ${esc(v.title)}">
          ${media(`https://i.ytimg.com/vi/${v.id}/maxresdefault.jpg`, '', 1280, 720, 'r16',
            `<span class="tag">Latest episode</span><span class="play"></span><span class="dur">${fmtDur(v.seconds)}</span>`,
            `data-fallback="${v.thumb}" fetchpriority="high"`)}
        </button>`;
      $('#home-next').innerHTML = nextGame();
      $('#home-rail').innerHTML = D.videos.slice(1, 9).map(videoCard).join('');
      $('#home-articles').innerHTML = leadStory(D.articles[0]) + `<div class="grid">${D.articles.slice(1, 5).map(articleCard).join('')}</div>`;
      $('#home-stats').innerHTML = channelStats();
      const names = D.sponsors.map((s) => `<span>${esc(s.name)}</span>`).join('');
      $('#home-marquee').innerHTML = `<div class="marquee-track">${names}${names.replaceAll('<span>', '<span aria-hidden="true">')}</div>`;
      $('#home-merch').innerHTML = D.merch.products.slice(0, 4).map(productCard).join('');
    },

    episodes() {
      const grid = $('#ep-grid'), q = $('#ep-q'), sort = $('#ep-sort'), count = $('#ep-count');
      const render = () => {
        const list = D.videos.filter((v) => matches(v.title, q.value))
          .sort((a, b) => (sort.value === 'views' ? b.views - a.views : b.date.localeCompare(a.date)));
        count.textContent = `${list.length} of ${D.videos.length} recent episodes`;
        grid.innerHTML = list.map(videoCard).join('') || '<p class="empty">Nothing matches that. Try fewer words, or just type “Eagles”. That one tends to work.</p>';
      };
      q.addEventListener('input', render);
      sort.addEventListener('change', render);
      render();
    },

    news() {
      const s = D.season;
      $('#news-record').textContent = s.record;
      $('#news-games').innerHTML = s.games.map((g) => `
        <li class="game" data-reveal>
          <span class="meta">Week ${g.week}</span>
          <span class="game-opp">${esc(g.opp)}</span>
          <span class="fine">@ ${esc(g.site)}</span>
          <span class="game-res"><span class="wl ${g.result}">${g.result}<span class="sr-only">${g.result === 'W' ? ' win' : ' loss'}</span></span>${esc(g.score)}</span>
        </li>`).join('');
      $('#news-next').innerHTML = nextGame();

      const feed = [
        ...D.videos.map((v) => ({ type: 'Videos', date: v.date, html: `
          <button type="button" class="frow" data-video="${v.id}">
            ${media(v.thumb, '', 480, 270, 'r16')}
            <span class="frow-body"><span class="frow-top"><span class="tag">Video</span><span class="meta">${fmtDate(v.date)} · ${fmtDur(v.seconds)}</span></span><span class="card-title">${ttl(v.title)}</span></span>
          </button>` })),
        ...D.articles.map((a) => ({ type: 'Articles', date: a.date, html: `
          <a class="frow" href="${articleHref(a)}">
            ${media(a.image, '', 480, 270, 'r16')}
            <span class="frow-body"><span class="frow-top"><span class="tag quiet">Article</span><span class="meta">${fmtDate(a.date)} · ${esc(a.series)}</span></span><span class="card-title">${ttl(a.title)}</span></span>
          </a>` })),
      ].sort((a, b) => b.date.localeCompare(a.date));
      const render = (type) => {
        $('#news-feed').innerHTML = feed.filter((f) => type === 'All' || f.type === type).map((f) => `<li>${f.html}</li>`).join('');
      };
      chips($('#news-chips'), ['All', 'Videos', 'Articles'], 'All', render);
      render('All');
    },

    blog() {
      const wanted = new URLSearchParams(location.search).get('series');
      let series = D.writer.series.includes(wanted) ? wanted : 'All';
      const q = $('#blog-q'), out = $('#blog-list'), count = $('#blog-count');
      const render = () => {
        const list = D.articles.filter((a) => (series === 'All' || a.series === series) && matches(`${a.title} ${a.excerpt}`, q.value));
        const browsing = series === 'All' && !q.value.trim();
        count.textContent = `${list.length} of ${D.articles.length} recent articles`;
        out.innerHTML = !list.length ? '<p class="empty">No articles match. Loosen the filter and take another shot.</p>'
          : (browsing ? leadStory(list[0]) : '') + `<div class="grid">${(browsing ? list.slice(1) : list).map(articleCard).join('')}</div>`;
      };
      chips($('#blog-chips'), ['All', ...D.writer.series], series, (s) => { series = s; render(); });
      q.addEventListener('input', render);
      render();
      $('#blog-author').innerHTML = authorBox();
    },

    article() {
      const key = new URLSearchParams(location.search).get('a') ?? '';
      const i = /^\d+$/.test(key) ? Number(key) : D.articles.findIndex((a) => slug(a) === key);
      const a = D.articles[i];
      const body = $('#art-body');
      if (!a) {
        $('#art-title').textContent = 'That article took a bad angle';
        body.innerHTML = '<p class="lede">We couldn’t find that one. The rest of the coverage is where you left it.</p><div class="btn-row"><a class="btn" href="blog.html">Back to the DiBona Desk</a></div>';
        return;
      }
      document.title = `${a.title} | ${D.show.name}`;
      $('#art-title').textContent = a.title;
      $('#art-top').innerHTML = `<a class="tag" href="blog.html?series=${encodeURIComponent(a.series)}">${esc(a.series)}</a>`;
      const newer = D.articles[i - 1], older = D.articles[i + 1];
      const pn = (x, label) => (x ? `<a href="${articleHref(x)}"><span class="meta">${label}</span><span class="card-title">${ttl(x.title)}</span></a>` : '');
      body.innerHTML = `
        <p class="meta">By ${esc(D.writer.name)} · ${fmtDate(a.date)}</p>
        ${media(a.image, '', 1200, 800, 'r32', '', 'fetchpriority="high"')}
        ${a.excerpt ? `<p class="excerpt">${ttl(a.excerpt)}</p>` : '<p class="excerpt">No preview on this one. The full piece is a click away.</p>'}
        <div class="readmore">
          <p class="fine">This is a preview. The full article lives on the show’s site.</p>
          <div class="btn-row"><a class="btn" href="${esc(a.url)}" ${EXT}>Read the full article</a><a class="btn ghost" href="blog.html">All articles</a></div>
        </div>
        ${authorBox()}
        <nav class="pn" aria-label="More articles">${pn(newer, 'Newer')}${pn(older, 'Older')}</nav>`;
    },

    merch() {
      $('#merch-grid').innerHTML = D.merch.products.map(productCard).join('');
      $$('[data-store]').forEach((a) => { a.href = D.merch.storeUrl; });
    },

    sponsors() {
      $('#sp-grid').innerHTML = D.sponsors.map((s) => `
        <article class="sponsor" data-reveal>
          <h3 class="sponsor-name">${esc(s.name)}</h3>
          ${s.offer ? `<p>${esc(s.offer)}</p>` : ''}
          ${s.code ? `<div class="code"><span><span class="sr-only">Promo code </span><code>${esc(s.code)}</code></span><button type="button" class="btn sm" data-copy="${esc(s.code)}">Copy<span class="sr-only"> ${esc(s.name)} code</span></button></div>` : ''}
          <a class="more" href="${esc(s.url)}" ${EXT}>Visit ${esc(s.name)}</a>
        </article>`).join('');
      $('#sp-grid').addEventListener('click', async (e) => {
        const b = e.target.closest('[data-copy]');
        if (!b) return;
        const label = b.firstChild; // the visible "Copy" text node
        try {
          await navigator.clipboard.writeText(b.dataset.copy);
          label.textContent = 'Copied';
        } catch {
          // No clipboard permission (or not a secure origin): select the code so Ctrl/Cmd+C works.
          getSelection().selectAllChildren($('code', b.closest('.code')));
          label.textContent = 'Selected';
        }
        setTimeout(() => { label.textContent = 'Copy'; }, 1800);
      });
      const avg = D.videos.reduce((sum, v) => sum + v.views, 0) / D.videos.length;
      $('#sp-stats').innerHTML = channelStats(stat(compact(avg), `Average views, last ${D.videos.length} uploads`, Math.round(avg), 'compact'));
      $('#sp-mail').href = `mailto:${D.contact.advertisingEmail}?subject=${encodeURIComponent(`Advertising on ${D.show.name}`)}`;
      $('#sp-email').textContent = D.contact.advertisingEmail;
    },

    socials() {
      $('#soc-grid').innerHTML = D.socials.map((s) => `
        <a class="social" href="${esc(s.url)}" ${EXT} data-reveal>
          <span class="social-name">${esc(s.name)}</span>
          <span class="social-handle">${esc(s.handle)}</span>
          ${s.stat ? `<span class="meta">${esc(s.stat)} ${asOf}</span>` : ''}
          <span class="go">Follow on ${esc(s.name)}</span>
        </a>`).join('') + `
        <a class="social" href="${D.show.membershipUrl}" ${EXT} data-reveal>
          <span class="social-name">Members</span>
          <span class="social-handle">YouTube channel membership</span>
          <span class="go">Become a member on YouTube</span>
        </a>`;
    },

    about() {
      const s = D.show, w = D.writer, c = D.contact;
      $('#about-josh').innerHTML = `
        ${media(s.hostPhoto, s.host, 600, 600, 'r11')}
        <div>
          <p class="eyebrow">Host</p>
          <h2>${esc(s.host)}</h2>
          <blockquote>${esc(s.about)}</blockquote>
          <p class="fine">On YouTube since ${fmtDate(s.joined)}. ${int(s.videoCount)} videos and ${esc(s.subscribers)} subscribers ${asOf}.</p>
          <div class="btn-row"><a class="btn" href="${s.subscribeUrl}" ${EXT}>Subscribe on YouTube</a><a class="btn ghost" href="episodes.html">Watch episodes</a></div>
        </div>`;
      $('#about-anthony').innerHTML = `
        <div class="monogram" aria-hidden="true">${w.name.split(' ').map((n) => n[0]).join('')}</div>
        <div>
          <p class="eyebrow">${esc(w.role)}</p>
          <h2>${esc(w.name)}</h2>
          <p class="bio">${esc(w.bio)}</p>
          <p class="links"><a href="${w.x}" ${EXT}>${esc(w.name)} on X</a><a href="${w.instagram}" ${EXT}>${esc(w.name)} on Instagram</a></p>
          <div class="btn-row"><a class="btn ghost" href="blog.html">Read the DiBona Desk</a></div>
        </div>`;
      $('#about-contact').innerHTML = `
        <div><h3>General</h3><p class="fine">Questions, tips, corrections, strongly worded opinions.</p><a href="mailto:${c.email}">${c.email}</a></div>
        <div><h3>Send me stuff</h3><address>${esc(s.name)}<br>${c.mail.map(esc).join('<br>')}</address></div>
        <div><h3>Advertising</h3><p class="fine">Sponsorships and brand deals.</p><a href="mailto:${c.advertisingEmail}">${c.advertisingEmail}</a></div>`;
    },
  };

  function authorBox() {
    const w = D.writer;
    return `
      <aside class="author" aria-label="About the author">
        <p class="eyebrow" style="margin:0">${esc(w.role)}</p>
        <p class="name">${esc(w.name)}</p>
        <p>${esc(w.bio)}</p>
        <p class="links"><a href="${w.x}" ${EXT}>X</a><a href="${w.instagram}" ${EXT}>Instagram</a><a href="about.html">About the show</a></p>
      </aside>`;
  }

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
    // Signature move: the tagline snaps up word by word, then the hero plate drifts as you scroll away.
    gsap.from('.kinetic > span > span', { yPercent: 110, duration: 1, ease: 'power4.out', stagger: 0.09 });
    if ($('.hero-bg img')) {
      gsap.to('.hero-bg img', { yPercent: 10, scale: 1.12, ease: 'none', scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true } });
      gsap.from('.frame', { y: 40, autoAlpha: 0, rotate: 1.5, duration: 1.1, ease: 'power3.out', delay: 0.15 });
    }
    // transition:none so the cards' CSS hover transition doesn't fight the tween; clearProps hands them back after.
    gsap.set('[data-reveal]', { autoAlpha: 0, y: 26, transition: 'none' });
    ScrollTrigger.batch('[data-reveal]', {
      start: 'top 94%', once: true,
      onEnter: (els) => gsap.to(els, { autoAlpha: 1, y: 0, duration: 0.7, ease: 'power3.out', stagger: 0.06, clearProps: 'all' }),
    });
    $$('[data-count]').forEach((el) => {
      const end = Number(el.dataset.count), final = el.textContent, fmt = el.dataset.fmt === 'int' ? int : compact;
      const n = { v: 0 };
      gsap.to(n, {
        v: end, duration: 1.6, ease: 'power2.out', scrollTrigger: { trigger: el, start: 'top 92%', once: true },
        onUpdate: () => { el.textContent = fmt(n.v); },
        onComplete: () => { el.textContent = final; },
      });
    });
  }

  chrome();
  player();
  pages[page]?.();
  forms();
  countdowns();
  motion();
})();
