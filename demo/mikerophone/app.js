/* Mikerophone demo. Every page renders from data.js (window.MK); no facts live in this file. */
(() => {
  'use strict';
  const D = window.MK;
  if (!D) return;

  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const page = document.body.dataset.page;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const EXT = 'target="_blank" rel="noopener"';
  const S = D.show;
  let lenis = null;

  /* ---------- helpers ---------- */
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const fmtDate = (iso) => new Date(iso + 'T12:00:00').toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
  const fmtDur = (s) => {
    const h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), sec = String(s % 60).padStart(2, '0');
    return h ? `${h}:${String(m).padStart(2, '0')}:${sec}` : `${m}:${sec}`;
  };
  const compact = (digits) => {
    const f = new Intl.NumberFormat('en-US', { notation: 'compact', maximumFractionDigits: digits });
    return (n) => f.format(n);
  };
  // c0: 874M. c1: 140.5K. c2: 1.12M. int: 2,819.
  const FMT = { c0: compact(0), c1: compact(1), c2: compact(2), int: (n) => Math.round(n).toLocaleString('en-US') };
  const asOf = `as of ${fmtDate(S.statsAsOf)}`;
  const slug = (name) => name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  const LINKS = { subscribe: S.subscribeUrl, youtube: S.youtube };
  // Every playable video by id: the series picks, then the latest uploads (which carry date, views and length).
  const VIDEOS = new Map([...D.series.flatMap((s) => s.videos), ...D.videos].map((v) => [v.id, v]));

  // Hotlinked images: hide a broken one and let the panel colour show. (load/error don't bubble: capture phase.)
  document.addEventListener('error', (e) => { if (e.target.tagName === 'IMG') e.target.classList.add('failed'); }, true);
  // YouTube answers a missing thumbnail with a 120px grey placeholder instead of an error.
  document.addEventListener('load', (e) => {
    if (e.target.tagName === 'IMG' && e.target.closest('.thumb') && e.target.naturalWidth <= 120) e.target.classList.add('failed');
  }, true);

  /* ---------- shared components ---------- */
  const thumb = (v, inner = '') =>
    `<span class="thumb"><img src="${esc(v.thumb)}" alt="" width="480" height="360" loading="lazy" decoding="async" referrerpolicy="no-referrer">${inner}</span>`;

  // One video, as a button that opens the player. Series picks have no date, views or length, so none is shown.
  const tile = (v, cls = '') => `
    <button type="button" class="tile ${cls}" data-video="${esc(v.id)}" data-reveal>
      ${thumb(v, `<span class="eq" aria-hidden="true"><i></i><i></i><i></i><i></i></span>${v.seconds ? `<span class="dur">${fmtDur(v.seconds)}</span>` : ''}`)}
      <span class="tile-body">
        <span class="tile-title"><span class="sr-only">Play: </span>${esc(v.title)}</span>
        ${v.date ? `<span class="meta">${fmtDate(v.date)} · ${FMT.c1(v.views)} views</span>` : ''}
      </span>
    </button>`;

  const shelf = (s, dark) => {
    const id = slug(s.name);
    return `
    <section class="shelf${dark ? ' dark' : ''}" id="${id}" aria-labelledby="${id}-h">
      <div class="wrap shelf-head" data-reveal>
        <div>
          <p class="kicker">${dark ? 'Featured series · ' : ''}${FMT.int(s.count)} videos</p>
          <h2 id="${id}-h">${esc(s.name)}</h2>
          <p class="lede">${esc(s.blurb)}</p>
        </div>
        <div class="shelf-ctl">
          <button type="button" class="arrow" data-rail="-1" aria-label="Scroll ${esc(s.name)} back">&larr;</button>
          <button type="button" class="arrow" data-rail="1" aria-label="Scroll ${esc(s.name)} forward">&rarr;</button>
          <a class="btn sm ghost" href="${esc(s.url)}" ${EXT}>See all ${FMT.int(s.count)} on YouTube</a>
        </div>
      </div>
      <div class="rail" role="region" tabindex="0" aria-label="${esc(s.name)}: ${s.videos.length} videos. Scrolls sideways.">
        <ul>${s.videos.map((v) => `<li>${tile(v)}</li>`).join('')}</ul>
      </div>
    </section>`;
  };

  const playlistRow = (p, href, ext) =>
    `<li><a href="${esc(href)}"${ext ? ` ${EXT}` : ''}>${esc(p.name)}<span class="count">${FMT.int(p.count)} videos</span></a></li>`;

  const stat = (text, label, count, fmt, note = '') => `
    <div class="stat" data-reveal>
      <b${count ? ` data-count="${count}" data-fmt="${fmt}"` : ''}>${esc(text)}</b>
      <span class="kicker">${esc(label)}</span>
      ${note ? `<span class="fine">${esc(note)}</span>` : ''}
    </div>`;
  const channelStats = () =>
    stat(FMT.c0(S.totalViews), 'Total views', S.totalViews, 'c0', `${FMT.int(S.totalViews)} in full`)
    + stat(S.subscribers, 'YouTube subscribers', S.subscribersNum, 'c2')
    + stat(FMT.int(S.videoCount), 'Videos published', S.videoCount, 'int');

  // links: [label, url] pairs, pinned to the bottom so a row of cards lines up.
  const card = (kicker, title, text, links) => `
    <article class="card" data-reveal>
      <p class="kicker">${esc(kicker)}</p>
      <h3>${esc(title)}</h3>
      ${text ? `<p class="meta">${esc(text)}</p>` : ''}
      <p class="card-links">${links.map(([label, url]) => `<a class="btn sm ghost" href="${esc(url)}" ${EXT}>${esc(label)}</a>`).join('')}</p>
    </article>`;

  const sponsorCard = (s) => `
    <article class="sponsor" data-reveal>
      <p class="kicker">Promo partner</p>
      <h3>${esc(s.name)}</h3>
      <p class="meta">${esc(s.note)}</p>
      <p class="offer">Offer listed with the link: ${esc(s.offer)}.</p>
      <div class="code"><span class="meta">Code</span><code>${esc(s.code)}</code><button type="button" class="btn sm" data-copy="${esc(s.code)}">Copy<span class="sr-only"> ${esc(s.name)} code</span></button></div>
      <a class="btn ghost" href="${esc(s.url)}" ${EXT}>Go to ${esc(s.name)}</a>
      <p class="fine">The link and code are the ones the channel shares. Terms are set by ${esc(s.name)}.</p>
    </article>`;

  // The public subscriber count as a studio level meter: the bars show how far the count has run
  // toward the next round number (our math from the count), and the tag says how fresh the number is.
  function subsLive(el) {
    const SEGS = 24;
    el.innerHTML = `
      <p class="subs-top"><span class="meta">YouTube subscribers</span><span class="subs-tag"></span></p>
      <p class="subs-num"></p>
      <div class="vu" aria-hidden="true">${Array.from({ length: SEGS }, (_, i) => `<i style="--i:${i}"></i>`).join('')}</div>
      <p class="subs-scale meta"><span></span><span></span></p>
      <p class="fine"></p>`;
    const tag = $('.subs-tag', el), num = $('.subs-num', el), segs = $$('.vu i', el);
    const [from, to] = $('.subs-scale', el).children, stamp = $('.fine', el);

    // checked: when subs.php read the number from YouTube. Left out for the dated number from data.js.
    const paint = (text, count, checked) => {
      tag.textContent = checked ? 'Live' : asOf;
      tag.classList.toggle('on', Boolean(checked));
      num.textContent = text; // YouTube's own rounding, e.g. "1.12M": shown as given, never re-parsed
      stamp.textContent = checked
        ? `Checked on YouTube at ${checked.toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' })}, your time.`
        : 'Dated figure from the channel’s YouTube page.';
      const step = 10 ** Math.floor(Math.log10(count)) / 10, base = Math.floor(count / step) * step;
      from.textContent = FMT.c2(base);
      to.textContent = `Next: ${FMT.c2(base + step)}`;
      const lit = Math.round(((count - base) / step) * SEGS);
      void el.offsetWidth; // so the first paint lights up from empty
      segs.forEach((s, i) => s.classList.toggle('on', i < lit));
    };
    const dated = () => paint(S.subscribers, S.subscribersNum);
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

  /* ---------- the signature: a waveform that answers the pointer and the scroll ---------- */
  // Desktop only. Phones, reduced motion and no-canvas browsers keep the still waveform drawn in CSS.
  function wave() {
    const c = $('#wave'), hero = $('.hero');
    const ctx = c && !reduced && innerWidth >= 700 && c.getContext('2d');
    if (!ctx) return;
    hero.classList.add('live');
    const PITCH = 9;
    let w = 0, h = 0, raf = 0, energy = 0, px = -1, lastY = scrollY, onScreen = true;
    const size = () => {
      const dpr = Math.min(devicePixelRatio || 1, 2);
      w = c.clientWidth; h = c.clientHeight;
      c.width = w * dpr; c.height = h * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    };
    const draw = (t) => {
      raf = requestAnimationFrame(draw);
      ctx.clearRect(0, 0, w, h);
      energy *= 0.93;
      const bars = Math.floor(w / PITCH);
      for (let i = 0; i < bars; i++) {
        const x = i / bars;
        const idle = Math.abs(Math.sin(x * 18 + t * 0.0021) + Math.sin(x * 41 - t * 0.0034) * 0.6 + Math.sin(x * 7 + t * 0.0012) * 0.8) / 2.4;
        const near = px < 0 ? 0 : Math.max(0, 1 - Math.abs(x - px) * 5);
        const level = Math.min(1, (0.14 + 0.4 * idle) * (0.6 + energy + near) * Math.sin(x * Math.PI));
        const bh = Math.max(2, level * h);
        ctx.fillStyle = level > 0.72 ? '#ff4d5e' : '#9d5cff'; // the bar clips into the red, like a meter
        ctx.globalAlpha = 0.16; // a wide soft pass under the bar stands in for glow, far cheaper than shadowBlur
        ctx.fillRect(i * PITCH - 3, (h - bh * 1.2) / 2, 10, bh * 1.2);
        ctx.globalAlpha = 0.9;
        ctx.fillRect(i * PITCH, (h - bh) / 2, 4, bh);
      }
    };
    const run = () => {
      cancelAnimationFrame(raf);
      if (onScreen && !document.hidden) raf = requestAnimationFrame(draw);
    };
    new ResizeObserver(size).observe(c);
    new IntersectionObserver(([e]) => { onScreen = e.isIntersecting; run(); }).observe(hero);
    document.addEventListener('visibilitychange', run);
    hero.addEventListener('pointermove', (e) => { px = e.clientX / w; });
    hero.addEventListener('pointerleave', () => { px = -1; });
    addEventListener('scroll', () => {
      energy = Math.min(1, energy + Math.abs(scrollY - lastY) / 90);
      lastY = scrollY;
    }, { passive: true });
    size();
  }

  /* ---------- chrome ---------- */
  const NAV = [['index.html', 'Home', 'home'], ['videos.html', 'Videos', 'videos'], ['series.html', 'Series', 'series'],
    ['sponsors.html', 'Sponsors', 'sponsors'], ['community.html', 'Community', 'community'], ['about.html', 'About', 'about']];
  const current = (key) => (key === page ? ' aria-current="page"' : '');
  const brand = (px) => `<a class="brand" href="index.html" aria-label="${esc(S.name)} home"><img src="${esc(S.logo)}" alt="" width="${px}" height="${px}">${esc(S.name)}</a>`;

  function chrome() {
    const head = $('#site-head');
    head.innerHTML = `
      <div class="wrap head-in">
        ${brand(36)}
        <button type="button" class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
        <nav class="nav" id="nav" aria-label="Main" data-lenis-prevent>
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
          <div class="foot-brand">
            ${brand(48)}
            <a class="btn sm" href="${esc(S.subscribeUrl)}" ${EXT}>Subscribe on YouTube</a>
          </div>
          <div>
            <p class="kicker foot-h">Pages</p>
            <ul>${NAV.map(([href, label]) => `<li><a href="${href}">${label}</a></li>`).join('')}<li><a href="subscribe.html">Get updates</a></li></ul>
          </div>
          <div>
            <p class="kicker foot-h">Follow</p>
            <ul>${D.socials.map((s) => `<li><a href="${esc(s.url)}" ${EXT}>${esc(s.name)}</a></li>`).join('')}</ul>
          </div>
        </div>
        <div class="foot-legal fine">
          <p>Independent creator site. Not affiliated with the NFL or any team.</p>
          <p>Concept demo by Top Shelf Business Solutions. Videos, titles and channel numbers come from the channel’s public YouTube pages.</p>
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
        <div class="player-bar"><span class="lamp" aria-hidden="true">Now playing</span><h2 id="player-title"></h2><button type="button" class="btn sm ghost">Close</button></div>
        <div class="player-frame"></div>
        <div class="player-meta meta"></div>
      </div>`;
    document.body.append(dlg);
    const frame = $('.player-frame', dlg);
    $('button', dlg).addEventListener('click', () => dlg.close());
    dlg.addEventListener('click', (e) => { if (e.target === dlg) dlg.close(); }); // backdrop click
    dlg.addEventListener('close', () => { frame.innerHTML = ''; lenis?.start(); });
    document.addEventListener('click', (e) => {
      const v = VIDEOS.get(e.target.closest('[data-video]')?.dataset.video);
      if (!v) return;
      $('#player-title').textContent = v.title;
      frame.innerHTML = `<iframe src="https://www.youtube-nocookie.com/embed/${esc(v.id)}?autoplay=1" title="${esc(v.title)}" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe>`;
      const facts = v.date ? `${fmtDate(v.date)} · ${FMT.int(v.views)} views · ${fmtDur(v.seconds)}` : '';
      $('.player-meta', dlg).innerHTML = `<span>${facts}</span><a href="${esc(v.url)}" ${EXT}>Watch on YouTube</a>`;
      lenis?.stop();
      dlg.showModal();
    });
  }

  /* ---------- shelf arrows ---------- */
  document.addEventListener('click', (e) => {
    const b = e.target.closest('[data-rail]');
    if (!b) return;
    const rail = $('.rail', b.closest('.shelf'));
    rail.scrollBy({ left: Number(b.dataset.rail) * rail.clientWidth * 0.8, behavior: reduced ? 'auto' : 'smooth' });
  });

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
        if (boxes.length && !picked.length) { err.textContent = 'Pick at least one kind of update.'; return boxes[0].focus(); }
        const name = form.elements.firstName?.value.trim();
        const wants = picked.length ? new Intl.ListFormat('en').format(picked) : 'new video updates';
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
      const v = D.videos[0], [featured, ...rest] = D.series;
      $('#hero-kicker').textContent = `${S.focus} · On YouTube since ${S.joined}`;
      $('#hero-lede').textContent = `${S.focus} stories with the volume up. ${FMT.int(S.videoCount)} videos so far.`;
      $('#hero-stage').innerHTML = `
        <figure class="host"><img src="${esc(S.banner)}" alt="From the ${esc(S.name)} channel’s YouTube banner" width="2120" height="351" fetchpriority="high"></figure>
        <div class="latest"><p class="kicker">Latest upload</p>${tile(v)}</div>`;
      subsLive($('#subs'));
      $('#home-numbers').innerHTML = channelStats();
      $('#home-asof').textContent = `Channel numbers ${asOf}.`;
      $('#home-latest').innerHTML = D.videos.slice(0, 6).map((x) => `<li>${tile(x)}</li>`).join('');
      $('#home-all').textContent = `All ${D.videos.length} latest videos`;
      $('#home-shelf').outerHTML = shelf(featured, true);
      $('#home-series').innerHTML = rest.map((s) => `
        <li><a class="scard" href="series.html#${slug(s.name)}" data-reveal>
          ${thumb(s.videos[0])}
          <span class="scard-body"><span class="scard-name">${esc(s.name)}</span><span class="meta">${esc(s.blurb)}</span></span>
          <span class="count">${FMT.int(s.count)} videos</span>
        </a></li>`).join('');
      $('#home-sponsor').innerHTML = D.sponsors.map(sponsorCard).join('');
      $('#home-socials').innerHTML = D.socials.map((s) => `<a class="chip" href="${esc(s.url)}" ${EXT}>${esc(s.name)}<span>${esc(s.handle)}</span></a>`).join('');
      wave();
    },

    videos() {
      const out = $('#vid-list'), q = $('#vid-q'), sort = $('#vid-sort');
      const by = { date: (a, b) => b.date.localeCompare(a.date), views: (a, b) => b.views - a.views, length: (a, b) => b.seconds - a.seconds };
      const render = () => {
        const needle = q.value.trim().toLowerCase();
        const list = D.videos.filter((v) => v.title.toLowerCase().includes(needle)).sort(by[sort.value]);
        $('#vid-count').textContent = `${list.length} of the ${D.videos.length} latest videos. Views ${asOf}.`;
        out.innerHTML = list.map((v) => `<li>${tile(v, 'row')}</li>`).join('') || '<li class="empty">No title matches that. Try a shorter search.</li>';
      };
      q.addEventListener('input', render);
      sort.addEventListener('change', render);
      render();
    },

    series() {
      $('#ser-shelves').outerHTML = D.series.map((s, i) => shelf(s, i === 0)).join('');
      $('#ser-other').innerHTML = D.otherPlaylists.map((p) => playlistRow(p, p.url, true)).join('');
      // The shelves did not exist when the browser looked for the #slug, so go there now.
      if (location.hash) document.getElementById(decodeURIComponent(location.hash.slice(1)))?.scrollIntoView();
    },

    sponsors() {
      $('#sp-main').innerHTML = D.sponsors.map(sponsorCard).join('');
      $('#sp-also').innerHTML = D.alsoLinked.map((a) => card('Linked in the descriptions', a.name, '', [['Open the link', a.url]])).join('');
      const avg = D.videos.reduce((sum, v) => sum + v.views, 0) / D.videos.length;
      $('#sp-stats').innerHTML = channelStats()
        + stat(FMT.c1(avg), `Average views, ${D.videos.length} latest videos`, Math.round(avg), 'c1', 'Computed here from the view counts on this site.');
      $('#sp-asof').textContent = `Channel and view numbers ${asOf}.`;
      $('#sp-contact-note').textContent = D.contact.note;
      $('#sp-contact').innerHTML = D.socials.filter((s) => ['X', 'Instagram', 'Discord'].includes(s.name))
        .map((s) => `<a class="chip" href="${esc(s.url)}" ${EXT}>${esc(s.name)}<span>${esc(s.handle)}</span></a>`).join('');
    },

    community() {
      $('#com-grid').innerHTML = D.socials.map((s) => card(s.name, s.handle, s.stat ? `${s.stat} ${asOf}` : '', [[`Open ${s.name}`, s.url]])).join('');
      $('#com-more').innerHTML =
        card('YouTube', 'Channel membership', 'Membership runs through YouTube, which lists the perks and the price.', [['Become a member', S.membershipUrl]])
        + card('Also from the channel', D.otherChannel.name, '', [['Open on YouTube', D.otherChannel.url]])
        + card('Music', D.music.credit, '', [['Spotify', D.music.url], ['Instagram', D.music.instagram]]);
    },

    about() {
      $('#about-logo').src = S.logo;
      $('#about-note').textContent = S.aboutNote;
      $('#about-stats').innerHTML = channelStats();
      $('#about-asof').textContent = `On YouTube since ${S.joined}. Channel numbers ${asOf}.`;
      $('#about-lib').innerHTML = D.series.map((s) => playlistRow(s, `series.html#${slug(s.name)}`, false)).join('')
        + D.otherPlaylists.map((p) => playlistRow(p, p.url, true)).join('');
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
    gsap.from('[data-in]', { opacity: 0, y: 26, duration: 0.9, ease: 'power3.out', stagger: 0.09, clearProps: 'opacity,transform' });
    // transition:none so a card's CSS hover transition doesn't fight the tween; clearProps hands it back after.
    // Opacity only, never visibility: cards below the fold must stay in the tab order before they are scrolled to.
    gsap.set('[data-reveal]', { opacity: 0, y: 22, transition: 'none' });
    ScrollTrigger.batch('[data-reveal]', {
      start: 'top 95%', once: true,
      onEnter: (els) => gsap.to(els, { opacity: 1, y: 0, duration: 0.6, ease: 'power3.out', stagger: 0.06, clearProps: 'all' }),
    });
    $$('[data-count]').forEach((el) => {
      const end = Number(el.dataset.count), final = el.textContent, fmt = FMT[el.dataset.fmt];
      const n = { v: 0 };
      gsap.to(n, {
        v: end, duration: 1.6, ease: 'power2.out', scrollTrigger: { trigger: el, start: 'top 94%', once: true },
        onUpdate: () => { el.textContent = fmt(n.v); },
        onComplete: () => { el.textContent = final; },
      });
    });
  }

  chrome();
  player();
  pages[page]?.();
  forms();
  motion();
})();
