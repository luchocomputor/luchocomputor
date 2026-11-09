"""Illustrations du README : pipeline UQAM et Granger pendant le sommeil (clair et sombre)."""
import numpy as np
from pathlib import Path

OUT = Path(__file__).parents[2] / "assets"
FONT = '-apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif'
PAL = {
    "light": dict(fg="#1f2328", mut="#656d76", line="#d0d7de", soft="#eff2f5", acc="#0969da", bg="#ffffff"),
    "dark": dict(fg="#e6edf3", mut="#8b949e", line="#30363d", soft="#161b22", acc="#58a6ff", bg="#0d1117"),
}

def pts(xs, ys):
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in zip(xs, ys))

def eeg(n, seed, alpha=1.0):
    r = np.random.default_rng(seed)
    t = np.arange(n) / n
    k = np.arange(1, 60)
    x = ((1 / k ** 0.9)[:, None] * np.sin(2 * np.pi * k[:, None] * t + r.uniform(0, 6.3, k.size)[:, None])).sum(0)
    x += alpha * (0.5 + 0.5 * np.sin(2 * np.pi * 2 * t)) ** 3 * np.sin(2 * np.pi * 24 * t)
    return x / np.abs(x).max()

# ---------------------------------------------------------------- UQAM
def uqam(p):
    W, H = 420, 360
    o = []
    # bloc EEG : 4 traces qui défilent dans une fenêtre
    o.append(f'<rect x="10" y="10" width="400" height="78" rx="10" fill="{p["soft"]}"/>')
    o.append('<clipPath id="cw"><rect x="70" y="14" width="332" height="70"/></clipPath>')
    o.append(f'<text x="22" y="40" class="b">EEG</text><text x="22" y="56" class="s">16 ch.</text><text x="22" y="70" class="s">26 players</text>')
    tr = []
    for i in range(4):
        x = eeg(240, 3 + i, 1.2 if i == 1 else 0.6)
        xs = np.linspace(0, 664, 481)
        ys = 26 + i * 16 - 6 * np.concatenate([x, x, x[:1]])
        col = p["acc"] if i == 1 else p["mut"]
        tr.append(f'<path d="{pts(xs, ys)}" fill="none" stroke="{col}" stroke-width="{1.4 if i == 1 else 1}" stroke-opacity="{1 if i == 1 else .6}"/>')
    o.append(f'<g clip-path="url(#cw)"><g transform="translate(70 0)"><g class="scroll">{"".join(tr)}</g></g></g>')
    # flèche
    def arrow(x1, y1, x2, y2, dly=0):
        d = f"M{x1},{y1} L{x2},{y2}"
        return (f'<path d="{d}" stroke="{p["line"]}" stroke-width="1.5" fill="none" marker-end="url(#ah)"/>'
                f'<circle r="2.6" fill="{p["acc"]}"><animateMotion dur="2.4s" begin="0s" repeatCount="indefinite" path="{d}"/></circle>')
    o.append(arrow(210, 90, 210, 112))
    # MEMD : 6 modes alignés, de la plus rapide à la plus lente
    o.append(f'<rect x="10" y="116" width="400" height="76" rx="10" fill="{p["soft"]}"/>')
    o.append(f'<text x="22" y="146" class="b">MEMD</text><text x="22" y="162" class="s">6 joint</text><text x="22" y="176" class="s">modes</text>')
    xs = np.linspace(82, 398, 300)
    for k in range(6):
        f = [26, 15, 9, 5, 3, 1.6][k]
        ys = 126 + k * 11 - 3.6 * np.sin(2 * np.pi * f * (xs - 82) / 316) * (0.6 + 0.4 * np.sin(np.pi * (xs - 82) / 316))
        o.append(f'<path d="{pts(xs, ys)}" fill="none" stroke="{p["acc"]}" stroke-opacity="{1 - k * .12:.2f}" stroke-width="1.1"/>')
    o.append(arrow(150, 194, 110, 216, .4) + arrow(270, 194, 310, 216, .4))
    # deux branches
    o.append(f'<rect x="10" y="220" width="195" height="80" rx="10" fill="{p["soft"]}"/>')
    o.append(f'<rect x="215" y="220" width="195" height="80" rx="10" fill="{p["soft"]}"/>')
    o.append(f'<text x="22" y="240" class="b">Wigner-Ville</text><text x="22" y="254" class="s">band energies</text>')
    r = np.random.default_rng(1)
    for i in range(6):
        for j in range(5):
            v = r.uniform(.15, 1)
            o.append(f'<rect x="{128 + j * 14}" y="{230 + i * 11}" width="12" height="9" rx="2" fill="{p["acc"]}" fill-opacity="{v:.2f}"/>')
    o.append(f'<text x="227" y="240" class="b">Riemannian</text><text x="227" y="254" class="s">tangent space</text>')
    # variété courbe + plan tangent
    o.append(f'<path d="M318,292 Q352,236 398,262" fill="none" stroke="{p["mut"]}" stroke-width="1.3"/>')
    o.append(f'<path d="M318,250 L398,244" fill="none" stroke="{p["acc"]}" stroke-width="1.3" stroke-dasharray="3 3"/>')
    for (cx, cy) in [(336, 266), (350, 258), (366, 256), (382, 259)]:
        o.append(f'<circle cx="{cx}" cy="{cy}" r="2.6" fill="{p["acc"]}"/>')
    o.append(f'<circle cx="356" cy="247" r="3.4" fill="none" stroke="{p["fg"]}" stroke-width="1.2"/>')
    o.append(arrow(110, 302, 180, 322, .8) + arrow(310, 302, 240, 322, .8))
    # sortie
    o.append(f'<rect x="120" y="326" width="180" height="28" rx="14" fill="{p["acc"]}"/>')
    o.append(f'<text x="210" y="344" text-anchor="middle" class="w">SVM · F1 = 0.76</text>')
    style = f"""text {{ font-family: {FONT}; }}
.b {{ font-size: 13px; font-weight: 600; fill: {p["fg"]}; }}
.s {{ font-size: 11px; fill: {p["mut"]}; }}
.w {{ font-size: 12px; font-weight: 600; fill: {p["bg"]}; }}
.scroll {{ animation: sc 14s linear infinite; }}
@keyframes sc {{ from {{ transform: translateX(0); }} to {{ transform: translateX(-332px); }} }}
@media (prefers-reduced-motion: reduce) {{ .scroll {{ animation: none; }} }}"""
    return W, H, style, "".join(o)

