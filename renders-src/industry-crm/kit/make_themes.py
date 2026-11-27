"""Generate themes.css (one body.t-<industry> class per industry) and check WCAG contrast.

  python make_themes.py          writes themes.css, prints the contrast report, exits 1 if any check fails

Edit the PALETTES below, not themes.css. Each palette names a handful of key colors; everything
else (brand scale, lines, tints, semantic colors, customer-page tokens) is derived here so the
11 themes stay consistent. Chrome (sidebar / band / bars / tab bar) is always dark with light text.
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
PALETTES = {
    "home-services": dict(mode="light", canvas="#f7faf8", panel="#ffffff", side="#1f6e4a", accent="#2e9e6a",
        ink="#111827", ink2="#374151", muted="#4b5563", muted2="#6b7280", faint="#9ca3af",
        grad=("#38a06c", "#23825a", "#1a6a47"), on_accent="#ffffff", nav_ink="#ffffff",
        cx_accent="#1f6e4a", cx_ink="#ffffff", keep_scale=True),
    "car-lots": dict(mode="dark", canvas="#111113", panel="#1a1a1d", side="#09090a", accent="#c9a34e",
        ink="#f4efe4", ink2="#ddd6c8", muted="#aca596", muted2="#938c7f", faint="#6b665d",
        grad=("#e3c378", "#c9a34e", "#a9873b"), on_accent="#17130a", edge="rgb(201 163 78 / .35)",
        cx_accent="#c9a34e", cx_ink="#17130a"),
    "auto-repair": dict(mode="dark", canvas="#1b2026", panel="#242a31", side="#13171b", accent="#f26b1d",
        ink="#eef1f4", ink2="#cfd5dc", muted="#a5aeb9", muted2="#8d97a3", faint="#66707c",
        grad=("#ff8f45", "#f26b1d", "#d9580f"), on_accent="#1a0d04", edge="rgb(242 107 29 / .45)", bar="#333c46",
        cx_accent="#f26b1d", cx_ink="#1a0d04"),
    "auto-detailing": dict(mode="dark", canvas="#07090d", panel="#0f131a", side="#030406", accent="#3b8eff",
        ink="#eaf0f7", ink2="#cbd5e1", muted="#9aa7b8", muted2="#8290a3", faint="#55637a",
        grad=("#3f87f2", "#2563eb", "#1d4ed8"), on_accent="#ffffff", edge="rgb(59 142 255 / .35)",
        cx_accent="#4f9cff", cx_ink="#04101f"),
    "fitness": dict(mode="dark", canvas="#161719", panel="#202124", side="#0e0f10", accent="#e0702e",
        ink="#f2f2f0", ink2="#d6d6d2", muted="#a9a9a4", muted2="#91918c", faint="#666662",
        grad=("#f08a45", "#e0702e", "#c95e1f"), on_accent="#180a03", edge="rgb(224 112 46 / .4)",
        cx_accent="#e0702e", cx_ink="#180a03"),
    "restaurants": dict(mode="dark", canvas="#17110f", panel="#221a17", side="#100b0a", accent="#c49a5a",
        ink="#f4ebe3", ink2="#dccfc3", muted="#b5a79a", muted2="#9b8c80", faint="#6e6158",
        grad=("#a8434a", "#8a2b31", "#6e1f25"), on_accent="#fbf1ea", edge="rgb(196 154 90 / .35)",
        bar="#5e1f25", bubble=("#6e242a", "#fbf1ea"), cx_accent="#c49a5a", cx_ink="#1a110c",
        cx_logo=("#8a2b31", "#f3d9a8")),
    "real-estate": dict(mode="light", canvas="#f8f5ee", panel="#fffefa", side="#24493b", band="#2e5c4a", accent="#3f7a63",
        ink="#1d2722", ink2="#38443e", muted="#525e57", muted2="#66716a", faint="#a3aaa3",
        grad=("#47826a", "#2e5c4a", "#244a3b"), on_accent="#ffffff", nav_ink="#ecd8ae", edge="rgb(176 138 78 / .85)",
        cx_accent="#2e5c4a", cx_ink="#ffffff"),
    "salon-spa": dict(mode="light", canvas="#fbf5f3", panel="#fffdfc", side="#4b2843", accent="#9b5a86",
        ink="#2a1f27", ink2="#44363f", muted="#5e5059", muted2="#74656e", faint="#b0a3ab",
        grad=("#a8679a", "#8a4c78", "#6f3c61"), on_accent="#ffffff", nav_ink="#f7dcec",
        cx_accent="#8a4c78", cx_ink="#ffffff"),
    "medical-dental": dict(mode="light", canvas="#f3f7f9", panel="#ffffff", side="#1e3a55", accent="#14928f",
        ink="#12202c", ink2="#2f3e4c", muted="#4a5866", muted2="#5f6d7b", faint="#a0abb6",
        grad=("#1b9d99", "#11797a", "#0d6264"), on_accent="#ffffff", nav_ink="#c9f1ee",
        cx_accent="#11797a", cx_ink="#ffffff"),
    "legal": dict(mode="light", canvas="#f6f2e9", panel="#fffdf8", side="#1b2741", accent="#3b5687",
        ink="#1c2230", ink2="#363d4c", muted="#51586a", muted2="#666c7b", faint="#a9a9a6",
        grad=("#3c5888", "#2a4170", "#1e3157"), on_accent="#ffffff", nav_ink="#ead9b0", edge="rgb(168 138 78 / .85)",
        cx_accent="#1e2b4a", cx_ink="#ffffff"),
    "retail": dict(mode="light", canvas="#fbf6ef", panel="#fffdf9", side="#7a3a25", accent="#c0643e",
        ink="#2b1e18", ink2="#47362e", muted="#5f5048", muted2="#75655c", faint="#b3a59b",
        grad=("#c86a43", "#a84d2a", "#8c3f22"), on_accent="#ffffff", nav_ink="#ffe1cf",
        cx_accent="#a84d2a", cx_ink="#ffffff"),
}


def scale(p):
    a = p["accent"]
    if p["mode"] == "light":
        lo = [(50, .10), (100, .20), (200, .35), (300, .52), (400, .75)]
        out = {k: mix(a, "#ffffff", t) for k, t in lo}
        out[500] = a
        out.update({k: mix("#000000", a, t) for k, t in [(600, .14), (700, .28), (800, .42), (900, .55), (950, .70)]})
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
    if not p.get("keep_scale"):
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
        ("b-600 text / panel", sc[600] if not p.get("keep_scale") else "#28885b", panel, 4.5 if not p.get("keep_scale") else 4.0),
        ("b-700 on brand chip", sc[700] if not p.get("keep_scale") else "#21724c", mix(p["accent"], panel, .15), 4.5),
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
    css = ["/* Industry themes for the Top Shelf CRM kit. GENERATED by make_themes.py: edit the palettes there, then rerun.\n"
           "   Load after kit.css. Staff pages: <body class=\"t-<industry>\">. Customer pages: <body class=\"cx t-<industry>\">.\n"
           "   Dark themes: car-lots, auto-repair, auto-detailing, fitness, restaurants. Light: the rest. */\n"]
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
