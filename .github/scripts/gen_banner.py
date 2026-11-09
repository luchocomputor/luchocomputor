"""Bannière animée du profil GitHub : 4 traces EEG synthétiques qui défilent en boucle."""
import numpy as np
from pathlib import Path

OUT = Path(__file__).parents[2] / "assets"
W, H = 1200, 240          # taille de la bannière
P = 1200                  # période de la boucle (px) = largeur d'une copie du tracé
N = 600                   # points par période
rng = np.random.default_rng(7)

def trace(alpha_amp, seed):
    """Signal périodique sur P : bruit 1/f à phases aléatoires + rythme alpha modulé."""
    r = np.random.default_rng(seed)
    t = np.arange(N) / N
    k = np.arange(1, 160)
    amp = 1 / k**0.9
    ph = r.uniform(0, 2 * np.pi, k.size)
    x = (amp[:, None] * np.sin(2 * np.pi * k[:, None] * t + ph[:, None])).sum(0)
    # bouffées alpha : porteuse à 42 cycles par période, enveloppe lente
    env = 0.5 + 0.5 * np.sin(2 * np.pi * 3 * t + r.uniform(0, 6.28))
    x += alpha_amp * env**3 * np.sin(2 * np.pi * 42 * t + r.uniform(0, 6.28))
    return x / np.abs(x).max()

def path(y0, a, x):
    xs = np.linspace(0, 2 * P, 2 * N + 1)
    ys = np.concatenate([x, x, x[:1]])
    pts = " ".join(f"{u:.1f},{y0 - a * v:.1f}" for u, v in zip(xs, ys))
    return f"M{pts.replace(' ', ' L', 1)}" if False else "M" + " L".join(pts.split(" "))

CH = [(70, 1.2, 11), (115, 2.2, 23), (160, 0.8, 5), (205, 1.6, 41)]

def svg(dark):
    fg = "#e6edf3" if dark else "#1f2328"
    mut = "#8b949e" if dark else "#656d76"
    line = "#30363d" if dark else "#d0d7de"
    acc = "#58a6ff" if dark else "#0969da"
    traces = []
    for i, (y0, aa, s) in enumerate(CH):
        x = trace(aa, s)
        col = acc if i == 1 else line
        op = 0.95 if i == 1 else 0.9
        dur = 26 + 4 * i
        traces.append(
            f'<g class="t" style="animation-duration:{dur}s"><path d="{path(y0, 21, x)}" '
            f'fill="none" stroke="{col}" stroke-opacity="{op}" stroke-width="{1.6 if i == 1 else 1.2}" '
            f'stroke-linejoin="round"/></g>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
.t {{ animation: scroll linear infinite; }}
@keyframes scroll {{ from {{ transform: translateX(0); }} to {{ transform: translateX(-{P}px); }} }}
@media (prefers-reduced-motion: reduce) {{ .t {{ animation: none; }} }}
text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
</style>
<defs>
  <linearGradient id="fade" x1="0" x2="1">
    <stop offset="0" stop-color="#fff" stop-opacity="0"/>
    <stop offset="0.3" stop-color="#fff" stop-opacity="0"/>
    <stop offset="0.45" stop-color="#fff" stop-opacity="0.35"/>
    <stop offset="0.68" stop-color="#fff" stop-opacity="1"/>
    <stop offset="1" stop-color="#fff" stop-opacity="1"/>
  </linearGradient>
  <mask id="m"><rect width="{W}" height="{H}" fill="url(#fade)"/></mask>
</defs>
<g mask="url(#m)">{"".join(traces)}</g>
<text x="0" y="112" font-size="58" font-weight="650" fill="{fg}" letter-spacing="-0.5">Louis Almairac</text>
<text x="2" y="152" font-size="25" fill="{mut}">Machine learning for time series and EEG</text>
<text x="2" y="186" font-size="20" fill="{mut}">MVA, ENS Paris-Saclay · École des Ponts</text>
</svg>
'''

for name, dark in [("banner-light.svg", False), ("banner-dark.svg", True)]:
    (OUT / name).write_text(svg(dark))
    print(name, (OUT / name).stat().st_size)
