"""Entry titles of the profile README: serif title + small-caps context line, light and dark."""
from html import escape
from pathlib import Path

OUT = Path(__file__).parents[2] / "assets" / "titles"
SERIF = "'Iowan Old Style', Charter, 'Bitstream Charter', 'Sitka Text', Cambria, Georgia, serif"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
PAL = {"light": ("#1f2328", "#656d76", "#0969da"), "dark": ("#e6edf3", "#8b949e", "#58a6ff")}

ENTRIES = {
    "uqam": ("Can EEG tell when a player is in the zone?", ["UQAM, Montréal", "Research internship", "2026"], None),
    "granger": ("How do brain regions drive each other during sleep?", ["École des Ponts", "With CNRS and Max Planck researchers", "2024-25"], "Repo"),
    "challenge": ("EEG/EMG Foundation Challenge 2026: EEG-to-Image", ["Meta, Muse and Yneuro", "In progress"], None),
    "qrt": ("QRT Data Challenge 2025", ["QRT and Institut Gustave Roussy", "2025"], "Repo"),
    "martha": ("Martha", ["Personal project", "iOS", "2025-26"], "Repo"),
    "cdc": ("Caisse des Dépôts", ["Machine learning intern", "Paris", "2025"], None),
    "sopra": ("Sopra Steria", ["Data science intern", "Paris", "2024"], None),
}

def svg(title, ctx, link, theme):
    fg, mut, acc = PAL[theme]
    sep = '<tspan dx="7">·</tspan><tspan dx="7">'
    parts = [escape(c if c == "iOS" else c.upper()) for c in ctx]
    line = parts[0] + "".join(f'{sep}{p}</tspan>' for p in parts[1:])
    if link:
        line += f'<tspan dx="7">·</tspan><tspan dx="7" fill="{acc}">{escape(link.upper())} ↗</tspan>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="790" height="58" viewBox="0 0 790 58">
<text x="0" y="27" font-family="{SERIF}" font-size="25" font-weight="600" fill="{fg}">{escape(title)}</text>
<text x="1" y="50" font-family="{SANS}" font-size="11.5" letter-spacing="0.9" fill="{mut}">{line}</text>
</svg>
'''

OUT.mkdir(parents=True, exist_ok=True)
for key, (title, ctx, link) in ENTRIES.items():
    for theme in PAL:
        (OUT / f"{key}-{theme}.svg").write_text(svg(title, ctx, link, theme))
print(len(ENTRIES), "titles")
