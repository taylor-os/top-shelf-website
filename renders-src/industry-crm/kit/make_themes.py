"""Generate themes.css (one body.t-<industry> class per industry) and check WCAG contrast.

  python make_themes.py          writes themes.css, prints the contrast report, exits 1 if any check fails

Edit the PALETTES below, not themes.css. Each palette names a handful of key colors; everything
else (brand scale, lines, tints, semantic colors, customer-page tokens) is derived here so the
12 themes stay consistent. Chrome (sidebar / band / bars / tab bar) is always dark with light text.
"""
import sys
from pathlib import Path


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def hx(c):
    return "#%02x%02x%02x" % tuple(max(0, min(255, round(v))) for v in c)


def mix(a, b, t):  # t of a into b
    a, b = rgb(a), rgb(b)
    return hx(tuple(a[i] * t + b[i] * (1 - t) for i in range(3)))


def trip(h):
    return " ".join(str(v) for v in rgb(h))


def lum(h):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = rgb(h)
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


LIGHT_SEM = dict(green="#047857", green_ink="#166b46", amber="#b45309", amber_ink="#92400e", red="#b91c1c",
                 rose="#e11d48", badge="#e11d48", blue="#2563eb", blue_ink="#1d4ed8", violet="#7c3aed")
DARK_SEM = dict(green="#34d399", green_ink="#6ee7b7", amber="#fbbf24", amber_ink="#fcd34d", red="#fb8a8a",
                rose="#fb7185", badge="#e11d48", blue="#60a5fa", blue_ink="#93c5fd", violet="#a78bfa")

