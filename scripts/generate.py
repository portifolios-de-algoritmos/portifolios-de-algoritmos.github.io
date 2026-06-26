#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador estático do mural de portfólios da disciplina de Algoritmos e Programação.

Fonte única de verdade: a lista PORTFOLIOS abaixo.
Produz: images/<slug>.svg (capa gerada por aluno), data/portfolios.json e index.html.

Rode com:  python3 scripts/generate.py
"""

import json
import os
from html import escape as html_escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# Dados dos portfólios (coletados visitando cada site da turma).
# status: "online" | "wip" (no ar, em construção) | "offline" (fora do ar)
# ---------------------------------------------------------------------------
PORTFOLIOS = [
    {
        "slug": "arthur-prates",
        "nome": "Arthur Prates",
        "iniciais": "AP",
        "curso": "Engenharia Mecânica",
        "intro": "Evolução em lógica de programação com Python, documentada atividade por atividade.",
        "tech": ["Python", "HTML", "CSS", "Git", "IA"],
        "url": "https://arthurpratesaluno-collab.github.io/arthurpratesaluno.github.io",
        "status": "online",
    },
    {
        "slug": "andressa-almada",
        "nome": "Andressa Almada",
        "iniciais": "AA",
        "curso": "",
        "intro": "Portfólio em formato de guia, ensinando fundamentos de Python com exemplos.",
        "tech": ["Python", "HTML", "CSS"],
        "url": "https://andressaalmadaaluno-prog.github.io/portfolio-andressa./",
        "status": "online",
    },
    {
        "slug": "diogo",
        "nome": "Diogo",
        "iniciais": "DI",
        "curso": "Engenharia de Telecomunicações",
        "intro": "Portfólio da disciplina com atividades em Python, em construção.",
        "tech": ["Python", "JavaScript", "HTML", "CSS", "IA"],
        "url": "https://sudodiogo.github.io",
        "status": "online",
    },
    {
        "slug": "erick-abella",
        "nome": "Erick Abella",
        "iniciais": "EA",
        "curso": "Engenharia Elétrica",
        "intro": "14 atividades de Algoritmos reunidas numa stack web moderna com Next.js.",
        "tech": ["Next.js", "Tailwind", "Vercel", "Python", "JavaScript"],
        "url": "https://portifolio-erickabella.vercel.app",
        "status": "online",
    },
    {
        "slug": "fernando-dala",
        "nome": "Fernando da Silva Dala",
        "iniciais": "FD",
        "curso": "",
        "intro": "18 atividades concluídas da disciplina de Algoritmos e Programação.",
        "tech": ["Python", "HTML", "CSS"],
        "url": "https://fernandodalaaluno-beep.github.io/algoritmos/",
        "status": "online",
    },
    {
        "slug": "gabriel-garcia",
        "nome": "Gabriel Garcia",
        "iniciais": "GG",
        "curso": "",
        "intro": "Portfólio semestral reunindo as atividades do curso, em fase inicial.",
        "tech": ["HTML", "CSS"],
        "url": "https://gabrieldagaluno-sys.github.io",
        "status": "online",
    },
    {
        "slug": "henrique",
        "nome": "Henrique",
        "iniciais": "HE",
        "curso": "",
        "intro": "Exercícios e atividades de algoritmos, incluindo um simulador de movimento.",
        "tech": ["HTML", "CSS"],
        "url": "https://henriquedsnaluno-dotcom.github.io/Portfolio/",
        "status": "online",
    },
    {
        "slug": "lorenzo-ximendes",
        "nome": "Lorenzo Ximendes",
        "iniciais": "LX",
        "curso": "",
        "intro": "Portfólio interativo com um terminal Python rodando no próprio navegador.",
        "tech": ["JavaScript", "Python", "HTML", "CSS"],
        "url": "https://github.com/lorenzoximendesaluno-dotcom/portifolio-de-algoritmos",
        "status": "online",
    },
    {
        "slug": "lucas-viana",
        "nome": "Lucas Viana de Freitas",
        "iniciais": "LV",
        "curso": "",
        "intro": "Portfólio acadêmico com 23 atividades de Algoritmos e Programação.",
        "tech": ["HTML", "CSS", "JavaScript", "Python"],
        "url": "https://algoritimos2.github.io",
        "status": "online",
    },
    {
        "slug": "matheus-leal",
        "nome": "Matheus Leal Peres",
        "iniciais": "ML",
        "curso": "",
        "intro": "Painel de acompanhamento de atividades, com filtros de entregas e prazos.",
        "tech": ["JavaScript", "SVG", "Python", "HTML", "CSS"],
        "url": "https://exoticos55.github.io",
        "status": "online",
    },
    {
        "slug": "pedro-amaral",
        "nome": "Pedro Amaral",
        "iniciais": "PA",
        "curso": "",
        "intro": "Portfólio acadêmico em montagem, organizando as entregas do semestre.",
        "tech": ["HTML", "CSS"],
        "url": "https://portfoliopeamaral.github.io",
        "status": "online",
    },
    {
        "slug": "pedro-henrique",
        "nome": "Pedro Henrique",
        "iniciais": "PH",
        "curso": "Engenharia Elétrica",
        "intro": "Portfólio de algoritmos com foco na linguagem C.",
        "tech": ["C", "HTML", "CSS"],
        "url": "https://pedrinhogang.github.io/pedrohaluno-github.io/",
        "status": "online",
    },
    {
        "slug": "vinicius-moletta",
        "nome": "Vinícius Moletta",
        "iniciais": "VM",
        "curso": "",
        "intro": "Jornada acadêmica 2026: 14 trabalhos da disciplina reunidos em repositório.",
        "tech": ["HTML", "CSS", "JavaScript"],
        "url": "https://github.com/viniciusmolettaaluno-lang/jornada-academica-2026",
        "status": "online",
    },
    {
        "slug": "lista-trabalhos",
        "nome": "Lista de Trabalhos",
        "iniciais": "LT",
        "curso": "",
        "intro": "Atividades em Python com exercícios gerados e avaliados com apoio de IA.",
        "tech": ["Python", "HTML", "CSS", "IA"],
        "url": "https://lista-do-meu-trabalho-da-disciplina.github.io/",
        "status": "online",
    },
    {
        "slug": "bernardo-bender",
        "nome": "Bernardo Bender",
        "iniciais": "BB",
        "curso": "",
        "intro": "Portfólio ainda não publicado (página retorna 404).",
        "tech": [],
        "url": "https://bernardobenderaluno-hue.github.io/atividadefinal/",
        "status": "offline",
    },
    {
        "slug": "kaua-santos",
        "nome": "Kauã Santos",
        "iniciais": "KS",
        "curso": "",
        "intro": "Espaço criado, conteúdo do portfólio ainda em construção.",
        "tech": [],
        "url": "https://kauasantosaluno-tech.github.io",
        "status": "wip",
    },
    {
        "slug": "portfolio-sem-id",
        "nome": "Portfólio sem identificação",
        "iniciais": "?",
        "curso": "",
        "intro": "Endereço da turma sem página publicada no momento (404).",
        "tech": [],
        "url": "https://algoritmos-e-programacao.github.io",
        "status": "offline",
    },
]

MASK32 = 0xFFFFFFFF


def imul(a, b):
    """Multiplicação 32-bit (equivalente ao Math.imul do JS)."""
    return (a * b) & MASK32


def hash32(s):
    """FNV-1a 32-bit."""
    h = 2166136261
    for ch in s:
        h ^= ord(ch)
        h = imul(h, 16777619)
    return h & MASK32


def mulberry32(seed):
    """PRNG determinístico (mulberry32)."""
    a = seed & MASK32

    def rnd():
        nonlocal a
        a = (a + 0x6D2B79F5) & MASK32
        t = imul(a ^ (a >> 15), 1 | a)
        t = (t + imul(t ^ (t >> 7), 61 | t)) & MASK32
        t = t ^ (t >> 14)
        return (t & MASK32) / 4294967296

    return rnd


def esc_xml(s):
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def esc_html(s):
    return html_escape(str(s), quote=True)


def svg_cover(p, index):
    W, H = 640, 400
    seed = hash32(p["slug"])
    rnd = mulberry32(seed)
    # Ângulo áureo: distribui os matizes bem separados no círculo cromático.
    hue = round(index * 137.508) % 360
    hue2 = (hue + 35 + int(rnd() * 40)) % 360

    offline = p["status"] == "offline"
    sat = 12 if offline else 72
    base_light = 60 if offline else 56

    c1 = f"hsl({hue} {sat}% {base_light}%)"
    c2 = f"hsl({hue2} {sat}% {base_light - 14}%)"

    blobs = []
    for _ in range(5):
        bx = round(rnd() * W)
        by = round(rnd() * H)
        r = round(50 + rnd() * 120)
        bhue = (hue + int(rnd() * 360)) % 360
        if offline:
            fill = f"hsl({hue} 8% {70 + int(rnd() * 15)}%)"
        else:
            fill = f"hsl({bhue} 85% {62 + int(rnd() * 18)}%)"
        op = round(0.18 + rnd() * 0.22, 2)
        blobs.append(f'<circle cx="{bx}" cy="{by}" r="{r}" fill="{fill}" opacity="{op}"/>')

    dots = []
    for _ in range(14):
        dx = round(rnd() * W)
        dy = round(rnd() * H)
        dr = round(2 + rnd() * 5)
        op = round(0.25 + rnd() * 0.4, 2)
        dots.append(f'<circle cx="{dx}" cy="{dy}" r="{dr}" fill="#ffffff" opacity="{op}"/>')

    initials_size = 150 if len(p["iniciais"]) > 2 else 190
    blobs_str = "\n  ".join(blobs)
    dots_str = "\n  ".join(dots)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Capa do portfólio de {esc_xml(p['nome'])}">
  <defs>
    <linearGradient id="g-{p['slug']}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{c1}"/>
      <stop offset="1" stop-color="{c2}"/>
    </linearGradient>
    <filter id="s-{p['slug']}" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#000000" flood-opacity="0.28"/>
    </filter>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#g-{p['slug']})"/>
  {blobs_str}
  {dots_str}
  <text x="{W // 2}" y="{H // 2}" text-anchor="middle" dominant-baseline="central"
    font-family="'Trebuchet MS', Verdana, sans-serif" font-weight="800"
    font-size="{initials_size}" fill="#ffffff" filter="url(#s-{p['slug']})">{esc_xml(p['iniciais'])}</text>
</svg>
"""


