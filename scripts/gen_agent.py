"""Gera assets/agent.svg: mascote com emoções (dorme, acorda, trabalha, raiva com bug, comemora)
sincronizado com um terminal de automação agêntica, em loop.

O mascote é sempre o mesmo corpo, de frente; cada emoção muda só olhos, braços, cor e acessórios.
"""
import sys
from html import escape

OUT = sys.argv[1]
W, H = 820, 280
DUR = 16.0                        # duração do loop em segundos
MX, MY, MS = 30, 30, 1.9          # posição e escala do mascote (desenhado em 120x120)

BG, FG, DIM, AMBER, GREEN, RED = "#1c1917", "#e7e5e4", "#a8a29e", "#f59e0b", "#86efac", "#f87171"
ORANGE = ("#d97757", "#a9553c", "#eba184")         # cor, sombra, brilho
HOT = ("#dc2626", "#7f1d1d", "#f87171")
EYE = "#1c1917"
FONT = "'JetBrains Mono','Cascadia Code',Consolas,'DejaVu Sans Mono',monospace"

# linha do tempo (s): dorme · acorda · trabalha · raiva · trabalha · comemora
T_WAKE, T_WORK, T_RAGE, T_FIX, T_HAPPY = 3.0, 4.0, 7.8, 10.0, 12.4


def vis(t0, t1=None):
    """Visível de t0 até t1 (segundos) dentro do loop."""
    if t1 is None:
        vals, keys = "0;1", f"0;{t0 / DUR:.4f}"
    elif t0 == 0:
        vals, keys = "1;0", f"0;{t1 / DUR:.4f}"
    else:
        vals, keys = "0;1;0", f"0;{t0 / DUR:.4f};{t1 / DUR:.4f}"
    return (f'<animate attributeName="opacity" values="{vals}" keyTimes="{keys}" '
            f'calcMode="discrete" dur="{DUR}s" repeatCount="indefinite"/>')


def loop(kind, values, dur, begin=None):
    b = f' begin="{begin}"' if begin else ""
    if kind == "opacity":
        return f'<animate attributeName="opacity" values="{values}" dur="{dur}s" repeatCount="indefinite"{b}/>'
    return (f'<animateTransform attributeName="transform" type="{kind}" values="{values}" '
            f'dur="{dur}s" repeatCount="indefinite"{b}/>')


# ---------- corpo único (grade de 6 unidades: corpo 12x8, braços nas linhas 4-5, 4 pernas) ----------
def legs(c, h=12):
    cor, sombra, _ = c
    return (f'<rect x="30" y="76" width="6" height="{h + 2}" fill="{sombra}"/><rect x="84" y="76" width="6" height="{h + 2}" fill="{sombra}"/>'
            f'<rect x="42" y="76" width="6" height="{h + 2}" fill="{cor}"/><rect x="72" y="76" width="6" height="{h + 2}" fill="{cor}"/>')


def torso(c):
    cor, sombra, brilho = c
    return (f'<rect x="24" y="30" width="72" height="48" fill="{cor}"/>'
            f'<rect x="24" y="72" width="72" height="6" fill="{sombra}"/>'
            f'<rect x="24" y="30" width="72" height="4" fill="{brilho}"/>')


def arms(c, up=False):
    cor = c[0]
    if up:   # braços levantados, saindo dos ombros
        return f'<rect x="12" y="14" width="12" height="28" fill="{cor}"/><rect x="96" y="14" width="12" height="28" fill="{cor}"/>'
    return f'<rect x="12" y="54" width="12" height="12" fill="{cor}"/><rect x="96" y="54" width="12" height="12" fill="{cor}"/>'


EYES_OPEN = f'<g fill="{EYE}"><rect x="36" y="42" width="6" height="12"/><rect x="78" y="42" width="6" height="12"/></g>'
EYES_SHUT = f'<g fill="{EYE}"><rect x="34" y="50" width="10" height="4"/><rect x="76" y="50" width="10" height="4"/></g>'


def chevrons(color, w=4.5):
    return (f'<g stroke="{color}" stroke-width="{w}" stroke-linecap="square" stroke-linejoin="miter" fill="none">'
            '<path d="M35 42L43 48L35 54"/><path d="M85 42L77 48L85 54"/></g>')


SHADOW = '<ellipse cx="60" cy="96" rx="40" ry="5" fill="#0c0a09" opacity=".7"/>'

