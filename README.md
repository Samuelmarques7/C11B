# C11: Ciência de Dados com Python

Exercícios e estudos da disciplina **C11 (Ciência de Dados com Python)** do curso de Engenharia de Software do **Inatel**.

O repositório acompanha a evolução da disciplina: começa pelas estruturas básicas do Python, passa por NumPy e pandas para manipular dados, chega à visualização com Matplotlib e Seaborn e termina com séries temporais.

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c)
![Seaborn](https://img.shields.io/badge/Seaborn-4c72b0)
![statsmodels](https://img.shields.io/badge/statsmodels-8c1d40)

---

## Sumário

- [O que tem aqui](#o-que-tem-aqui)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Conteúdo por tema](#conteúdo-por-tema)
- [Datasets](#datasets)
- [Como executar](#como-executar)
- [Tecnologias](#tecnologias)

---

## O que tem aqui

- **Fundamentos de Python:** listas, conjuntos, dicionários, laços e entrada de dados.
- **NumPy:** criação e manipulação de arrays, operações vetorizadas, filtros com máscaras booleanas e análise de datasets em formato de matriz.
- **pandas:** Series, DataFrames, `loc` e `iloc`, tratamento de dados ausentes, funções customizadas com `apply`, agrupamento com `groupby` e geração de novos arquivos.
- **Visualização com Matplotlib:** gráficos de linha, barras, pizza, dispersão e subplots.
- **Visualização estatística com Seaborn:** histogramas com KDE, boxplots, heatmaps de correlação e regressões (`regplot`).
- **Séries temporais:** leitura de datas, frequência mensal e decomposição em tendência, sazonalidade e resíduo com `statsmodels`.

---

## Estrutura do repositório

```
C11B/
├── Cap3/                        # Fundamentos de Python: listas, conjuntos e dicionários
├── Cap4_Partes 2 e 3/           # NumPy: criação, soma, concatenação e remodelagem de arrays
├── Cap4_Partes_3_e_4/           # NumPy aplicado ao dataset de missões espaciais
├── treino/                      # Treino com NumPy no dataset de países
├── Exercicio_para_prova/        # Revisão para a prova com o dataset de países
├── ExercicioPosprova/           # Exercícios de revisão após a prova
├── Pandas/                      # Aulas de pandas: Series, DataFrame, slicing, ausentes, groupby
├── aulaPandas2/                 # Recursos extras de pandas vistos em aula
├── PandasParte1 e parte2/       # Lista de exercícios: Series e DataFrames
├── PandasParte3 e parte4/       # Lista de exercícios: filtros, buscas em texto e agrupamentos
├── Cap 6 partes 1 e 2/          # Visualização com Matplotlib
├── Cap 6 partes 3 e 4/          # Visualização com Seaborn
├── Seaborn/                     # Aulas de Seaborn: estilos, histograma, boxplot, heatmap, regplot
├── Cap 7/                       # Séries temporais e decomposição sazonal
├── pyproject.toml               # Dependências do projeto
└── uv.lock                      # Versões travadas das dependências (uv)
```

---

## Conteúdo por tema

### 1. Fundamentos de Python (`Cap3/`)

Exercícios com as estruturas de dados nativas da linguagem:

- Fatiamento de listas (classificação de um campeonato).
- Operações entre conjuntos: união e interseção dos produtos de duas lojas, ingredientes que faltam para uma receita.
- Dicionários para guardar dados de alunos e produtos, incluindo situação de aprovação e valor total em estoque.
- Leitura de dados do usuário e cálculos simples, como média de idade e maior e menor peso.

### 2. NumPy (`Cap4_*`, `treino/`, `Exercicio_para_prova/`, `ExercicioPosprova/`)

- Criação de arrays com `ones`, `arange` e números aleatórios, soma, concatenação, ordenação e `reshape`.
- Uso de máscaras booleanas para filtrar dados sem laços.
- Análise do dataset **space.csv** só com NumPy:
  - porcentagem de missões bem-sucedidas;
  - custo médio das missões com valor conhecido;
  - missões feitas pelos EUA e lançadas da Rússia;
  - missão mais cara da SpaceX e de todo o dataset;
  - quantidade de missões por empresa.
- Análise do dataset **paises.csv**: regiões do mundo, taxa média de alfabetização, países da América do Norte e maior renda per capita da América Latina e Caribe.

### 3. pandas (`Pandas/`, `aulaPandas2/`, `PandasParte*`)

- Criação de Series e DataFrames e operações entre Series (com `add` e `fill_value`).
- Seleção de dados com `loc` (rótulos) e `iloc` (posições).
- Tratamento de dados ausentes.
- Funções customizadas aplicadas a colunas.
- Agrupamento por região com `groupby`, contagem, soma e estatísticas descritivas.
- Buscas em texto com `str.contains`.
- Exportação de novos arquivos a partir de um dataset.

### 4. Visualização com Matplotlib (`Cap 6 partes 1 e 2/`)

| Exercício | Gráfico | Pergunta respondida |
|---|---|---|
| 1 | Linhas | Mortalidade x natalidade na América do Norte |
| 2 | Barras | Empresas diferentes com missões nos EUA e na China |
| 3 | Pizza | Missões da Roscosmos que deram certo e que falharam |
| 4 | Barras | 5 empresas com mais falhas |
| 5 | Dispersão | Renda per capita x alfabetização na América Latina (tamanho do ponto = população) |
| 6 | Pizza | Foguetes ativos x aposentados |
| 7 | Linhas | PIB per capita x telefones por mil habitantes na Europa Ocidental |
| 8 | Subplots | Top 5 empresas em sucessos e em falhas, lado a lado |

### 5. Visualização estatística com Seaborn (`Seaborn/`, `Cap 6 partes 3 e 4/`)

| Exercício | Gráfico | Análise |
|---|---|---|
| 1 | Heatmap | Correlação entre as medidas da espécie *setosa* (Iris) |
| 2 | Histograma + KDE | Distribuição das idades no Titanic por sexo |
| 3 | Boxplot | Idades no Titanic por classe e sexo |
| 4 | Regplot | Potência x consumo de combustível (mpg) |
| 5 | Heatmap | Correlação entre PIB, alfabetização, mortalidade infantil e telefones |
| 6 | Boxplot | PIB per capita: América Latina x Europa Ocidental |
| 7 | Regplot | Alfabetização x mortalidade infantil |
| 8 | Boxplot | Custo das missões: foguetes ativos x aposentados |

A pasta `Seaborn/` também traz as aulas de base com os datasets `tips` e `penguins`.

### 6. Séries temporais (`Cap 7/`)

- Leitura de séries com datas como índice e frequência mensal.
- Visualização da evolução ao longo do tempo.
- Decomposição aditiva com `seasonal_decompose` para separar **tendência**, **sazonalidade** e **resíduo**.
- Séries analisadas: passageiros de avião (1958 a 1960), emissões de CO₂ e índice de volume de vendas do varejo brasileiro.

---

## Datasets

| Arquivo | Conteúdo |
|---|---|
| `paises.csv` / `paises_v2.csv` | Indicadores de países: região, população, área, PIB per capita, alfabetização, natalidade, mortalidade, telefones |
| `space.csv` | Missões espaciais: empresa, local, data, status da missão, status do foguete e custo |
| `airtravel.csv` | Número mensal de passageiros de avião |
| `co2_emissions.csv` | Emissões de CO₂ ao longo do tempo |
| `retail_index_br.csv` | Índice de volume de vendas do varejo brasileiro |
| Seaborn (`load_dataset`) | `iris`, `titanic`, `mpg`, `tips` e `penguins`, baixados automaticamente pela biblioteca |

---

## Como executar

**Pré-requisito:** Python 3.12 ou mais recente.

### Opção 1: com [uv](https://docs.astral.sh/uv/) (recomendado)

```bash
git clone https://github.com/Samuelmarques7/C11B.git
cd C11B
uv sync
```

### Opção 2: com pip

```bash
git clone https://github.com/Samuelmarques7/C11B.git
cd C11B
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
pip install numpy pandas matplotlib seaborn statsmodels ipython
```

### Rodando um exercício

Os scripts leem os arquivos `.csv` pelo nome, então **execute de dentro da pasta do exercício**:

```bash
cd "Cap 6 partes 3 e 4"
python "exercicio 5.py"
```

Com uv, troque `python` por `uv run python`.

Os exercícios com Seaborn baixam os datasets de exemplo na primeira execução, então precisam de internet.

---

## Tecnologias

- **Python 3.12+**
- **NumPy:** computação numérica com arrays
- **pandas:** manipulação e análise de dados tabulares
- **Matplotlib:** gráficos
- **Seaborn:** visualização estatística
- **statsmodels:** séries temporais
- **IPython:** execução interativa
- **uv:** gerenciamento de ambiente e dependências

---

## Autor

**Samuel Marques**, estudante de Engenharia de Software no Inatel.

[GitHub](https://github.com/Samuelmarques7) · [LinkedIn](https://www.linkedin.com/in/samuel-marques-2bb64033a/) · [Portfólio](https://samuelmarques7.github.io/Portifolio/)
