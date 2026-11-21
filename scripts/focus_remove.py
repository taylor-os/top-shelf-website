"""Remove the retired pages and keep every old address working. Re-runnable.

- deletes every file in focus_catalog.REMOVED (git rm)
- drops the generated page specs that would rebuild them
- drops list links to them, unwraps inline links to them (pages and sources)
- strips the one-time wiring blocks wire_one_time.py added
- writes the 301 block in .htaccess
"""
import ast
import os
import re
import subprocess

import focus_catalog as cat

BEGIN, END = "# BEGIN crm-website-focus", "# END crm-website-focus"
ONE_TIME_MARK = "<!-- one-time-links -->"


def removed_slugs():
    return {p.rsplit(".", 1)[0] for p in cat.REMOVED}


def link_res():
    names = "|".join(re.escape(p) for p in sorted(cat.REMOVED, key=len, reverse=True))
    li = re.compile(r'[ \t]*<li><a href="(?:%s)"[^>]*>.*?</a></li>[ \t]*\r?\n?' % names)
    inline = re.compile(r'<a\b[^>]*\bhref="(?:%s)(?:#[^"]*)?"[^>]*>(.*?)</a>' % names, re.S)
    return li, inline


def clean_html(text):
    li, inline = link_res()
    text = re.sub(re.escape(ONE_TIME_MARK) + r".*?</section>\s*", "", text, flags=re.S)
    text = li.sub("", text)
    return inline.sub(r"\1", text)


def drop_spec_pages(src):
    """Remove dict elements of SPECS-style lists whose "slug" is a removed page."""
    tree = ast.parse(src)
    spans = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            for k, v in zip(node.keys, node.values):
                if (isinstance(k, ast.Constant) and k.value == "slug" and isinstance(v, ast.Constant)
                        and v.value in removed_slugs()):
                    spans.append((node.lineno, node.end_lineno, node.col_offset, node.end_col_offset))
    lines = src.splitlines(keepends=True)
    for start, end, c0, c1 in sorted(spans, reverse=True):
        tail = lines[end - 1][c1:]
        tail = tail[1:] if tail.startswith(",") else tail
        head = lines[start - 1][:c0]
        joined = head + tail if (head.strip() or tail.strip()) else ""
        lines[start - 1:end] = [joined] if joined else []
    return "".join(lines)


def clean_source(src):
    names = "|".join(re.escape(p) for p in sorted(cat.REMOVED, key=len, reverse=True))
    src = drop_spec_pages(src)
    # related-link tuples: ("marketing-for-x.html", "label"),
    src = re.sub(r'[ \t]*\("(?:%s)", "[^"]*"\),?[ \t]*\r?\n' % names, "", src)
    # a bridge pointing at a removed page now points at its redirect target
    for path, target in cat.REMOVED.items():
        slug, tslug = path.rsplit(".", 1)[0], target.split("#")[0].rsplit(".", 1)[0]
        src = re.sub(r'(["\'])%s\1' % re.escape(slug), r"\g<1>%s\g<1>" % tslug, src)
    return clean_html(src)


def redirect_rules():
    rules = []
    fam = {p: t for p, t in cat.REMOVED.items() if p.startswith("marketing-for-")}
    if fam and all(t == "for-" + p[len("marketing-for-"):] for p, t in fam.items()):
        rules.append(r"RedirectMatch 301 ^/marketing-for-(.+)\.html$ /for-$1.html")
    for p, t in cat.REMOVED.items():
        if p not in fam:
            rules.append("Redirect 301 /%s /%s" % (p, t))
    return rules


def write_htaccess():
    path = os.path.join(cat.ROOT, ".htaccess")
    text = open(path, encoding="utf-8").read()
    text = re.sub(r"\n?%s.*?%s\n?" % (re.escape(BEGIN), re.escape(END)), "\n", text, flags=re.S).rstrip("\n")
    block = [BEGIN,
             "# 2026-11-21: the site now sells only the Signature plan and the website.",
             "# These pages were removed; this host never deletes files on deploy, so each",
             "# old address 301s to its closest surviving page.",
             *redirect_rules(), END]
    open(path, "w", encoding="utf-8", newline="\n").write(text + "\n\n" + "\n".join(block) + "\n")


def main():
    gone = [p for p in cat.REMOVED if os.path.exists(os.path.join(cat.ROOT, p))]
    if gone:
        subprocess.run(["git", "rm", "-q", *gone], cwd=cat.ROOT, check=True)
    for page in cat.site_pages():
        s = open(page, encoding="utf-8").read()
        t = clean_html(s)
        if t != s:
            open(page, "w", encoding="utf-8", newline="").write(t)
    for src in cat.source_files():
        s = open(src, encoding="utf-8").read()
        t = clean_source(s)
        if t != s:
            open(src, "w", encoding="utf-8", newline="").write(t)
    write_htaccess()


if __name__ == "__main__":
    main()