# ---------- emoções ----------
sleep = (SHADOW
         + f'<g>{loop("translate", "0 0;0 1.5;0 0", 2.4)}'           # respiração
         + legs(ORANGE, 4).replace('y="76"', 'y="84"') + '<g transform="translate(0 8)">'
         + torso(ORANGE) + arms(ORANGE) + EYES_SHUT
         + '<path d="M26 32C30 10 70 4 94 32Z" fill="#3b82f6"/><rect x="22" y="28" width="76" height="7" rx="3" fill="#fff"/>'
         '<path d="M86 18Q104 20 106 40Q105 52 100 56" fill="none" stroke="#3b82f6" stroke-width="9" stroke-linecap="round"/>'
         '<circle cx="99" cy="58" r="6" fill="#fff"/></g></g>'
         f'<g font-weight="900" fill="#60a5fa">{loop("translate", "0 0;4 -8", 2)}{loop("opacity", "0;1;1;0", 2)}'
         '<text x="100" y="34" font-size="16">Z</text><text x="108" y="20" font-size="12" fill="#93c5fd">z</text>'
         '<text x="113" y="9" font-size="9" fill="#bfdbfe">z</text></g>')

awake = (SHADOW + legs(ORANGE) + torso(ORANGE) + arms(ORANGE) + EYES_OPEN
         + f'<text x="60" y="22" fill="{AMBER}" font-size="20" font-weight="900" text-anchor="middle">!'
         f'{loop("translate", "0 0;0 -3;0 0", 0.4)}</text>')

# trabalhando: notebook na frente (vemos a tampa), olhos baixos piscando, braços digitando
work = (SHADOW + legs(ORANGE) + torso(ORANGE)
        + f'<g fill="{EYE}"><rect x="36" y="48" width="6" height="7"/><rect x="78" y="48" width="6" height="7"/>'
        f'<animate attributeName="opacity" values="1;0;1" keyTimes="0;.92;.97" dur="2.6s" repeatCount="indefinite"/></g>'
        + f'<rect x="12" y="58" width="12" height="12" fill="{ORANGE[0]}">{loop("translate", "0 0;3 2;0 0", 0.3)}</rect>'
        f'<rect x="96" y="58" width="12" height="12" fill="{ORANGE[0]}">{loop("translate", "0 0;-3 2;0 0", 0.3, "0.15s")}</rect>'
        # tampa do notebook com brilho da tela no rosto
        '<path d="M34 64H86L90 96H30Z" fill="#57534e"/><path d="M36 66H84L87 94H33Z" fill="#78716c"/>'
        '<rect x="22" y="94" width="76" height="4" rx="2" fill="#a8a29e"/>'
        f'<text x="60" y="84" fill="{AMBER}" font-size="10" font-weight="700" text-anchor="middle">&lt;/&gt;</text>'
        '<rect x="24" y="34" width="72" height="30" fill="#34d399" opacity=".08"/>'
        # símbolos de código subindo
        + "".join(f'<text x="{x}" y="60" fill="{col}" font-size="9" font-weight="700" opacity="0">{escape(s)}'
                  f'{loop("translate", "0 0;0 -40", 1.8, f"{d}s")}{loop("opacity", "0;1;0", 1.8, f"{d}s")}</text>'
                  for x, s, col, d in [(18, "{ }", "#34d399", 0), (96, "SQL", "#fbbf24", 0.6), (8, "API", "#60a5fa", 1.2)]))

rage = ('<defs><linearGradient id="fire" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#dc2626"/>'
        '<stop offset=".4" stop-color="#ea580c"/><stop offset=".7" stop-color="#f59e0b"/><stop offset="1" stop-color="#fef08a"/></linearGradient></defs>'
        '<ellipse cx="60" cy="96" rx="42" ry="6" fill="#7f1d1d" opacity=".6"/>'
        f'<g>{loop("translate", "-1.5 0;1.5 0;-1.5 0", 0.12)}'
        f'<path d="M30 31Q26 12 38 16Q42 0 60 -4Q78 0 82 16Q94 12 90 31Z" fill="url(#fire)">{loop("translate", "0 0;0 -2;0 0", 0.3)}</path>'
        f'<path d="M40 31Q38 18 46 20Q50 6 60 4Q70 6 74 20Q82 18 80 31Z" fill="#fff">{loop("opacity", ".9;.4;.9", 0.25)}</path>'
        + legs(HOT) + torso(HOT) + arms(HOT, up=True) + chevrons("#fef08a", 5)
        + '<path d="M32 36L46 42M88 36L74 42" stroke="#7f1d1d" stroke-width="4" stroke-linecap="square"/>'
        '<rect x="46" y="58" width="28" height="9" fill="#7f1d1d"/>'
        '<path d="M48 62.5H72M53 58V67M60 58V67M67 58V67" stroke="#fff" stroke-width="1.5"/></g>'
        f'<g fill="{AMBER}" font-weight="900" font-size="15"><text x="-8" y="20">#!?</text><text x="98" y="20">ERR</text></g>')