def aggregate_tech(items):
    counts = {}
    for p in items:
        for t in p["tech"]:
            counts[t] = counts.get(t, 0) + 1
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))


STATUS_LABEL = {"online": "No ar", "wip": "Em construção", "offline": "Indisponível"}


def status_badge(status):
    return f'<span class="badge badge--{status}">{STATUS_LABEL[status]}</span>'


def tech_chips(tech):
    if not tech:
        return ""
    items = "".join(
        f'<li class="chip" data-tech="{esc_html(t)}">{esc_html(t)}</li>' for t in tech
    )
    return f'<ul class="chips">{items}</ul>'


def card(p):
    is_repo = "github.com" in p["url"]
    if p["status"] == "offline":
        link_label = "Indisponível"
    elif is_repo:
        link_label = "Ver repositório"
    else:
        link_label = "Abrir portfólio"

    course_chip = (
        f'<span class="course">{esc_html(p["curso"])}</span>' if p["curso"] else ""
    )

    if p["status"] == "offline":
        action = f'<span class="btn btn--disabled" aria-disabled="true">{link_label}</span>'
    else:
        action = (
            f'<a class="btn" href="{esc_html(p["url"])}" target="_blank" rel="noopener">'
            f'{link_label} <span aria-hidden="true">↗</span></a>'
        )

    return f"""
      <article class="card card--{p['status']}">
        <div class="card__cover">
          <img src="images/{p['slug']}.svg" alt="Capa do portfólio de {esc_html(p['nome'])}" loading="lazy" width="640" height="400"/>
          {status_badge(p['status'])}
        </div>
        <div class="card__body">
          <header class="card__head">
            <h3 class="card__name">{esc_html(p['nome'])}</h3>
            {course_chip}
          </header>
          <p class="card__intro">{esc_html(p['intro'])}</p>
          {tech_chips(p['tech'])}
          {action}
        </div>
      </article>"""