# mode, canvas, panel, chrome (sidebar) [, band], accent (brand 500), text ramp, button gradient (light, mid, deep) + its text,
# nav highlight on chrome, optional hairline on band/sidebar, section-bar color, customer-page accent (+ ink).
# Optional: deep = how far b-600..b-950 darken toward black in a light theme (default DEEP); a bright accent
# (amber, teal) needs more so its text shades stay AA. fonts = (heading, body) Google Fonts families for the
# customer pages (body.cx) only, copied from the paired website in pairs.json; staff pages keep Figtree.
# Every palette except car-lots, auto-detailing and fitness is taken from its paired website's styles.css
# (those three sites are being built to these palettes).
PALETTES = {
    "home-services": dict(mode="light", canvas="#f6f3ee", panel="#ffffff", side="#0b1b2b", band="#0e2740", accent="#f6a623",
        ink="#0b1b2b", ink2="#2f3d4a", muted="#3c4a57", muted2="#5a6976", faint="#a3aeb8",
        grad=("#fac969", "#f6a623", "#e08e12"), on_accent="#0b1b2b", nav_ink="#fac969", edge="rgb(246 166 35 / .55)",
        deep=(.40, .50, .60, .70, .80), cx_accent="#0e2740", cx_ink="#ffffff", cx_logo=("#f6a623", "#0b1b2b"),
        fonts=("Sora", "Inter")),
    "car-lots": dict(mode="dark", canvas="#111113", panel="#1a1a1d", side="#09090a", accent="#c9a34e",
        ink="#f4efe4", ink2="#ddd6c8", muted="#aca596", muted2="#938c7f", faint="#6b665d",
        grad=("#e3c378", "#c9a34e", "#a9873b"), on_accent="#17130a", edge="rgb(201 163 78 / .35)",
        cx_accent="#c9a34e", cx_ink="#17130a", fonts=("Archivo", "Figtree")),
    "auto-repair": dict(mode="dark", canvas="#15171b", panel="#1d2026", side="#0e0f12", accent="#e23b2e",
        ink="#f5f7f9", ink2="#d5dbe2", muted="#aeb6bf", muted2="#8a929b", faint="#5f6670",
        grad=("#e23b2e", "#c42e22", "#a62518"), on_accent="#ffffff", edge="rgb(226 59 46 / .45)", bar="#2c313a",
        cx_accent="#f0604f", cx_ink="#0e0f12", fonts=("Space Grotesk", "Inter")),
    "auto-detailing": dict(mode="dark", canvas="#07090d", panel="#0f131a", side="#030406", accent="#3b8eff",
        ink="#eaf0f7", ink2="#cbd5e1", muted="#9aa7b8", muted2="#8290a3", faint="#55637a",
        grad=("#3f87f2", "#2563eb", "#1d4ed8"), on_accent="#ffffff", edge="rgb(59 142 255 / .35)",
        cx_accent="#4f9cff", cx_ink="#04101f"),
    "fitness": dict(mode="dark", canvas="#161719", panel="#202124", side="#0e0f10", accent="#e0702e",
        ink="#f2f2f0", ink2="#d6d6d2", muted="#a9a9a4", muted2="#91918c", faint="#666662",
        grad=("#f08a45", "#e0702e", "#c95e1f"), on_accent="#180a03", edge="rgb(224 112 46 / .4)",
        cx_accent="#e0702e", cx_ink="#180a03"),
    "restaurants": dict(mode="dark", canvas="#141110", panel="#221c18", side="#0e0c0b", accent="#e8722a",
        ink="#f4ece2", ink2="#dcd3c6", muted="#c4bbae", muted2="#a0978b", faint="#6e655c",
        grad=("#f29a5b", "#e8722a", "#cf5f1f"), on_accent="#1a0f08", edge="rgb(228 180 88 / .4)",
        cx_accent="#e8722a", cx_ink="#1a0f08", fonts=("Fraunces", "Inter")),
    "real-estate": dict(mode="light", canvas="#f7f5f0", panel="#ffffff", side="#22493a", band="#2e5c4a", accent="#2e5c4a",
        ink="#211f1b", ink2="#413d36", muted="#575249", muted2="#6b665c", faint="#a8a397",
        grad=("#3a6e59", "#2e5c4a", "#22493a"), on_accent="#ffffff", nav_ink="#f0d496", edge="rgb(232 178 74 / .7)",
        cx_accent="#2e5c4a", cx_ink="#ffffff", fonts=("Cormorant Garamond", "Manrope")),
    "salon-spa": dict(mode="light", canvas="#f4ede3", panel="#fbf7f1", side="#4a2f4d", band="#5b3b5e", accent="#5b3b5e",
        ink="#2a2129", ink2="#45373f", muted="#5a4c54", muted2="#66585f", faint="#ad9fa6",
        grad=("#6e4c71", "#5b3b5e", "#4a2f4d"), on_accent="#fbf7f1", nav_ink="#e4c88a", edge="rgb(193 151 78 / .6)",
        cx_accent="#5b3b5e", cx_ink="#fbf7f1", fonts=("Cormorant Garamond", "Jost")),
    "medical-dental": dict(mode="light", canvas="#f5fbfb", panel="#ffffff", side="#0a555c", band="#0c6e77", accent="#17b0b8",
        ink="#123138", ink2="#2c464d", muted="#41585f", muted2="#526a6f", faint="#9fb4b7",
        grad=("#0e8a93", "#0c7c85", "#0a6168"), on_accent="#ffffff", nav_ink="#dcf1f2",
        deep=(.32, .42, .54, .65, .76), cx_accent="#0c6e77", cx_ink="#ffffff", fonts=("Manrope", "Inter")),
    "legal": dict(mode="light", canvas="#f5f1e8", panel="#fffdf8", side="#16231d", band="#1c2e26", accent="#a6813f",
        ink="#16231d", ink2="#2f3b35", muted="#48524c", muted2="#5a645d", faint="#aaa89e",
        grad=("#a6813f", "#8a6a2e", "#735823"), on_accent="#ffffff", nav_ink="#c7a65c", edge="rgb(166 129 63 / .85)",
        deep=(.20, .32, .44, .56, .70), cx_accent="#8a6a2e", cx_ink="#ffffff", fonts=("Playfair Display", "Inter")),
    "retail": dict(mode="light", canvas="#f4efe6", panel="#faf6ee", side="#5a3a2a", accent="#c0694a",
        ink="#2b211b", ink2="#44382f", muted="#544b42", muted2="#635a50", faint="#b3a698",
        grad=("#c0694a", "#a2543a", "#8c4530"), on_accent="#faf6ee", nav_ink="#f2dfd3",
        cx_accent="#a2543a", cx_ink="#faf6ee", fonts=("Bricolage Grotesque", "Inter")),
    "vet": dict(mode="light", canvas="#fbf8f3", panel="#ffffff", side="#175540", band="#1e6b54", accent="#1e6b54",
        ink="#16302a", ink2="#33443c", muted="#4c5a52", muted2="#58635b", faint="#a2aca5",
        grad=("#2a7d64", "#1e6b54", "#175540"), on_accent="#fbf8f3", nav_ink="#fee0d5", edge="rgb(238 114 86 / .6)",
        cx_accent="#1e6b54", cx_ink="#fbf8f3", fonts=("Quicksand", "Nunito Sans")),
}

