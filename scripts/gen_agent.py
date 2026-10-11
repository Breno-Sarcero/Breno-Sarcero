"""Gera assets/agent.svg: mascote pixel art trabalhando como agente, em loop."""
import sys
from html import escape

OUT = sys.argv[1]
W, H = 820, 280
U = 14                            # tamanho do "pixel" do mascote
MX, MY = 40, 66                   # canto do mascote
DUR = 9                           # duração do loop em segundos

BG, FG, DIM, AMBER, GREEN, ORANGE = "#1c1917", "#e7e5e4", "#a8a29e", "#f59e0b", "#86efac", "#d97757"
FONT = "'JetBrains Mono','Cascadia Code',Consolas,'DejaVu Sans Mono',monospace"

STEPS = [
    "Lendo dados do ERP via API",
    "Conciliando lançamentos",
    "Validando no SQL Server",
    "Abrindo PR para revisão",
]


def px(c, r, w=1, h=1, fill=ORANGE):
    return f'<rect x="{MX + c * U}" y="{MY + r * U}" width="{w * U}" height="{h * U}" fill="{fill}"/>'


def show(start, end=0.95):
    """Opacidade: aparece em `start` e some em `end` (frações do loop)."""
    return (f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{start:.3f};{end:.3f}" '
            f'calcMode="discrete" dur="{DUR}s" repeatCount="indefinite"/>')


def text(x, y, s, color, size=15, extra=""):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}"{extra}>{escape(s)}</text>'


DONE = 0.12 + len(STEPS) * 0.15   # momento em que todas as etapas terminaram

# ---------- mascote ----------
body = px(2, 0, 12, 8) + px(0, 4, 16, 2)
legs_a = px(3, 8, 1, 2) + px(10, 8, 1, 2)
legs_b = px(5, 8, 1, 2) + px(12, 8, 1, 2)
eyes_open = (f'<g>{px(4, 2, 1, 2, BG)}{px(11, 2, 1, 2, BG)}'
             f'<animate attributeName="opacity" values="1;0;1" keyTimes="0;{DONE:.3f};0.97" '
             f'calcMode="discrete" dur="{DUR}s" repeatCount="indefinite"/></g>')
h = U / 2


def chev(cx, d):
    """Olho "> <" como traço grosso, igual ao sticker."""
    x0, x1, y = MX + cx * U - d * U * 0.6, MX + cx * U + d * U * 0.6, MY + 3 * U
    return (f'<polyline points="{x0},{y - U} {x1},{y} {x0},{y + U}" fill="none" stroke="{BG}" '
            f'stroke-width="{U * 0.55}" stroke-linejoin="miter" stroke-linecap="square"/>')


eyes_happy = f'<g opacity="0">{chev(4.5, 1)}{chev(11.5, -1)}{show(DONE, 0.97)}</g>'
# patas alternam, como um passinho no lugar
walk = lambda begin: (f'<animateTransform attributeName="transform" type="translate" values="0 0;0 -{h}" '
                      f'calcMode="discrete" dur="0.6s" begin="{begin}" repeatCount="indefinite"/>')
# no fim, dois pulinhos de comemoração
d = DONE
hop = (f'<animateTransform attributeName="transform" type="translate" '
       f'values="0 0;0 -{U};0 0;0 -{U};0 0" keyTimes="0;{d + .01:.3f};{d + .04:.3f};{d + .07:.3f};{d + .10:.3f}" '
       f'calcMode="discrete" dur="{DUR}s" repeatCount="indefinite"/>')
mascot = (f'<g>{hop}{body}{eyes_open}{eyes_happy}'
          f'<g>{legs_a}{walk("0s")}</g><g>{legs_b}{walk("0.3s")}</g></g>')
shadow = f'<ellipse cx="{MX + 8 * U}" cy="{MY + 10 * U + 8}" rx="{7 * U}" ry="5" fill="#0c0a09" opacity=".7"/>'

# ---------- terminal do agente ----------
TX, TY, LH = 310, 58, 32
lines = [text(TX, TY, "$ claude", AMBER, extra=' font-weight="700"')
         + text(TX + 92, TY, '"fecha o mês do cliente"', FG)]
for i, s in enumerate(STEPS):
    y = TY + (i + 1) * LH + 8
    t0 = 0.12 + i * 0.15
    lines.append(f'<g opacity="0">{text(TX, y, "●", AMBER)}{text(TX + 22, y, s + "…", DIM)}{show(t0)}</g>')
    lines.append(f'<g opacity="0">{text(TX + 330, y, "✓", GREEN, extra=" font-weight=\"700\"")}{show(t0 + 0.12)}</g>')
y = TY + (len(STEPS) + 1) * LH + 22
lines.append(f'<g opacity="0">{text(TX, y, "✓ pronto · automação agêntica com IA", GREEN, 15, " font-weight=\"700\"")}{show(DONE)}</g>')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}" role="img" aria-label="Mascote pixel art executando uma automação agêntica com IA">
<defs><pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#44403c"/></pattern></defs>
<rect width="{W}" height="{H}" rx="12" fill="{BG}"/>
<rect width="{W}" height="{H}" rx="12" fill="url(#dots)" opacity=".55"/>
{shadow}
{mascot}
{chr(10).join(lines)}
</svg>
'''
open(OUT, "w", encoding="utf-8").write(svg)
print("ok")
