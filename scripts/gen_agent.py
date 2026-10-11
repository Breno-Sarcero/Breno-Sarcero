"""Gera assets/agent.svg: mascote com emoções (dorme, acorda, trabalha, raiva com bug, comemora)
sincronizado com um terminal de automação agêntica, em loop."""
import sys
from html import escape

OUT = sys.argv[1]
W, H = 820, 280
DUR = 16.0                        # duração do loop em segundos
MX, MY, MS = 22, 34, 1.9          # posição e escala do mascote (desenhado em 120x120)

BG, FG, DIM, AMBER, GREEN, RED = "#1c1917", "#e7e5e4", "#a8a29e", "#f59e0b", "#86efac", "#f87171"
C, CD, CL, EYE = "#d97757", "#a9553c", "#eba184", "#1c1917"   # laranja, sombra, brilho, olhos
FONT = "'JetBrains Mono','Cascadia Code',Consolas,'DejaVu Sans Mono',monospace"


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


def loop(kind, values, dur, extra=""):
    if kind == "opacity":
        return f'<animate attributeName="opacity" values="{values}" dur="{dur}s" repeatCount="indefinite"{extra}/>'
    return (f'<animateTransform attributeName="transform" type="{kind}" values="{values}" '
            f'dur="{dur}s" repeatCount="indefinite"{extra}/>')


SHADOW = '<ellipse cx="60" cy="106" rx="38" ry="5" fill="#0c0a09" opacity=".7"/>'


def body(c=C, cd=CD, cl=CL, y=30, h=36):
    return (f'<path d="M30 {y}H90V{y + h + 4}H30Z" fill="{cd}"/>'
            f'<path d="M30 {y}H90V{y + h}H30Z" fill="{c}"/>'
            f'<rect x="32" y="{y + 2}" width="56" height="4" fill="{cl}"/>')


def legs(back=CD, front=C, y=66, h=28):
    return (f'<g fill="{back}"><rect x="38" y="{y}" width="8" height="{h}" rx="2"/><rect x="74" y="{y}" width="8" height="{h}" rx="2"/></g>'
            f'<g fill="{front}"><rect x="48" y="{y}" width="8" height="{h}" rx="2"/><rect x="64" y="{y}" width="8" height="{h}" rx="2"/></g>')


ARMS = f'<rect x="18" y="42" width="12" height="20" rx="2" fill="{C}"/><rect x="90" y="42" width="12" height="20" rx="2" fill="{C}"/>'
HAPPY_EYES = (f'<g stroke="{EYE}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" fill="none">'
              '<path d="M42 46L50 51L42 56"/><path d="M78 46L70 51L78 56"/></g>')

# ---------- poses ----------
sleep = (SHADOW
         + f'<rect x="32" y="88" width="10" height="12" rx="3" fill="{CD}"/><rect x="46" y="88" width="10" height="12" rx="3" fill="{C}"/>'
         f'<rect x="64" y="88" width="10" height="12" rx="3" fill="{C}"/><rect x="78" y="88" width="10" height="12" rx="3" fill="{CD}"/>'
         f'<g>{loop("translate", "0 0;0 1.5;0 0", 2.4)}'   # respiração
         f'<path d="M28 46H92V92H80V96H40V92H28Z" fill="{CD}"/><path d="M28 46H92V88H80V94H40V88H28Z" fill="{C}"/>'
         f'<rect x="30" y="48" width="60" height="4" fill="{CL}"/>'
         f'<rect x="18" y="60" width="10" height="18" rx="3" fill="{C}"/><rect x="92" y="60" width="10" height="18" rx="3" fill="{C}"/>'
         f'<g stroke="{EYE}" stroke-width="4" stroke-linecap="round"><line x1="42" y1="66" x2="52" y2="66"/><line x1="68" y1="66" x2="78" y2="66"/></g>'
         '<path d="M32 48C32 30 72 20 88 48Z" fill="#3b82f6"/><rect x="28" y="44" width="64" height="6" rx="3" fill="#fff"/>'
         '<path d="M82 36Q96 38 98 56Q96 68 92 72" fill="none" stroke="#3b82f6" stroke-width="10" stroke-linecap="round"/>'
         '<circle cx="91" cy="74" r="6" fill="#fff"/></g>'
         f'<g font-weight="900" fill="#60a5fa">{loop("translate", "0 0;4 -8", 2)}{loop("opacity", "0;1;1;0", 2)}'
         '<text x="98" y="40" font-size="16">Z</text><text x="106" y="26" font-size="12" fill="#93c5fd">z</text>'
         '<text x="110" y="14" font-size="9" fill="#bfdbfe">z</text></g>')

