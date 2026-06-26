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
        "sugestoes": [
            "Tirar o código de dentro dos PDFs do Google Drive: publicar os arquivos .py no repositório e exibi-los na página com realce de sintaxe.",
            "Abrir a permissão de todos os links do Drive e do Docs para \"qualquer pessoa com o link\", evitando barreira de login para os tutores.",
            "Transcrever a resolução feita em papel para código digital, mantendo a foto apenas como complemento.",
            "Incluir o enunciado de cada atividade antes do link, para que um leitor não técnico entenda o problema sem abrir o anexo.",
        ],
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
        "sugestoes": [
            "Transformar o site num portfólio de verdade: hoje é um tutorial genérico de Python, falta a seção \"Atividades\" com cada exercício e projeto entregues, com data e tema.",
            "Publicar o código das próprias soluções (.py) e exibi-lo com realce de sintaxe, no lugar dos exemplos genéricos.",
            "Para cada atividade, escrever o enunciado, a abordagem usada e o resultado.",
            "Adicionar uma seção \"Sobre\" identificando a autora, o curso e o objetivo do portfólio.",
        ],
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
        "sugestoes": [
            "Corrigir os links quebrados da atividade p11: o projects.js aponta para arquivos .yf, mas no repositório eles são .py (v1.py a v4.py).",
            "Converter as soluções que só existem em PDF em arquivos .py e exibi-las na página com realce de sintaxe.",
            "Mostrar um conteúdo de reserva quando o JavaScript não carrega: hoje, se o projects.js falhar, a seção fica eternamente em \"carregando projetos...\".",
            "Transcrever os exercícios feitos em papel (p08) para código digital, mantendo a foto como complemento.",
        ],
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
        "sugestoes": [
            "Publicar o código de cada atividade na própria página, com realce de sintaxe e botão de copiar: hoje o portfólio é bonito, mas não mostra uma única linha de código.",
            "Tornar o conteúdo autossuficiente: incluir o enunciado completo e uma explicação da solução, sem depender do Google Classroom, que é fechado para visitantes.",
            "Digitalizar e transcrever os exercícios feitos em papel, em vez de só apontar para o Classroom.",
            "Adicionar link para o repositório com os arquivos .py de cada atividade.",
        ],
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
        "sugestoes": [
            "Corrigir os links quebrados com urgência: todos os botões \"Pasta da Tarefa\" retornam 404 (falta um index.html dentro de cada pasta), então o site inteiro está inacessível, mesmo parecendo completo.",
            "Eliminar os arquivos ZIP: descompactar e publicar o código como arquivos .py legíveis, em vez de forçar o avaliador a baixar e extrair.",
            "Tirar o código de dentro dos PDFs e apresentá-lo como texto copiável com realce de sintaxe.",
            "Adicionar a cada tarefa o enunciado e uma breve explicação da solução.",
        ],
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
        "sugestoes": [
            "Corrigir o bug de dados: as páginas de detalhe mostram \"Atividade undefined\" porque o atividades.json não tem os campos numero, descricao e classroom usados por atividade.html.",
            "Publicar o código de cada atividade com realce de sintaxe: hoje o portfólio de uma disciplina de Python não exibe nenhuma linha de código.",
            "Adicionar enunciado e explicação por atividade, com a entrega correspondente (código .py, foto transcrita ou relato).",
            "Ajustar a identidade (os selos \"HTML & CSS / Web Dev\" não condizem com Python) e remover o admin.html exposto publicamente.",
        ],
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
        "sugestoes": [
            "Corrigir os links quebrados: as duas atividades retornam 404 (as pastas Atividade1 e Atividade2 não existem), então 100% do conteúdo está inacessível hoje.",
            "Publicar o código como texto copiável com realce de sintaxe (a fonte Fira Code já está carregada na página).",
            "Adicionar o enunciado e uma explicação de cada atividade, mais um link para o repositório com os .py.",
            "Completar o portfólio com todas as atividades do semestre e uma seção \"Sobre\".",
        ],
    },
    {
        "slug": "lorenzo-ximendes",
        "nome": "Lorenzo Ximendes",
        "iniciais": "LX",
        "curso": "Engenharia Mecânica",
        "intro": "Painel com 11 atividades concluídas, cada uma com problema, abordagem e entregáveis.",
        "tech": ["JavaScript", "Python", "HTML", "CSS"],
        "url": "https://lorenzoximendesaluno-dotcom.github.io/portifolio-de-algoritmos/",
        "status": "online",
        "sugestoes": [
            "Tirar o código de dentro dos PDFs (muitas pastas só têm index.pdf) e publicá-lo como .py, exibindo-o no site com realce de sintaxe.",
            "Criar um README.md na raiz do repositório com nome, disciplina, índice das atividades e o link do site publicado.",
            "Transcrever os exercícios fotografados (pasta exercicios-em-papel) para arquivos .py, mantendo as fotos como registro do raciocínio.",
            "Padronizar nomes de arquivos e pastas (evitar espaços, parênteses e acentos) e consolidar portal-alegrete e portal-alegrete-novo em uma única versão.",
        ],
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
        "sugestoes": [
            "Substituir os PDFs de código por arquivos .py e exibir o código na página com realce de sintaxe (a fonte DM Mono já está carregada).",
            "Adicionar o enunciado de cada atividade num trecho expansível (\"o que foi pedido\" e \"o que eu fiz\").",
            "Concluir as 4 atividades pendentes e revisar os itens marcados como \"Em andamento\".",
            "Transformar os conjuntos de imagens (A12, A21) em uma galeria com legendas e transcrever para .py o que está apenas fotografado (A08).",
        ],
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
        "sugestoes": [
            "Tirar o código dos PDFs e da dupla extensão \".png.pdf\": subir cada código como .py (o site já o exibe como texto) e cada imagem como .png ou .jpg.",
            "Transcrever as resoluções feitas em papel (as fotos) para código digital, mantendo a foto como evidência ao lado.",
            "Adicionar um campo \"Enunciado\" em texto no próprio cartão, sem depender dos links do Google Classroom, que exigem login.",
            "Aplicar realce de sintaxe ao visualizador de código que o site já possui.",
        ],
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
        "sugestoes": [
            "Preencher o conteúdo real: hoje os três cartões são placeholders do template (\"[Nome da Atividade]\") e o link \"entregas/trabalho1.pdf\" está quebrado.",
            "Listar todas as entregas do semestre, uma por atividade.",
            "Publicar o código como .py no repositório e/ou em bloco de código na página, em vez de depender de PDF e Drive.",
            "Adicionar enunciado e explicação acessível por atividade, e identificar o autor (nome, curso, contato) na seção \"Sobre\".",
        ],
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
        "sugestoes": [
            "Cadastrar os trabalhos que faltam: o array projects tem só 1 item, mas a página anuncia 12 trabalhos e 4 projetos finais, e os filtros ficam vazios.",
            "Corrigir ou remover o botão \"Ver Código\": o campo githubUrl está vazio, então o botão abre uma página em branco.",
            "Ajustar as estatísticas para refletir o conteúdo real enquanto os trabalhos não são adicionados.",
            "Aplicar realce de sintaxe ao bloco de código C do modal, que hoje é texto cru.",
        ],
    },
    {
        "slug": "vinicius-moletta",
        "nome": "Vinícius Moletta",
        "iniciais": "VM",
        "curso": "Engenharia Elétrica",
        "intro": "Jornada acadêmica 2026: 14 trabalhos com enunciado, código copiável e saída esperada.",
        "tech": ["HTML", "CSS", "JavaScript", "Python"],
        "url": "https://viniciusmolettaaluno-lang.github.io/jornada-academica-2026/",
        "status": "online",
        "sugestoes": [
            "Eliminar o código em PDF: substituir os arquivos codigo*.pdf por .py reais, reservando o PDF apenas para relatórios e enunciados.",
            "Adicionar um README.md na raiz com nome, disciplina, link do site e índice dos 14 trabalhos.",
            "Aplicar realce de sintaxe aos blocos de código, mantendo o botão \"Copiar\" que já funciona bem.",
            "Corrigir ou remover os links \"Ver no Google Colab\" (sem URL real), transcrever o conteúdo de fotostrabalho05.pdf e renomear a pasta \"algoritimos\" para \"algoritmos\".",
        ],
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
        "sugestoes": [
            "Trazer o código para dentro do site (blocos copiáveis ou arquivos .py versionados), em vez de depender 100% do Google Drive.",
            "Conferir e padronizar a permissão de todos os links do Drive para \"qualquer pessoa com o link\", para o professor e os 6 tutores não baterem em acesso negado.",
            "Preencher os campos \"COLOCAR_AQUI\" (link do repositório, URL publicada e hash do commit), que hoje sinalizam entrega inacabada.",
            "Transcrever os \"5 exercícios em papel\" e, se mantiver as fotos, exibi-las como galeria na própria página.",
        ],
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
        "sugestoes": [
            "Publicar a página: o endereço retorna 404. Conferir se o GitHub Pages está ativo e se há um index.html na branch correta.",
            "Depois de publicar, montar a estrutura mínima: lista de atividades, código em .py exibido na página e uma seção \"Sobre\".",
        ],
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
        "sugestoes": [
            "Personalizar a identidade: o template ainda se identifica como \"Diogo / Engenharia de Telecomunicações\"; trocar pelo nome e curso do Kauã.",
            "Substituir os links \"#\" por conteúdo real, começando por uma atividade já feita: publicar o .py e exibir o código em bloco copiável.",
            "Corrigir o erro de sintaxe no trecho sobre_mim.py (self] no lugar de self.), que aparece logo na vitrine.",
            "Escrever um enunciado curto para cada projeto e adicionar um README com status honesto de \"em construção\".",
        ],
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
        "sugestoes": [
            "Endereço sem página publicada (404): identificar o responsável e publicar o conteúdo, ou retirar este endereço da lista da turma.",
        ],
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


def suggestions_block(p):
    sugestoes = p.get("sugestoes") or []
    if not sugestoes:
        return ""
    n = len(sugestoes)
    rotulo = "sugestão" if n == 1 else "sugestões"
    items = "".join(f"<li>{esc_html(s)}</li>" for s in sugestoes)
    return f"""
          <details class="card__sug">
            <summary>Como melhorar <span class="card__sug-count">{n} {rotulo}</span></summary>
            <ol class="card__sug-list">{items}</ol>
          </details>"""


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
          {suggestions_block(p)}
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
      portfólio próprio. Esta página reúne e apresenta todos eles, num só lugar. Cada card
      traz também sugestões concretas de melhoria, abertas no botão <strong>Como melhorar</strong>.
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

    <section class="section section--guia" aria-labelledby="guia-title">
      <h2 id="guia-title" class="section__title">Como deixar seu portfólio melhor</h2>
      <p class="section__lead">
        Quem visita estes portfólios não é só o professor: são também os 6 tutores da disciplina
        e pessoas de formações variadas, muitas sem nenhuma vivência em programação. Um bom
        portfólio precisa ser entendido por todos eles, sem exigir login, download ou conhecimento
        prévio. Os pontos abaixo resumem o que mais aparece nas sugestões de cada card.
      </p>
      <ul class="guia">
        <li class="guia__item">
          <h3 class="guia__name">Código é texto, não imagem</h3>
          <p>Mostre o código na própria página, em bloco copiável e com realce de sintaxe. Evite código preso em PDF, em ZIP ou em foto: ninguém consegue copiar, executar ou revisar.</p>
        </li>
        <li class="guia__item">
          <h3 class="guia__name">Versione os .py no repositório</h3>
          <p>Cada solução deve existir como arquivo .py no GitHub. O PDF fica reservado para o que é mesmo documento: relatórios, enunciados e reflexões.</p>
        </li>
        <li class="guia__item">
          <h3 class="guia__name">Nada de muros de login</h3>
          <p>Conteúdo no Google Classroom ou no Drive fechado é invisível para tutores e visitantes. Traga o material para o site ou libere o acesso como \"qualquer pessoa com o link\".</p>
        </li>
        <li class="guia__item">
          <h3 class="guia__name">Conte o que era o problema</h3>
          <p>Para cada atividade, escreva o enunciado, a ideia da solução e o resultado. Assim um leitor não técnico entende o trabalho sem precisar ler o código.</p>
        </li>
        <li class="guia__item">
          <h3 class="guia__name">Papel também vira código</h3>
          <p>Exercícios feitos à mão podem entrar como foto, mas transcreva a solução para .py ou pseudocódigo digital. A foto é o registro do raciocínio, não a entrega final.</p>
        </li>
        <li class="guia__item">
          <h3 class="guia__name">Imagens em galeria, com legenda</h3>
          <p>Telas de execução e saídas do programa ajudam quem não vai rodar o código. Agrupe-as numa galeria e explique em uma linha o que cada imagem mostra.</p>
        </li>
        <li class="guia__item">
          <h3 class="guia__name">Teste cada link antes de entregar</h3>
          <p>Botão que leva a 404, página de detalhe vazia ou \"Ver código\" sem destino derrubam um portfólio que parecia pronto. Clique em tudo antes de considerar concluído.</p>
        </li>
        <li class="guia__item">
          <h3 class="guia__name">Sem placeholder de template</h3>
          <p>Troque os textos de exemplo (\"[Nome da Atividade]\", nome de outra pessoa, estatísticas que não batem) por conteúdo real. Identifique-se: nome, curso e objetivo.</p>
        </li>
      </ul>
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