# ---------------------------------------------------------------- Granger
STAGES = ["W", "N1", "N2", "N3", "N2", "REM", "N2", "W"]
LEVEL = {"W": 0, "REM": 1, "N1": 2, "N2": 3, "N3": 4}

def granger(p):
    W, H = 380, 330
    o = []
    cx, cy, R = 190, 120, 100
    el = {"F3": (-38, -48), "F4": (38, -48), "C3": (-58, 4), "C4": (58, 4), "O1": (-30, 66), "O2": (30, 66)}
    el = {k: (cx + x, cy + y) for k, (x, y) in el.items()}
    # tête vue de dessus
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{p["soft"]}" stroke="{p["line"]}" stroke-width="1.5"/>')
    o.append(f'<path d="M{cx - 12},{cy - R + 1} L{cx},{cy - R - 14} L{cx + 12},{cy - R + 1}" fill="{p["soft"]}" stroke="{p["line"]}" stroke-width="1.5"/>')
    for s in (-1, 1):
        o.append(f'<path d="M{cx + s * R},{cy - 16} q{s * 12},16 0,32" fill="{p["soft"]}" stroke="{p["line"]}" stroke-width="1.5"/>')
    # liens orientés, dont l'intensité suit le stade de sommeil
    links = [("F3", "C3"), ("F4", "C4"), ("C3", "O1"), ("C4", "O2"), ("O1", "F3"), ("O2", "F4"), ("C3", "C4"), ("F4", "F3")]
    r = np.random.default_rng(5)
    base = {s: r.uniform(0.05, 1, len(links)) for s in LEVEL}
    base["N3"][[0, 1, 4, 5]] = [1, .95, .9, .85]   # sommeil profond : couplages forts
    base["W"][:] = r.uniform(.05, .35, len(links))
    n = len(STAGES)
    for j, (a, b) in enumerate(links):
        (x1, y1), (x2, y2) = el[a], el[b]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        nx, ny = -(y2 - y1), (x2 - x1)
        L = (nx ** 2 + ny ** 2) ** .5
        qx, qy = mx + 14 * nx / L, my + 14 * ny / L
        # raccourcir pour ne pas mordre les électrodes
        def sh(x0, y0, x3, y3, d=11):
            vx, vy = x3 - x0, y3 - y0
            l = (vx ** 2 + vy ** 2) ** .5
            return x0 + d * vx / l, y0 + d * vy / l
        sx, sy = sh(x1, y1, qx, qy)
        ex, ey = sh(x2, y2, qx, qy, 14)
        kf = []
        for i, s in enumerate(STAGES):
            v = base[s][j]
            a0, a1 = 100 * i / n, 100 * (i + 1) / n
            kf.append(f"{a0 + .01:.2f}%, {a1 - 1.5:.2f}% {{ stroke-opacity: {.12 + .88 * v:.2f}; stroke-width: {1 + 2.4 * v:.2f}px; }}")
        kf.append(f"100% {{ stroke-opacity: {.12 + .88 * base[STAGES[0]][j]:.2f}; stroke-width: {1 + 2.4 * base[STAGES[0]][j]:.2f}px; }}")
        o.append(f'<style>@keyframes k{j} {{ {" ".join(kf)} }} .k{j} {{ animation: k{j} 12s ease-in-out infinite; }}</style>')
        o.append(f'<path class="k{j}" d="M{sx:.1f},{sy:.1f} Q{qx:.1f},{qy:.1f} {ex:.1f},{ey:.1f}" fill="none" '
                 f'stroke="{p["acc"]}" stroke-width="1.6" stroke-opacity=".5" stroke-linecap="round" marker-end="url(#ah2)"/>')
    for k, (x, y) in el.items():
        o.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{p["bg"]}" stroke="{p["fg"]}" stroke-width="1.3"/>')
        o.append(f'<text x="{x}" y="{y + 3.5}" text-anchor="middle" class="e">{k}</text>')
    # hypnogramme
    x0, x1, y0, dy = 46, 366, 248, 14
    for s, lv in [("W", 0), ("REM", 1), ("N1", 2), ("N2", 3), ("N3", 4)]:
        o.append(f'<text x="{x0 - 8}" y="{y0 + lv * dy + 4}" text-anchor="end" class="s">{s}</text>')
        o.append(f'<line x1="{x0}" x2="{x1}" y1="{y0 + lv * dy}" y2="{y0 + lv * dy}" stroke="{p["line"]}" stroke-width=".6"/>')
    seg = (x1 - x0) / n
    d = []
    for i, s in enumerate(STAGES):
        y = y0 + LEVEL[s] * dy
        d.append(f"{'M' if i == 0 else 'L'}{x0 + i * seg:.1f},{y} L{x0 + (i + 1) * seg:.1f},{y}")
    o.append(f'<path d="{" ".join(d)}" fill="none" stroke="{p["fg"]}" stroke-width="1.6"/>')
    o.append(f'<rect class="cur" x="{x0}" y="{y0 - 8}" width="{seg:.1f}" height="{4 * dy + 16}" rx="4" fill="{p["acc"]}" fill-opacity=".14"/>')
    o.append(f'<text x="{x1}" y="{H - 4}" text-anchor="end" class="s">one night, schematic</text>')
    style = f"""text {{ font-family: {FONT}; }}
.e {{ font-size: 8.5px; font-weight: 600; fill: {p["fg"]}; }}
.s {{ font-size: 10.5px; fill: {p["mut"]}; }}
.cur {{ animation: cur 12s steps({n}, end) infinite; }}
@keyframes cur {{ from {{ transform: translateX(0); }} to {{ transform: translateX({seg * n:.1f}px); }} }}
@media (prefers-reduced-motion: reduce) {{ .cur, [class^=k] {{ animation: none; }} }}"""
    return W, H, style, "".join(o)

def write(name, fn):
    for theme, p in PAL.items():
        W, H, style, body = fn(p)
        defs = (f'<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
                f'<path d="M0,1 L9,5 L0,9 z" fill="{p["line"]}"/></marker>'
                f'<marker id="ah2" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto">'
                f'<path d="M0,1 L9,5 L0,9 z" fill="{p["acc"]}"/></marker></defs>')
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><style>{style}</style>{defs}{body}</svg>\n'
        (OUT / f"{name}-{theme}.svg").write_text(svg)

OUT.mkdir(parents=True, exist_ok=True)
write("uqam", uqam)
write("granger", granger)
print("ok")