DEEP = (.14, .28, .42, .55, .70)
SERIF = {"Cormorant Garamond", "Fraunces", "Playfair Display"}
SANS_STACK = 'ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif'
SERIF_STACK = 'Georgia, "Times New Roman", serif'


def font_stack(family):
    return f'"{family}", {SERIF_STACK if family in SERIF else SANS_STACK}'


def fonts_import():
    fams = sorted({f for p in PALETTES.values() for f in p.get("fonts", ())})
    q = "&".join(f"family={f.replace(' ', '+')}:wght@400;500;600" for f in fams)
    return f'@import url("https://fonts.googleapis.com/css2?{q}&display=swap");\n'


def scale(p):
    a = p["accent"]
    if p["mode"] == "light":
        lo = [(50, .10), (100, .20), (200, .35), (300, .52), (400, .75)]
        out = {k: mix(a, "#ffffff", t) for k, t in lo}
        out[500] = a
        out.update({k: mix("#000000", a, t) for k, t in zip((600, 700, 800, 900, 950), p.get("deep", DEEP))})
    else:  # dark: 50-400 are tints toward the panel, 600-950 lighten so they read as text on dark
        out = {k: mix(a, p["panel"], t) for k, t in [(50, .10), (100, .18), (200, .30), (300, .45), (400, .70)]}
        out[500] = a
        out.update({k: mix("#ffffff", a, t) for k, t in [(600, .16), (700, .32), (800, .48), (900, .64), (950, .80)]})
    return out


def alpha_over(color, a, base):
    return mix(color, base, a)