def tech_section(items):
    agg = aggregate_tech(items)
    max_count = agg[0][1] if agg else 1
    rows = []
    for tech, count in agg:
        pct = round((count / max_count) * 100)
        rows.append(
            f"""
          <li class="techbar">
            <span class="techbar__name" data-tech="{esc_html(tech)}">{esc_html(tech)}</span>
            <span class="techbar__track"><span class="techbar__fill" style="width:{pct}%"></span></span>
            <span class="techbar__count">{count}</span>
          </li>"""
        )
    return "".join(rows)


def build():
    online = sum(1 for p in PORTFOLIOS if p["status"] == "online")
    total = len(PORTFOLIOS)
    tech_count = len(aggregate_tech(PORTFOLIOS))

    cards_html = "\n".join(card(p) for p in PORTFOLIOS)
    tech_html = tech_section(PORTFOLIOS)

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Portfólios da Turma · Algoritmos e Programação</title>
  <meta name="description" content="Mural dos portfólios criados pelos alunos da disciplina de Algoritmos e Programação."/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="styles.css"/>
</head>
<body>
  <div class="bg-blobs" aria-hidden="true">
    <span class="bg-blob bg-blob--1"></span>
    <span class="bg-blob bg-blob--2"></span>
    <span class="bg-blob bg-blob--3"></span>
  </div>

  <header class="hero">
    <p class="hero__eyebrow">Disciplina de Algoritmos e Programação</p>
    <h1 class="hero__title">Mural de Portfólios da Turma</h1>
    <p class="hero__lead">
      Ao longo do semestre, cada aluno foi desafiado a transformar suas entregas em um
      portfólio próprio. Esta página reúne e apresenta todos eles, num só lugar.
    </p>
    <p class="hero__actions">
      <a class="hero__cta" href="https://algoritmos4all.github.io" target="_blank" rel="noopener">
        Conteúdo da disciplina <span aria-hidden="true">↗</span>
      </a>
    </p>
    <ul class="stats">
      <li class="stat"><strong>{total}</strong><span>portfólios</span></li>
      <li class="stat"><strong>{online}</strong><span>no ar</span></li>
      <li class="stat"><strong>{tech_count}</strong><span>tecnologias</span></li>
    </ul>
  </header>

  <main>
    <section class="section" aria-labelledby="mural-title">
      <h2 id="mural-title" class="section__title">Portfólios</h2>
      <div class="grid">
{cards_html}
      </div>
    </section>

    <section class="section section--tech" aria-labelledby="tech-title">
      <h2 id="tech-title" class="section__title">Tecnologias da turma</h2>
      <p class="section__lead">
        O que os alunos usaram para construir seus portfólios e atividades. O trio
        HTML + CSS + GitHub Pages é o padrão; Python é a linguagem de fundo da disciplina.
      </p>
      <ul class="techlist">
{tech_html}
      </ul>
    </section>
  </main>

  <footer class="footer">
    <p>
      Conteúdo da disciplina em
      <a href="https://algoritmos4all.github.io" target="_blank" rel="noopener">algoritmos4all.github.io</a>
    </p>
    <p>Feito para celebrar as entregas da turma de Algoritmos e Programação · UNIPAMPA</p>
  </footer>
</body>
</html>
"""

    os.makedirs(os.path.join(ROOT, "images"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)

    for index, p in enumerate(PORTFOLIOS):
        with open(os.path.join(ROOT, "images", f"{p['slug']}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_cover(p, index))

    with open(os.path.join(ROOT, "data", "portfolios.json"), "w", encoding="utf-8") as f:
        json.dump(PORTFOLIOS, f, ensure_ascii=False, indent=2)

    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

    print(
        f"OK: {total} capas SVG, data/portfolios.json e index.html gerados "
        f"({online} no ar, {tech_count} tecnologias)."
    )


if __name__ == "__main__":
    build()
