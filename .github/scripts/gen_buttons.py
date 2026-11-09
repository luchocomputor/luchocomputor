"""Small pill buttons (icon + label) for the profile README, light and dark."""
from pathlib import Path

OUT = Path(__file__).parents[2] / "assets" / "buttons"
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
PAL = {"light": ("#1f2328", "#d0d7de", "#f6f8fa"), "dark": ("#e6edf3", "#30363d", "#161b22")}
ICONS = {  # 16x16 strokes
    "code": "M5.5 4 L1.5 8 L5.5 12 M10.5 4 L14.5 8 L10.5 12",
    "doc": "M3.5 1.5 H10 L13 4.5 V14.5 H3.5 Z M10 1.5 V4.5 H13 M6 8 H10.5 M6 11 H10.5",
    "image": "M2 3 H14 V13 H2 Z M2 11 L6 7 L9 10 L11 8 L14 11 M10.5 5.5 h0.01",
    "link": "M6.5 3 H3 V13 H13 V9.5 M9 2.5 H13.5 V7 M13.5 2.5 L7.5 8.5",
    "mail": "M2 3.5 H14 V12.5 H2 Z M2 4 L8 9 L14 4",
    "person": "M8 8 a3 3 0 1 0 0 -6 a3 3 0 1 0 0 6 M2.5 14.5 c0.8 -3 3 -4.5 5.5 -4.5 s4.7 1.5 5.5 4.5",
}
BUTTONS = {
    "code": ("code", "Code"),
    "repo": ("code", "Repo"),
    "preprint": ("doc", "Preprint"),
    "poster": ("image", "Poster"),
    "challenge": ("link", "Challenge"),
    "cv": ("doc", "CV"),
    "linkedin": ("person", "LinkedIn"),
    "email": ("mail", "Email"),
}

def width(label):
    w = {"i": 3.5, "l": 3.5, "I": 4, " ": 3.5, "m": 11, "w": 10, "M": 11, "W": 12}
    return sum(w.get(c, 8.6 if c.isupper() else 6.8) for c in label)

def svg(icon, label, theme):
    fg, line, bg = PAL[theme]
    W = int(12 + 16 + 7 + width(label) + 13)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="30" viewBox="0 0 {W} 30">
<rect x="0.5" y="0.5" width="{W - 1}" height="29" rx="15" fill="{bg}" stroke="{line}"/>
<path transform="translate(12 7)" d="{ICONS[icon]}" fill="none" stroke="{fg}" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
<text x="35" y="19.5" font-family="{SANS}" font-size="13" font-weight="500" fill="{fg}">{label}</text>
</svg>
'''

OUT.mkdir(parents=True, exist_ok=True)
for key, (icon, label) in BUTTONS.items():
    for theme in PAL:
        (OUT / f"{key}-{theme}.svg").write_text(svg(icon, label, theme))
print(len(BUTTONS), "buttons")