happy = (SHADOW + f'<g>{loop("translate", "0 0;0 -8;0 0;0 0", 0.9)}'
         + legs(ORANGE) + torso(ORANGE) + arms(ORANGE, up=True) + chevrons(EYE) + '</g>'
         f'<g fill="{AMBER}" font-size="14">{loop("opacity", "1;.2;1", 0.8)}'
         '<text x="0" y="24">✦</text><text x="106" y="16">✦</text><text x="112" y="70">✦</text></g>')

poses = [(sleep, 0, T_WAKE), (awake, T_WAKE, T_WORK), (work, T_WORK, T_RAGE),
         (rage, T_RAGE, T_FIX), (work, T_FIX, T_HAPPY), (happy, T_HAPPY, None)]
inner = "".join(f'<g opacity="{1 if t0 == 0 else 0}">{vis(t0, t1)}{g}</g>' for g, t0, t1 in poses)

# "pop" a cada troca de emoção: achata, estica e volta (escala a partir dos pés)
vals, keys = ["1 1"], [0.0]
for t in (T_WAKE, T_WORK, T_RAGE, T_FIX, T_HAPPY):
    for dt, v in ((-0.01, "1 1"), (0, "1.14 0.84"), (0.1, "0.92 1.1"), (0.2, "1.03 0.98"), (0.28, "1 1")):
        vals.append(v)
        keys.append((t + dt) / DUR)
vals.append("1 1")
keys.append(1.0)
pop = (f'<animateTransform attributeName="transform" type="scale" values="{";".join(vals)}" '
       f'keyTimes="{";".join(f"{k:.4f}" for k in keys)}" dur="{DUR}s" repeatCount="indefinite"/>')
mascot = (f'<g transform="translate({MX + 60 * MS} {MY + 96 * MS}) scale({MS})"><g>{pop}'
          f'<g transform="translate(-60 -96)">{inner}</g></g></g>')


# ---------- terminal ----------
def text(x, y, s, color, weight="400"):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="15" font-weight="{weight}">{escape(s)}</text>'


TX, TY, LH, CHK = 300, 52, 30, 640
term = [
    # cursor piscando enquanto o mascote dorme
    f'<g>{vis(0, T_WAKE)}{text(TX, TY, "$", AMBER, "700")}'
    f'<rect x="{TX + 18}" y="{TY - 13}" width="9" height="17" fill="{AMBER}">{loop("opacity", "1;0;1", 1)}</rect></g>',
    f'<g opacity="0">{vis(T_WAKE)}{text(TX, TY, "$ claude", AMBER, "700")}{text(TX + 92, TY, chr(34) + "fecha o mês do cliente" + chr(34), FG, "700")}</g>',
]


def step(row, label, t_start, t_ok, t_fail=None):
    y = TY + row * LH + 8
    out = f'<g opacity="0">{vis(t_start)}{text(TX, y, "●", AMBER)}{text(TX + 22, y, label, DIM)}</g>'
    if t_fail:
        out += f'<g opacity="0">{vis(t_fail, t_ok)}{text(CHK, y, "✗", RED, "700")}</g>'
    return out + f'<g opacity="0">{vis(t_ok)}{text(CHK, y, "✓", GREEN, "700")}</g>'


term += [
    step(1, "Lendo dados do ERP via API…", 4.0, 5.0),
    step(2, "Conciliando lançamentos…", 5.3, 6.3),
    step(3, "Validando no SQL Server…", 6.6, 10.8, t_fail=T_RAGE),
    f'<g opacity="0">{vis(T_RAGE, 10.8)}{text(TX + 22, TY + 4 * LH + 8, "↳ saldo divergente, corrigindo…", RED)}</g>',
    f'<g opacity="0">{vis(10.8)}{text(TX + 22, TY + 4 * LH + 8, "↳ corrigido e validado de novo", DIM)}</g>',
    step(5, "Abrindo PR para revisão…", 11.2, 12.2),
    f'<g opacity="0">{vis(T_HAPPY)}{text(TX, TY + 6 * LH + 14, "✓ pronto · automação agêntica com IA", GREEN, "700")}</g>',
]

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}" role="img" aria-label="Mascote que dorme, acorda com um comando, trabalha, se irrita com um erro, corrige e comemora: automação agêntica com IA">
<defs><pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#44403c"/></pattern></defs>
<rect width="{W}" height="{H}" rx="12" fill="{BG}"/>
<rect width="{W}" height="{H}" rx="12" fill="url(#dots)" opacity=".55"/>
{mascot}
{chr(10).join(term)}
</svg>
'''
open(OUT, "w", encoding="utf-8").write(svg)
print("ok")
