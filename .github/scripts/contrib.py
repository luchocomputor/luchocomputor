"""Contribution graph as a light and a dark SVG, in the style of the banner.

Usage: GITHUB_TOKEN=... python contrib.py <login> <out_dir>
"""
import json
import os
import sys
import urllib.request
from datetime import date
from pathlib import Path

LOGIN, OUT = sys.argv[1], Path(sys.argv[2])
QUERY = """query($login: String!) { user(login: $login) { contributionsCollection {
  contributionCalendar { totalContributions weeks { contributionDays { date contributionCount weekday } } } } } }"""

req = urllib.request.Request(
    "https://api.github.com/graphql",
    data=json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode(),
    headers={"Authorization": f"bearer {os.environ['GITHUB_TOKEN']}", "Content-Type": "application/json"},
)
cal = json.load(urllib.request.urlopen(req))["data"]["user"]["contributionsCollection"]["contributionCalendar"]
weeks = cal["weeks"]
total = cal["totalContributions"]

# Niveaux par quantiles des jours non nuls : un calendrier clairsemé reste lisible.
counts = sorted(d["contributionCount"] for w in weeks for d in w["contributionDays"] if d["contributionCount"] > 0)
def q(p):
    return counts[min(len(counts) - 1, int(p * len(counts)))] if counts else 1
cuts = [q(0.25), q(0.5), q(0.75)]
def level(n):
    if n == 0:
        return 0
    return 1 + sum(n > c for c in cuts)

THEMES = {
    "light": dict(text="#656d76", strong="#1f2328", empty="#eff2f5",
                  levels=["#cfe2fb", "#8cbcf5", "#3d8be8", "#0969da"]),
    "dark": dict(text="#8b949e", strong="#e6edf3", empty="#161b22",
                 levels=["#0c2d6b", "#1158c7", "#388bfd", "#79c0ff"]),
}
CELL, GAP, LEFT, TOP = 12, 3, 30, 28
W = LEFT + len(weeks) * (CELL + GAP) + 4
H = TOP + 7 * (CELL + GAP) + 34
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()

def svg(theme):
    t = THEMES[theme]
    cells, labels, last_month = [], [], None
    for i, w in enumerate(weeks):
        x = LEFT + i * (CELL + GAP)
        first = date.fromisoformat(w["contributionDays"][0]["date"])
        if first.month != last_month and first.day <= 7 and i < len(weeks) - 2:
            labels.append(f'<text x="{x}" y="{TOP - 9}" class="l">{MONTHS[first.month - 1]}</text>')
            last_month = first.month
        for d in w["contributionDays"]:
            y = TOP + d["weekday"] * (CELL + GAP)
            lv = level(d["contributionCount"])
            fill = t["empty"] if lv == 0 else t["levels"][lv - 1]
            n = d["contributionCount"]
            cells.append(
                f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="3" fill="{fill}"'
                + (f' class="on" style="animation-delay:{i * 0.025:.3f}s"' if lv else '') + f'><title>{n} contribution{"s" * (n != 1)} on {d["date"]}</title></rect>')
    days = ["", "Mon", "", "Wed", "", "Fri", ""]
    daylab = "".join(f'<text x="0" y="{TOP + k * (CELL + GAP) + 10}" class="l">{s}</text>' for k, s in enumerate(days) if s)
    legend_x = W - 4 - 5 * (CELL + GAP) - 64
    ly = H - 16
    legend = [f'<text x="{legend_x}" y="{ly + 10}" class="l">Less</text>']
    for k, c in enumerate([t["empty"]] + t["levels"]):
        legend.append(f'<rect x="{legend_x + 30 + k * (CELL + GAP)}" y="{ly}" width="{CELL}" height="{CELL}" rx="3" fill="{c}"/>')
    legend.append(f'<text x="{legend_x + 30 + 5 * (CELL + GAP) + 4}" y="{ly + 10}" class="l">More</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
.l {{ font-size: 11px; fill: {t["text"]}; }}
.on {{ transform-box: fill-box; transform-origin: center; animation: wave 9s ease-in-out infinite; }}
@keyframes wave {{ 0%, 8%, 100% {{ transform: scale(1); }} 4% {{ transform: scale(1.3); }} }}
@media (prefers-reduced-motion: reduce) {{ .on {{ animation: none; }} }}
</style>
{"".join(labels)}{daylab}
<g class="c">{"".join(cells)}</g>
<text x="{LEFT}" y="{ly + 10}" font-size="12" fill="{t["strong"]}"><tspan font-weight="600">{total}</tspan><tspan fill="{t["text"]}"> contributions in the last year</tspan></text>
{"".join(legend)}
</svg>
'''

OUT.mkdir(parents=True, exist_ok=True)
for theme in THEMES:
    (OUT / f"contrib-{theme}.svg").write_text(svg(theme))
print(f"{total} contributions, {len(weeks)} weeks, cuts {cuts}")
