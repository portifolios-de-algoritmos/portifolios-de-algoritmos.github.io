# Mural de Portfólios · Algoritmos e Programação

Página que reúne e apresenta os portfólios criados pelos alunos da disciplina de
Algoritmos e Programação. Cada aluno foi desafiado a transformar suas entregas do
semestre em um portfólio próprio; este site é a vitrine de todos eles, com uma
capa colorida gerada para cada um e um resumo das tecnologias usadas pela turma.

## Como funciona

O site é **estático** (HTML + CSS), pronto para o GitHub Pages. Tudo é gerado a
partir de uma única fonte de verdade: a lista `PORTFOLIOS` em `scripts/generate.py`.

```
scripts/generate.py     # fonte de dados + gerador
data/portfolios.json    # dados exportados (gerado)
images/<slug>.svg       # uma capa SVG por aluno (gerada)
index.html              # a página do mural (gerada)
styles.css              # estilo colorido e lúdico (escrito à mão)
```

As capas são **arte SVG generativa**: a partir do nome de cada aluno o script deriva
uma cor (matizes distribuídos por ângulo áureo), monta um gradiente, posiciona blobs e
as iniciais. São determinísticas, leves e nunca dependem de serviço externo.

## Regerar o site

Depois de editar os dados em `scripts/generate.py` (adicionar aluno, corrigir nome,
trocar status ou tecnologias), rode:

```bash
python3 scripts/generate.py
```

Isso reescreve `images/*.svg`, `data/portfolios.json` e `index.html`.

## Status dos portfólios

Cada card mostra um selo de status:

- **No ar** (`online`): portfólio publicado e acessível.
- **Em construção** (`wip`): página existe, conteúdo ainda incompleto.
- **Indisponível** (`offline`): página fora do ar (ex.: 404); o card é mostrado
  com capa acinzentada e botão desabilitado.

## Visualizar localmente

Como tudo é estático e sem `fetch`, basta abrir `index.html` no navegador. Para
servir via HTTP local:

```bash
python3 -m http.server
# acesse http://localhost:8000
```