def build(name, p):
    dark = p["mode"] == "dark"
    sem = dict(DARK_SEM if dark else LIGHT_SEM)
    sc = scale(p)
    side, band = p["side"], p.get("band", p["side"])
    panel, canvas, ink = p["panel"], p["canvas"], p["ink"]
    t = {}  # token -> value
    for k, v in sc.items():
        t[f"b-{k}"] = trip(v)
    t["glow"] = trip(p["accent"])
    t.update({"grad-1": p["grad"][0], "grad-2": p["grad"][1], "grad-3": p["grad"][2], "on-accent": p["on_accent"],
              "focus": p["accent"] if dark else p["grad"][1]})
    soft = .16 if dark else .14
    if dark:
        on_em, on_dim, on_faint = ink, f"rgb({trip(ink)} / .74)", f"rgb({trip(ink)} / .52)"
        nav_bg, nav_ink = f"rgb({trip(p['accent'])} / .16)", hx(rgb(sc[700]))
        bar = p.get("bar", mix(p["accent"], canvas, .17))
        bubble = p.get("bubble", (mix(p["accent"], panel, .30), ink))
        band_btn = (p["grad"][1], p["on_accent"])
        t.update({"canvas": canvas, "sink": mix("#000000", canvas, .3), "well": mix("#ffffff", panel, .05),
                  "panel": panel, "panel-edge": "rgba(255, 255, 255, .06)", "panel-2": "rgba(255, 255, 255, .04)",
                  "head": mix("#ffffff", panel, .035), "hatch": mix("#ffffff", panel, .08), "tint": "rgba(255, 255, 255, .07)",
                  "line": mix("#ffffff", panel, .10), "line-soft": "rgba(255, 255, 255, .07)", "line-strong": mix("#ffffff", panel, .22),
                  "shadow": "0 10px 30px rgba(0, 0, 0, .35), inset 0 1px 0 rgba(255, 255, 255, .04)",
                  "shadow-sm": "0 2px 8px rgba(0, 0, 0, .3)"})
    else:
        on_em, on_dim, on_faint = "#ffffff", "rgba(255, 255, 255, .82)", "rgba(255, 255, 255, .6)"
        nav_bg, nav_ink = "rgba(255, 255, 255, .13)", p["nav_ink"]
        bar = p.get("bar", band)
        bubble = p.get("bubble", (band, "#ffffff"))
        band_btn = ("#ffffff", band)
        sh = trip(side)
        t.update({"canvas": canvas, "sink": mix(ink, canvas, .08), "well": mix(p["accent"], panel, .06),
                  "panel": panel, "panel-edge": "rgba(255, 255, 255, .7)", "panel-2": "rgba(255, 255, 255, .6)",
                  "head": mix(ink, panel, .025), "hatch": mix(ink, panel, .07), "tint": f"rgb({trip(ink)} / .05)",
                  "line": mix(ink, panel, .10), "line-soft": f"rgb({trip(ink)} / .06)", "line-strong": mix(ink, panel, .2),
                  "shadow": f"0 10px 30px rgb({sh} / .08), 0 0 26px rgb({trip(p['accent'])} / .06), inset 0 1px 0 rgba(255, 255, 255, .85)",
                  "shadow-sm": f"0 2px 8px rgb({sh} / .06)"})
    t.update({"ink": ink, "ink-2": p["ink2"], "muted": p["muted"], "muted-2": p["muted2"], "faint": p["faint"]})
    t.update({"em": band, "side": side, "band": band, "bar": bar, "tabbar": side, "dock-bg": side,
              "on-em": on_em, "on-em-dim": on_dim, "on-em-faint": on_faint, "em-line": "rgba(255, 255, 255, .1)",
              "nav-on-bg": nav_bg, "nav-on-ink": nav_ink, "band-edge": p.get("edge", "transparent"),
              "band-btn-bg": band_btn[0], "band-btn-ink": band_btn[1],
              "bubble-out": bubble[0], "bubble-out-ink": bubble[1]})
    for k in ("green", "amber", "blue", "violet"):
        t[k] = sem[k]
        t[f"{k}-soft"] = f"rgb({trip(sem[k])} / {soft})"
    t.update({"green-ink": sem["green_ink"], "amber-ink": sem["amber_ink"], "blue-ink": sem["blue_ink"],
              "red": sem["red"], "red-soft": f"rgb({trip(sem['red'])} / {soft})", "rose": sem["rose"], "rose-ink": sem["rose"],
              "badge": sem["badge"], "badge-ink": "#ffffff"})
    cx = {"accent": p["cx_accent"], "accent-ink": p["cx_ink"], "accent-soft": f"rgb({trip(p['cx_accent'])} / {.16 if dark else .09})",
          "cx-bg": canvas if dark else panel, "cx-card": panel if dark else "#ffffff" if panel == "#ffffff" else panel,
          "cx-ink": ink, "cx-ink-2": p["ink2"], "cx-muted": p["muted2"], "cx-faint": p["faint"], "cx-line": t["line"]}
    if "cx_logo" in p:
        cx["cx-logo"], cx["cx-logo-ink"] = p["cx_logo"]
    if dark:
        cx["cx-line"] = mix("#ffffff", panel, .14)
    if "fonts" in p:  # customer pages only: --font reaches body text and buttons, --font-head the headings
        cx["font-head"], cx["font"] = (font_stack(f) for f in p["fonts"])
    return t, cx, sc


