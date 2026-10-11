import sys
from html import escape

OUT = sys.argv[1]
W, H = 820, 322
FS, CW, LH = 16, 9.6, 26          # fonte, largura do caractere, altura da linha
X0, Y0 = 28, 84                   # início do texto
TYPE = 0.07                       # segundos por caractere digitado

BG, BAR, FG, DIM, AMBER, GREEN = "#1c1917", "#292524", "#e7e5e4", "#a8a29e", "#f59e0b", "#86efac"
PROMPT = "breno@sarcero:~$"

# (comando, [(linha de saída, cor, segundos até o ✓ ou None)])
SCRIPT = [
    ('"Olá, sejam bem-vindos todos!"', [
        ("● Lendo apresentacao.md…", DIM, 1.2),
        ("Breno Sarcero · Dev Júnior de IA · cursando ADS na FMU", GREEN, None)]),
    ("cat stack.txt", [("Django · APIs · Questor ERP · SQL Server · Claude Code", DIM, None)]),
    ("echo $INTERESSES", [("automações com agentes de IA · orquestração de IA · análise de dados", DIM, None)]),
]

parts, t, y = [], 0.6, Y0


def text(x, y, s, color, extra=""):
    return (f'<text x="{x}" y="{y}" fill="{color}" textLength="{len(s) * CW:.1f}" '
            f'lengthAdjust="spacingAndGlyphs"{extra}>{escape(s)}</text>')


for i, (cmd, outs) in enumerate(SCRIPT):
    # prompt aparece
    parts.append(f'<g opacity="0"><set attributeName="opacity" to="1" begin="{t:.2f}s" fill="freeze"/>'
                 + text(X0, y, PROMPT, AMBER) + '</g>')
    cx = X0 + (len(PROMPT) + 1) * CW
    # comando digitado: clip com largura em degraus, um por caractere
    widths = ";".join(f"{k * CW:.1f}" for k in range(len(cmd) + 1))
    keys = ";".join(f"{k / len(cmd):.3f}" for k in range(len(cmd) + 1))
    dur = len(cmd) * TYPE
    parts.append(
        f'<clipPath id="c{i}"><rect x="{cx:.1f}" y="{y - 18}" height="{LH}" width="0">'
        f'<animate attributeName="width" values="{widths}" keyTimes="{keys}" calcMode="discrete" '
        f'begin="{t + 0.3:.2f}s" dur="{dur:.2f}s" fill="freeze"/></rect></clipPath>'
        + text(cx, y, cmd, FG, f' clip-path="url(#c{i})"'))
    t += 0.3 + dur + 0.35
    y += LH
    for o, color, wait in outs:
        parts.append(f'<g opacity="0"><set attributeName="opacity" to="1" begin="{t:.2f}s" fill="freeze"/>'
                     + text(X0, y, o, color) + '</g>')
        if wait:   # linha "lendo…" ganha ✓ quando termina
            t += wait
            parts.append(f'<g opacity="0"><set attributeName="opacity" to="1" begin="{t:.2f}s" fill="freeze"/>'
                         + text(X0 + (len(o) + 1) * CW, y, "✓", GREEN) + '</g>')
            t += 0.3
        y += LH
    t += 0.5
    y += 8

# prompt final com cursor piscando
parts.append(f'<g opacity="0"><set attributeName="opacity" to="1" begin="{t:.2f}s" fill="freeze"/>'
             + text(X0, y, PROMPT, AMBER)
             + f'<rect x="{X0 + (len(PROMPT) + 1) * CW:.1f}" y="{y - 15}" width="9" height="19" fill="{AMBER}">'
             f'<animate attributeName="opacity" values="1;0;1" dur="1.1s" begin="{t:.2f}s" repeatCount="indefinite"/></rect></g>')

dots = "".join(f'<circle cx="{24 + k * 20}" cy="20" r="6" fill="{c}"/>'
               for k, c in enumerate(["#ff5f57", "#febc2e", "#28c840"]))

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Terminal: Olá, sejam bem-vindos todos! Breno Sarcero, Dev Júnior de IA, cursando ADS na FMU">
<defs><pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#44403c"/></pattern></defs>
<rect width="{W}" height="{H}" rx="12" fill="{BG}"/>
<rect width="{W}" height="{H}" rx="12" fill="url(#dots)" opacity=".55"/>
<path d="M0 12 a12 12 0 0 1 12 -12 h{W - 24} a12 12 0 0 1 12 12 v28 h-{W} z" fill="{BAR}"/>
{dots}
<text x="{W / 2}" y="25" fill="{DIM}" font-size="13" text-anchor="middle">breno@sarcero: ~</text>
<g font-size="{FS}">
{chr(10).join(parts)}
</g>
</svg>
'''
svg = svg.replace("<svg ", "<svg font-family=\"'JetBrains Mono','Cascadia Code',Consolas,'DejaVu Sans Mono',monospace\" ", 1)
open(OUT, "w", encoding="utf-8").write(svg)
print("ok", t)