awake = (SHADOW + legs() + f'<g>{body()}{ARMS}'
         f'<rect x="43" y="44" width="6" height="11" rx="2" fill="{EYE}"/><rect x="71" y="44" width="6" height="11" rx="2" fill="{EYE}"/></g>'
         f'<text x="60" y="22" fill="{AMBER}" font-size="20" font-weight="900" text-anchor="middle">!'
         f'{loop("translate", "0 0;0 -3;0 0", 0.4)}</text>')

work = (SHADOW + '<rect x="6" y="98" width="108" height="4" rx="2" fill="#44403c"/>'
        # sentado de lado, olhando para o notebook à esquerda
        f'<g fill="{CD}"><rect x="62" y="76" width="8" height="22" rx="2"/><rect x="88" y="76" width="8" height="22" rx="2"/></g>'
        f'<path d="M50 36H100V80H50Z" fill="{CD}"/><path d="M50 36H100V76H50Z" fill="{C}"/>'
        f'<rect x="52" y="38" width="46" height="4" fill="{CL}"/>'
        f'<g fill="{C}"><rect x="72" y="76" width="8" height="22" rx="2"/><rect x="80" y="76" width="8" height="22" rx="2"/></g>'
        f'<g fill="{EYE}">{loop("translate", "0 0;0 0;-2 0;-2 0;0 0", 3)}'
        '<rect x="56" y="48" width="5" height="10" rx="2"/><rect x="70" y="48" width="5" height="10" rx="2"/></g>'
        '<path d="M8 96L42 96L38 92L12 92Z" fill="#9ca3af"/><rect x="8" y="95" width="34" height="3" rx="1" fill="#6b7280"/>'
        '<path d="M10 62L34 62L36 92L8 92Z" fill="#1f2937" stroke="#4b5563" stroke-width="2"/>'
        '<path d="M12 64L32 64L34 90L10 90Z" fill="#064e3b"/>'
        # linhas de código aparecendo na tela
        + "".join(f'<line x1="14" y1="{70 + i * 5}" x2="{w}" y2="{70 + i * 5}" stroke="{col}" stroke-width="1.6" stroke-linecap="round">'
                  f'<animate attributeName="opacity" values="0;1;1" dur="1.2s" begin="{i * 0.3:.1f}s" repeatCount="indefinite"/></line>'
                  for i, (w, col) in enumerate([(24, "#fff"), (29, "#34d399"), (21, "#fbbf24"), (27, "#34d399")]))
        + f'<g>{loop("translate", "0 0;-1.5 1.5;0 0", 0.25)}'
        f'<rect x="30" y="80" width="24" height="7" rx="3" fill="{C}"/></g>'
        f'<g>{loop("translate", "0 0;-1.5 1.5;0 0", 0.25, ' begin="0.12s"')}'
        f'<rect x="34" y="86" width="20" height="6" rx="3" fill="{CD}"/></g>')

