"""Gera ícones de tecnologia no mesmo estilo do skillicons.dev (bloco 256x256, cantos 60, fundo #242938)
para as tecnologias que o skillicons não tem. Uso: python gen_tiles.py <pasta assets>

Os ícones de SQL Server e Playwright vêm do devicon (licença MIT) e ficam embutidos no SVG gerado.
"""
import re
import sys
import urllib.request

OUT = sys.argv[1]
TILE, GAP, H = 256, 44, 48
DEVICON = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/{0}/{0}-original.svg"
FONT = "'Segoe UI',Ubuntu,'Helvetica Neue',Arial,sans-serif"


def devicon(name):
    svg = urllib.request.urlopen(DEVICON.format(name), timeout=20).read().decode("utf-8")
    vb = re.search(r'viewBox="([^"]+)"', svg).group(1)
    inner = re.sub(r"^.*?<svg[^>]*>|</svg>\s*$", "", svg, flags=re.S)
    inner = re.sub(r'id="([^"]+)"', rf'id="{name}-\1"', inner)          # evita colisão de ids
    inner = re.sub(r"url\(#([^)]+)\)", rf"url(#{name}-\1)", inner)
    inner = re.sub(r'href="#([^"]+)"', rf'href="#{name}-\1"', inner)
    return f'<svg x="48" y="48" width="160" height="160" viewBox="{vb}">{inner}</svg>'


def claude():
    # asterisco de 8 raios, no laranja do Claude
    rays = "".join(f'<rect x="120" y="44" width="16" height="84" rx="8" fill="#d97757" transform="rotate({a} 128 128)"/>'
                   for a in range(0, 360, 45))
    return rays


def mcp():
    # três nós conectados (cliente, servidor, ferramenta)
    return ('<g stroke="#e7e5e4" stroke-width="14" stroke-linecap="round" fill="none">'
            '<path d="M84 92L128 164L172 92M84 92H172"/></g>'
            '<g fill="#242938" stroke="#e7e5e4" stroke-width="14">'
            '<circle cx="84" cy="92" r="22"/><circle cx="172" cy="92" r="22"/><circle cx="128" cy="164" r="22"/></g>'
            f'<text x="128" y="226" fill="#a8a29e" font-family="{FONT}" font-size="34" font-weight="700" text-anchor="middle">MCP</text>')


def powerbi():
    # três barras crescendo, nas cores do Power BI
    return ('<rect x="70" y="128" width="36" height="84" rx="10" fill="#f2c811" opacity=".55"/>'
            '<rect x="110" y="88" width="36" height="124" rx="10" fill="#f2c811" opacity=".8"/>'
            '<rect x="150" y="44" width="36" height="168" rx="10" fill="#f2c811"/>')


def questor():
    return (f'<text x="128" y="160" fill="#f59e0b" font-family="{FONT}" font-size="140" font-weight="800" text-anchor="middle">Q</text>'
            f'<text x="128" y="218" fill="#a8a29e" font-family="{FONT}" font-size="30" font-weight="700" text-anchor="middle">ERP</text>')


def row(filename, tiles):
    n = len(tiles)
    vw = n * TILE + (n - 1) * GAP
    body = "".join(f'<g transform="translate({i * (TILE + GAP)} 0)"><title>{title}</title>'
                   f'<rect width="{TILE}" height="{TILE}" rx="60" fill="#242938"/>{art}</g>'
                   for i, (title, art) in enumerate(tiles))
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{H * vw / TILE:.2f}" height="{H}" '
           f'viewBox="0 0 {vw} {TILE}" fill="none">{body}</svg>\n')
    open(f"{OUT}/{filename}", "w", encoding="utf-8").write(svg)
    print("ok", filename)


row("tiles-ia-v1.svg", [("Claude Code", claude()), ("MCP", mcp()), ("Playwright", devicon("playwright"))])
row("tiles-dados-v1.svg", [("SQL Server", devicon("microsoftsqlserver")), ("Power BI", powerbi()), ("Questor ERP", questor())])
