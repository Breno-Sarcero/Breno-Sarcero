"""Gera assets/flow.svg: diagrama animado do fluxo agêntico (orquestrador, subagentes, MCP)."""
import sys
from html import escape

OUT = sys.argv[1]
W, H = 820, 250
BW, BH = 132, 38                  # tamanho das caixas
DUR = 5                           # segundos de um ciclo completo

BG, BOX, LINE, FG, DIM, AMBER, GREEN, ORANGE = (
    "#1c1917", "#292524", "#44403c", "#e7e5e4", "#a8a29e", "#f59e0b", "#86efac", "#d97757")
FONT = "'JetBrains Mono','Cascadia Code',Consolas,'DejaVu Sans Mono',monospace"

COLS = [28, 188, 348, 508, 668]   # x de cada coluna
ROWS3 = [70, 130, 190]            # y (centro) das linhas quando a coluna tem 3 caixas
MID = 130

nodes = {
    "eu": (COLS[0], MID, "você", "$ prompt", AMBER),
    "orq": (COLS[1], MID, "orquestrador", "planeja e delega", ORANGE),
    "s1": (COLS[2], ROWS3[0], "subagente", "pesquisa", FG),
    "s2": (COLS[2], ROWS3[1], "subagente", "executa", FG),
    "s3": (COLS[2], ROWS3[2], "subagente", "valida", FG),
    "m1": (COLS[3], ROWS3[0], "MCP", "SQL Server", FG),
    "m2": (COLS[3], ROWS3[1], "MCP", "navegador", FG),
    "m3": (COLS[3], ROWS3[2], "API", "ERP · CRM", FG),
    "pr": (COLS[4], MID, "PR revisado", "✓ pronto", GREEN),
}
edges = [("eu", "orq"), ("orq", "s1"), ("orq", "s2"), ("orq", "s3"),
         ("s1", "m1"), ("s2", "m2"), ("s3", "m3"), ("m1", "pr"), ("m2", "pr"), ("m3", "pr")]
# em que etapa (0..3) cada aresta é percorrida
stage = {"eu": 0, "orq": 1, "s1": 2, "s2": 2, "s3": 2, "m1": 3, "m2": 3, "m3": 3}


def path(a, b):
    x1, y1 = nodes[a][0] + BW, nodes[a][1]
    x2, y2 = nodes[b][0], nodes[b][1]
    mx = (x1 + x2) / 2
    return f"M{x1},{y1} C{mx},{y1} {mx},{y2} {x2},{y2}"


parts = []
for i, (a, b) in enumerate(edges):
    d = path(a, b)
    parts.append(f'<path id="e{i}" d="{d}" fill="none" stroke="{LINE}" stroke-width="2"/>')
    seg = DUR / 5
    begin = stage[a] * seg
    # pulso percorre a aresta na sua etapa, fica invisível no resto do ciclo
    k0, k1 = begin / DUR, (begin + seg) / DUR
    parts.append(
        f'<circle r="4" fill="{AMBER}" opacity="0">'
        f'<animateMotion dur="{DUR}s" repeatCount="indefinite" keyPoints="0;0;1;1" '
        f'keyTimes="0;{k0:.3f};{k1:.3f};1" calcMode="linear"><mpath href="#e{i}"/></animateMotion>'
        f'<animate attributeName="opacity" values="0;1;0" keyTimes="0;{k0:.3f};{k1:.3f}" '
        f'calcMode="discrete" dur="{DUR}s" repeatCount="indefinite"/></circle>')

for key, (x, y, title, sub, color) in nodes.items():
    top = y - BH / 2
    glow = ""
    if key in stage or key == "pr":
        # a caixa acende quando o pulso chega nela
        t = stage.get(key, 4) / 5
        glow = (f'<animate attributeName="stroke" values="{LINE};{color};{LINE}" '
                f'keyTimes="0;{max(t, 0.001):.3f};{min(t + 0.2, 0.999):.3f}" calcMode="discrete" '
                f'dur="{DUR}s" repeatCount="indefinite"/>')
    parts.append(
        f'<rect x="{x}" y="{top}" width="{BW}" height="{BH}" rx="7" fill="{BOX}" stroke="{LINE}" stroke-width="1.5">{glow}</rect>'
        f'<text x="{x + BW / 2}" y="{top + 16}" fill="{color}" font-size="12" font-weight="700" text-anchor="middle">{escape(title)}</text>'
        f'<text x="{x + BW / 2}" y="{top + 31}" fill="{DIM}" font-size="11" text-anchor="middle">{escape(sub)}</text>')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}" role="img" aria-label="Fluxo agêntico: você, orquestrador, subagentes, ferramentas MCP e PR revisado">
<defs><pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#44403c"/></pattern></defs>
<rect width="{W}" height="{H}" rx="12" fill="{BG}"/>
<rect width="{W}" height="{H}" rx="12" fill="url(#dots)" opacity=".55"/>
<text x="20" y="30" fill="{DIM}" font-size="13"># como eu monto automações com IA</text>
{chr(10).join(parts)}
</svg>
'''
open(OUT, "w", encoding="utf-8").write(svg)
print("ok")
