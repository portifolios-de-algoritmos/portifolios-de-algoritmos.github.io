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
            "Abrir a permissão de todos os links do Drive e do Docs para \"qualquer pessoa com o link\": hoje vários abrem só com login (erro 401) e barram os tutores.",
            "Publicar os arquivos .py reais no repositório e exibi-los na página: o único código mostrado hoje é um exemplo ilustrativo (a classe Motor), não as soluções entregues.",
            "Confirmar que a transcrição digital dos exercícios em papel está acessível, de preferência como .py versionado, e não como PDF fechado no Drive.",
            "Preencher o README.md (hoje vazio) com nome, curso, objetivo do portfólio e link do site.",
        ],
    },
    {
        "slug": "andressa-almada",
        "nome": "Andressa Almada",
        "iniciais": "AA",
        "curso": "Engenharia",
        "intro": "Portfólio final com 7 atividades e questões extras, cada entrega em página própria com objetivo, código e resultados.",
        "tech": ["Python", "HTML", "CSS", "JavaScript"],
        "url": "https://andressaalmada.github.io/Portif-lio-Algoritmo-Programa-o/",
        "status": "online",
        "sugestoes": [
            "Dar conteúdo próprio às questões extras: os cartões 8 a 12 apenas reaproveitam os links das atividades 1, 2, 3 e 5, então quem clica não encontra a questão anunciada.",
            "Aplicar realce de sintaxe aos blocos de código das páginas de entrega (hoje o código aparece em texto puro, sem coloração).",
            "Publicar cada solução também como arquivo .py no repositório, além do código embutido nas páginas.",
            "Retirar do ar ou redirecionar o site antigo do tutorial (andressaalmadaaluno-prog.github.io), para o portfólio não ficar dividido em dois endereços.",
        ],
    },
    {
        "slug": "diogo",
        "nome": "Diogo",
        "iniciais": "DI",
        "curso": "Engenharia de Telecomunicações",
        "intro": "24 atividades em Python num visualizador próprio, com realce de sintaxe e modal de arquivos.",
        "tech": ["Python", "JavaScript", "HTML", "CSS", "IA"],
        "url": "https://sudodiogo.github.io",
        "status": "online",
        "sugestoes": [
            "Corrigir a atividade p24 (Projeto Final): os arquivos de relatório, print e hash dão 404; adicionar os arquivos ou ajustar os caminhos no projects.js e alinhar rótulo e extensão do print (.png x .pdf).",
            "Adicionar conteúdo de reserva sem JavaScript (um <noscript> e tratamento de erro no carregamento do projects.js), para a seção não ficar presa em \"carregando projetos...\".",
            "Concluir a conversão das listas ainda em PDF (p04, p05, p06, p10, p12, p13, p14) para .py exibidos no visualizador com realce, que já existe.",
            "Transcrever os exercícios em papel (p08) para .py ou texto, mantendo o PDF como complemento.",
        ],
    },
    {
        "slug": "eduardo-moura",
        "nome": "Eduardo Moura",
        "iniciais": "EM",
        "curso": "",
        "intro": "Portfólio acadêmico com 7 atividades, do catálogo esportivo à análise de treliças planas.",
        "tech": ["Python", "HTML", "CSS"],
        "url": "https://eduzin-spm.github.io/Portifolio-Algoritimos",
        "status": "online",
        "sugestoes": [
            "Publicar o código como .py e exibi-lo na página com realce: hoje quase tudo está em PDF, inclusive \"Código Python.pdf\" e até arquivos CSV/JSON convertidos para PDF; os scripts chatgpt.py e gemini.py da Atividade 2 mostram o caminho certo.",
            "Renomear os arquivos sem espaços nem acentos (ex.: \"Relatório Catálogo esportivo .pdf\" tem até um espaço antes da extensão), deixando os links menos frágeis.",
            "Adicionar uma seção \"Sobre\" com nome completo e curso (hoje o nome aparece só no rodapé) e um enunciado curto por atividade.",
            "Trocar o título genérico \"Portfólio Acadêmico\" por um que identifique o autor e a disciplina.",
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
            "Corrigir o link de repositório quebrado no rodapé: aponta para /portfolio (404); o endereço correto é /portifolio.",
            "Adicionar um botão de copiar nos blocos de código: o realce de sintaxe já está pronto, falta a cópia para a área de transferência.",
            "Preencher o link do repositório por atividade, apontando para os .py correspondentes (os projetos de engenharia já têm repositórios próprios), em vez de só o link único do site.",
            "Corrigir o idioma da atividade \"gerar versões de código\", cujo enunciado da versão em português está em inglês.",
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
            "Corrigir com urgência os botões das tarefas 05 a 18: hoje apontam para pastas sem index.html e retornam 404 (14 das 18 tarefas inacessíveis); apontar cada um para um arquivo real, como já acontece nas tarefas 01 a 04.",
            "Exibir no site os arquivos .py que já estão no repositório, como texto com realce de sintaxe, em vez de manter o código só em PDF.",
            "Em cada tarefa, acrescentar o enunciado e uma breve explicação da solução, além da frase-resumo atual.",
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
            "Proteger a renderização contra descricao indefinida (atividade.descricao || ''): hoje 22 das 23 páginas de detalhe quebram a descrição por falta desse campo.",
            "Preencher a descrição de verdade nas atividades (enunciado, explicação e o código em bloco com realce), começando por substituir o texto de teste da atividade 1, aproveitando o highlight.js já integrado.",
            "Remover ou proteger o admin.html, hoje público; se mantido, atualizá-lo para os campos atuais (titulo/descricao/pdf).",
            "Ajustar a identidade: trocar \"Projetos\" e \"Desenvolvimento Web\" por algo condizente com Algoritmos e Programação (Python).",
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
            "Ligar o card \"Atividade 01\" à página local que já existe (Atividade1/index.html), em vez de um Google Docs que exige login (401).",
            "Padronizar nomes de pasta sem espaços e alinhar os links da grade: os exercícios 6 e 7 têm pasta com espaço no nome (404) e os exercícios 8 a 10 não existem.",
            "Transformar as subpáginas de exercício em conteúdo real (um exercício por página), em vez de cópias da grade de atividades.",
            "Mostrar o código com realce de sintaxe de verdade e disponibilizar os .py no repositório, com enunciado e explicação por exercício; criar uma seção \"Sobre\".",
        ],
    },
    {
        "slug": "julia-rios",
        "nome": "Julia Rios",
        "iniciais": "JR",
        "curso": "",
        "intro": "Trabalhos organizados em quatro seções: algoritmos, vetores, engenharia e inteligência artificial.",
        "tech": ["Python", "HTML", "CSS"],
        "url": "https://meus-trabalhos-de-programacao.github.io/trabalhos-programa-o",
        "status": "online",
        "sugestoes": [
            "Corrigir o botão da seção \"Inteligência Artificial e Desenvolvimento\": ele aponta para engenharia/ em vez de ia/, escondendo a seção de IA que já está publicada e completa.",
            "Corrigir o link da \"Lista de 10 exercícios da Introdução a Algoritmos\": o arquivo apontado não existe (404) e o nome sugere que era o PDF de outra atividade.",
            "Exibir o código como texto com realce de sintaxe e publicar os .py no repositório: hoje todas as entregas estão presas em PDF.",
            "Simplificar os nomes dos PDFs (espaços, acentos e parênteses cortados, como \"...LLMs (1.pdf\"), que tendem a gerar links quebrados.",
            "Completar a seção \"Sobre Mim\" com curso e objetivo do portfólio.",
        ],
    },
    {
        "slug": "lorena-christello",
        "nome": "Lorena Christello",
        "iniciais": "LC",
        "curso": "Engenharia Mecânica",
        "intro": "Portfólio com enunciado, datas e prazos por atividade, entregas locais e comentários dos tutores.",
        "tech": ["Python", "HTML", "CSS", "IA"],
        "url": "https://lorenachristello-aluna.github.io/algoritmos-e-programacao/",
        "status": "online",
        "sugestoes": [
            "Mostrar o código na própria página com realce de sintaxe: as resoluções estão todas em PDF na pasta documentos/; publicar também os .py no repositório.",
            "Atualizar os campos desatualizados, como o \"Prazo de Entrega: Em breve\" da atividade 3, e revisar pequenos erros de digitação (\"Resulução\", \"Exerício\").",
            "Padronizar os nomes dos documentos (ex.: atividade615_exercicio.pdf destoa do padrão atividadeN_*.pdf).",
            "Dividir a página única em seções navegáveis por atividade ou adicionar um índice no topo: a home já está bem longa e seguirá crescendo.",
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
            "Sincronizar os links do index.html com os nomes reais dos arquivos (renomeados com underscore): muitos hoje dão 404. Ao renomear no repositório, atualizar sempre o index.html.",
            "Linkar os .py que já existem mas estão ocultos (problema-1, problema-2, simulador) e corrigir ou remover o link evolucao-tecnica/app.py, que aponta para arquivo inexistente.",
            "Continuar tirando o código dos PDFs: onde a pasta só tem PDF, publicar o .py e exibi-lo com o realce de sintaxe que já está configurado (Prism.js).",
            "Criar um README.md na raiz com nome, disciplina, índice das atividades e o link do site publicado.",
            "Eliminar a pasta duplicada \"modularização\" (acentuada) e unificar portal-alegrete e portal-alegrete-novo em uma única versão.",
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
            "Converter A08 e A10 de .heic para .jpg/.png: hoje essas evidências não abrem no navegador (o próprio site só oferece download).",
            "Aplicar realce de sintaxe ao visualizador de código que já existe (o código entra em <pre> puro, sem coloração).",
            "Converter as listas de exercícios de Python ainda em PDF (A05, A09) para .py exibido como texto.",
            "Adicionar a cada cartão um trecho de enunciado (\"o que foi pedido\") e uma frase de \"o que eu fiz\".",
            "Transformar A12 e A21 em galeria com legendas e acertar a inconsistência da trilha de progresso (final entregue x itens ainda \"em andamento\").",
        ],
    },
    {
        "slug": "maria-frandalozzo",
        "nome": "Maria Luisa Frandalozzo",
        "iniciais": "ML",
        "curso": "Engenharia Elétrica",
        "intro": "Mais de 20 atividades documentadas, do diagnóstico inicial ao projeto final, com pseudocódigo e código Python embutidos.",
        "tech": ["Python", "HTML", "CSS", "JavaScript"],
        "url": "https://mariafrandalozzoaluno-cpu.github.io",
        "status": "online",
        "sugestoes": [
            "Escapar o caractere < nos códigos embutidos (usar &lt;): nos exercícios 11 e 15 da atividade 4 o código aparece cortado porque o navegador interpreta \"< valor\" como início de tag HTML.",
            "Substituir o placeholder \"[Espaço Reservado para Anexar suas Imagens Laterais Depois]\" pelas imagens de execução ou removê-lo.",
            "Versionar os .py no repositório: hoje o código existe só embutido na página e nos botões \"Baixar .PY\".",
            "Aplicar realce de sintaxe aos blocos de código e conferir a numeração das atividades (13, 15, 21 e 23 não aparecem na lista).",
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
            "Converter as listas de Python ainda em PDF (A02, A03, A07) para .py exibido com realce, que o site já suporta muito bem.",
            "Trocar os .docx da A04 por formato visualizável (.py, .md ou PDF), pois .docx não abre dentro do modal.",
            "Transcrever a A06 (5 exercícios em papel) para .py, mantendo as fotos ao lado, como já feito na atividade de vetores/listas.",
            "Corrigir a tecnologia \"cahtgpt\" (digitação trocada) para \"chatgpt\".",
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
            "Substituir os textos de marcador dos três cartões (\"[Nome da Atividade]\") por títulos e descrições reais, começando pelo cartão 1, cujo PDF já está no ar.",
            "Trocar os links de exemplo dos cartões 2 e 3 por entregas reais, ou remover os cartões enquanto não houver conteúdo.",
            "Listar uma entrega por atividade do semestre, ampliando o catálogo além de um único arquivo.",
            "Publicar o código como .py no repositório e/ou em bloco de código na página, sem depender só de PDF.",
            "Preencher a seção \"Sobre\" com nome, curso e contato do autor, e adicionar enunciado por atividade.",
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
            "Corrigir o caminho dos 7 links de PDF para a pasta arquivos/: hoje todos os botões \"Abrir Documento PDF\" apontam para a raiz e retornam 404, deixando o portfólio sem nenhum documento acessível.",
            "Acertar o link do item 2 (arquivo inexistente) e renomear os PDFs \"Documento sem título\" para nomes que identifiquem a atividade.",
            "Alinhar as etiquetas de tecnologia ao conteúdo real (C, Python) e corrigir \"Ponde\" para \"Ponte de Wheatstone\".",
            "Reapresentar código C na página (bloco com realce ou link para .c), reforçando o foco na linguagem, e continuar cadastrando trabalhos até cobrir o semestre.",
        ],
    },
    {
        "slug": "vinicius-moletta",
        "nome": "Vinícius Moletta",
        "iniciais": "VM",
        "curso": "Engenharia Elétrica",
        "intro": "Jornada acadêmica 2026: 15 trabalhos com enunciado, código realçado e copiável e saída esperada.",
        "tech": ["HTML", "CSS", "JavaScript", "Python"],
        "url": "https://viniciusmolettaaluno-lang.github.io/jornada-academica-2026/",
        "status": "online",
        "sugestoes": [
            "Versionar o código de cada trabalho como .py no repositório (e/ou exibir o código completo na página): hoje o bloco realçado traz só um trecho de exemplo, e o código inteiro segue só nos codigo*.pdf.",
            "Criar um README.md na raiz com nome, disciplina, link do site e índice dos 15 trabalhos.",
            "Renomear a pasta trabalhos/algoritimos para trabalhos/algoritmos, corrigindo os links.",
            "Transcrever o conteúdo de fotostrabalho05.pdf para o trabalho5.html, mantendo as fotos como apoio.",
            "Ajustar a mensagem de fallback do botão \"Copiar\" para aparecer apenas em caso de erro (hoje surge mesmo quando a cópia dá certo).",
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
        "status": "wip",
        "sugestoes": [
            "Restaurar o conteúdo do portfólio (recuperar do histórico do Git ou reconstruir): a versão no ar hoje é um template inacabado, sem CSS, e perdeu todo o conteúdo anterior.",
            "Corrigir nome, curso e e-mail (a página atual exibe dados de exemplo de outra pessoa) e restabelecer a estrutura HTML completa com estilo.",
            "Trazer o código para dentro do site (blocos copiáveis ou arquivos .py versionados), em vez de depender de links externos.",
            "Preencher os campos de entrega (link do repositório, URL publicada e hash do commit), substituindo qualquer link de exemplo (href=\"#\").",
            "Transcrever os \"5 exercícios em papel\" e, se mantiver as fotos, exibi-las como galeria; se voltar a usar o Drive, padronizar as permissões para \"qualquer pessoa com o link\".",
        ],
    },
    {
        "slug": "bernardo-bender",
        "nome": "Bernardo Bender",
        "iniciais": "BB",
        "curso": "",
        "intro": "Portfólio publicado com 5 entregas, mas a URL principal ainda retorna 404.",
        "tech": ["Python", "HTML", "CSS"],
        "url": "https://bernardobenderaluno-hue.github.io/atividadefinal/",
        "status": "wip",
        "sugestoes": [
            "Renomear index2.html para index.html (ou defini-lo como página inicial): o conteúdo já existe, mas a URL principal retorna 404 porque o arquivo tem outro nome.",
            "Corrigir os links \"Ver Código no GitHub\" para o repositório atual (atividadefinal), em vez de depender do redirecionamento do repositório antigo.",
            "Mostrar o código .py embutido na página, em bloco copiável, além do link para o GitHub.",
            "Adicionar nome completo e curso na seção \"Sobre\".",
        ],
    },
    {
        "slug": "kaua-santos",
        "nome": "Kauã Lopes dos Santos",
        "iniciais": "KS",
        "curso": "",
        "intro": "Acervo com 55 arquivos em 21 atividades, com busca, visualização por pastas e executor de Python.",
        "tech": ["Python", "JavaScript", "HTML", "CSS"],
        "url": "https://kauals001.github.io/KauaLS001.io/",
        "status": "online",
        "sugestoes": [
            "Preencher a descrição de cada publicação com um enunciado curto explicando a atividade (o campo existe no posts.json, mas está vazio em todas as 55 entradas).",
            "Converter os códigos entregues em PDF para .py: o site já tem visualizador com realce e até executor de Python, mas a maior parte do código segue presa em PDF.",
            "Corrigir a ortografia nos títulos e nomes de arquivo (\"análise\" no lugar de \"analize\", \"algoritmo\" no lugar de \"algoritimo\", \"claude\" no lugar de \"cloude\").",
            "Remover ou proteger o painel \"Admin\", hoje linkado publicamente no topo do site.",
            "Retirar do ar ou redirecionar o endereço antigo (kauasantosaluno-tech.github.io), que continua publicado com a versão anterior do acervo.",
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
            "Confirmar se a organização \"Algoritmos-e-Programacao\" deve ser o índice da turma; se sim, publicar uma página índice nesse endereço.",
            "Caso contrário, retirar este endereço da lista de portfólios de alunos: a organização existe mas está vazia (0 repositórios) e não corresponde a um aluno.",
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