rage = ('<defs><linearGradient id="fire" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#dc2626"/>'
        '<stop offset=".4" stop-color="#ea580c"/><stop offset=".7" stop-color="#f59e0b"/><stop offset="1" stop-color="#fef08a"/></linearGradient>'
        '<linearGradient id="hot" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ef4444"/><stop offset="1" stop-color="#991b1b"/></linearGradient></defs>'
        '<ellipse cx="60" cy="108" rx="40" ry="6" fill="#7f1d1d" opacity=".5"/>'
        f'<g>{loop("translate", "-1.5 0;1.5 0;-1.5 0", 0.12)}'
        '<g><path d="M36 32Q32 10 44 16Q48 2 60 0Q72 2 76 16Q88 10 84 32Z" fill="url(#fire)">'
        f'{loop("translate", "0 0;0 -2;0 0", 0.3)}</path>'
        f'<path d="M44 32Q42 18 50 20Q54 8 60 6Q66 8 70 20Q78 18 76 32Z" fill="#fff">{loop("opacity", ".9;.4;.9", 0.25)}</path></g>'
        + legs("#7f1d1d", "#b91c1c", 70, 26)
        + '<path d="M30 32H90V74H30Z" fill="#7f1d1d"/><path d="M30 32H90V70H30Z" fill="url(#hot)"/><rect x="32" y="34" width="56" height="4" fill="#f87171"/>'
        '<rect x="16" y="38" width="12" height="20" rx="3" fill="#b91c1c" transform="rotate(-30 16 38)"/>'
        '<rect x="92" y="38" width="12" height="20" rx="3" fill="#b91c1c" transform="rotate(30 92 38)"/>'
        '<g stroke="#fef08a" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" fill="none">'
        '<path d="M40 46L50 51L40 56"/><path d="M80 46L70 51L80 56"/></g>'
        '<path d="M38 40L52 45M82 40L68 45" stroke="#7f1d1d" stroke-width="4" stroke-linecap="round"/>'
        '<rect x="48" y="58" width="24" height="8" rx="2" fill="#7f1d1d"/>'
        '<path d="M50 60H70M55 58V66M60 58V66M65 58V66" stroke="#fff" stroke-width="1.5"/></g>'
        f'<g fill="{AMBER}" font-weight="900" font-size="15"><text x="-4" y="28">#!?</text><text x="96" y="28">ERR</text></g>')

happy = (SHADOW + f'<g>{loop("translate", "0 0;0 -8;0 0;0 0", 0.9)}{legs()}{body()}'
         f'<rect x="18" y="18" width="12" height="26" rx="2" fill="{C}" transform="rotate(-20 30 44)"/>'
         f'<rect x="90" y="18" width="12" height="26" rx="2" fill="{C}" transform="rotate(20 90 44)"/>'
         f'{HAPPY_EYES}</g>'
         f'<g fill="{AMBER}" font-size="14">{loop("opacity", "1;.2;1", 0.8)}'
         '<text x="4" y="24">✦</text><text x="104" y="18">✦</text><text x="110" y="70">✦</text></g>')

# linha do tempo (s): dorme 0-3 · acorda 3-4 · trabalha 4-7.8 · raiva 7.8-10 · trabalha 10-12.4 · comemora 12.4-16
poses = [(sleep, 0, 3), (awake, 3, 4), (work, 4, 7.8), (rage, 7.8, 10), (work, 10, 12.4), (happy, 12.4, None)]
mascot = "".join(f'<g opacity="{1 if t0 == 0 else 0}">{vis(t0, t1)}{g}</g>' for g, t0, t1 in poses)
mascot = f'<g transform="translate({MX} {MY}) scale({MS})">{mascot}</g>'


# ---------- terminal ----------
def text(x, y, s, color, weight="400"):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="15" font-weight="{weight}">{escape(s)}</text>'


TX, TY, LH, CHK = 300, 52, 30, 640
term = [
    # cursor piscando enquanto o mascote dorme
    f'<g>{vis(0, 3)}{text(TX, TY, "$", AMBER, "700")}'
    f'<rect x="{TX + 18}" y="{TY - 13}" width="9" height="17" fill="{AMBER}">{loop("opacity", "1;0;1", 1)}</rect></g>',
    f'<g opacity="0">{vis(3)}{text(TX, TY, "$ claude", AMBER, "700")}{text(TX + 92, TY, chr(34) + "fecha o mês do cliente" + chr(34), FG, "700")}</g>',
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
    step(3, "Validando no SQL Server…", 6.6, 10.8, t_fail=7.8),
    f'<g opacity="0">{vis(7.8, 10.8)}{text(TX + 22, TY + 4 * LH + 8, "↳ saldo divergente, corrigindo…", RED)}</g>',
    f'<g opacity="0">{vis(10.8)}{text(TX + 22, TY + 4 * LH + 8, "↳ corrigido e validado de novo", DIM)}</g>',
    step(5, "Abrindo PR para revisão…", 11.2, 12.2),
    f'<g opacity="0">{vis(12.4)}{text(TX, TY + 6 * LH + 14, "✓ pronto · automação agêntica com IA", GREEN, "700")}</g>',
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