def checks(name, p, t, cx, sc):
    dark = p["mode"] == "dark"
    panel, canvas = p["panel"], p["canvas"]
    soft = .16 if dark else .14
    on_dim_c = mix(t["on-em"], p["side"], .74 if dark else .82)
    nav_bg_c = mix(p["accent"], p["side"], .16) if dark else mix("#ffffff", p["side"], .13)
    rows = [
        ("ink / panel", t["ink"], panel, 4.5), ("muted / panel", t["muted"], panel, 4.5),
        ("muted-2 / panel", t["muted-2"], panel, 4.5), ("muted-2 / canvas", t["muted-2"], canvas, 4.5),
        ("on-em / sidebar", t["on-em"], p["side"], 4.5), ("on-em-dim / sidebar", on_dim_c, p["side"], 4.5),
        ("on-em / band", t["on-em"], t["band"], 4.5), ("on-em / bar", t["on-em"], t["bar"], 4.5),
        ("active nav", t["nav-on-ink"], nav_bg_c, 4.5),
        ("button text / grad-2", t["on-accent"], t["grad-2"], 4.5), ("button text / grad-1 (edge)", t["on-accent"], t["grad-1"], 3.0),
        ("band button", t["band-btn-ink"], t["band-btn-bg"], 4.5), ("out bubble", t["bubble-out-ink"], t["bubble-out"], 4.5),
        ("b-600 text / panel", sc[600], panel, 4.5),
        ("b-700 on brand chip", sc[700], mix(p["accent"], panel, .15), 4.5),
        ("green chip", t["green-ink"], mix(t["green"], panel, soft), 4.5), ("amber chip", t["amber-ink"], mix(t["amber"], panel, soft), 4.5),
        ("red chip", t["red"], mix(t["red"], panel, soft), 4.5), ("blue chip", t["blue-ink"], mix(t["blue"], panel, soft), 4.5),
        ("badge", t["badge-ink"], t["badge"], 4.5),
        ("cx ink / bg", cx["cx-ink"], cx["cx-bg"], 4.5), ("cx muted / card", cx["cx-muted"], cx["cx-card"], 4.5),
        ("cx button", cx["accent-ink"], cx["accent"], 4.5), ("cx accent text / card", cx["accent"], cx["cx-card"], 4.5),
    ]
    out, bad = [], 0
    for label, fg, bg, need in rows:
        c = contrast(fg, bg)
        ok = c >= need
        bad += not ok
        out.append(f"  {'ok  ' if ok else 'FAIL'} {label:30s} {c:5.2f} (need {need})")
    return bad, out


def css_block(sel, tokens, scheme=None):
    lines = [f"{sel} {{"]
    if scheme:
        lines.append(f"  color-scheme: {scheme};")
    lines += [f"  --{k}: {v};" for k, v in tokens.items()]
    return "\n".join(lines) + "\n}\n"


def main():
    dark = ", ".join(n for n, p in PALETTES.items() if p["mode"] == "dark")
    css = ["/* Industry themes for the Top Shelf CRM kit. GENERATED by make_themes.py: edit the palettes there, then rerun.\n"
           "   Load after kit.css. Staff pages: <body class=\"t-<industry>\">. Customer pages: <body class=\"cx t-<industry>\">.\n"
           f"   Dark themes: {dark}. Light: the rest.\n"
           "   Customer pages use the paired website's fonts where a theme sets them; staff pages keep Figtree. */\n",
           fonts_import(),
           "body.cx :is(h1, h2, h3, .cx-name) { font-family: var(--font-head, var(--font)); }\n"]
    fails = 0
    for name, p in PALETTES.items():
        t, cx, sc = build(name, p)
        bad, report = checks(name, p, t, cx, sc)
        fails += bad
        print(f"{name} ({p['mode']}): {'all pass' if not bad else str(bad) + ' FAIL'}")
        for r in report:
            if "FAIL" in r or "-v" in sys.argv:
                print(r)
        css.append(f"\n/* ---- {name} · {p['mode']} · chrome {p['side']} · accent {p['accent']} · button {p['grad'][1]} ---- */\n")
        css.append(css_block(f"body.t-{name}", t, "dark" if p["mode"] == "dark" else "light"))
        css.append(css_block(f"body.cx.t-{name}", cx))
    Path(__file__).with_name("themes.css").write_text("".join(css), encoding="utf-8")
    print("wrote themes.css;", "contrast OK" if not fails else f"{fails} contrast failures")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
