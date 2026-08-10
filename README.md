<div align="center">

# 📊 Digital Corporativo — Data Analytics

### Pipeline de dados corporativos desenvolvido em Python

**Transformando dados brutos em informações, indicadores e insights para apoiar decisões de negócio.**

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM%2FDatabase-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git&logoColor=white)

<br>

**SQL • Python • ETL • Data Analytics • Business Intelligence • Data Visualization • IA**

</div>

---

# 📌 Sobre o Projeto

O **Digital Corporativo — Data Analytics** é um projeto de análise de dados desenvolvido em Python com o objetivo de transformar dados corporativos armazenados em um banco **PostgreSQL** em informações estruturadas para análise e tomada de decisão.

O projeto foi desenvolvido simulando um cenário empresarial real, trabalhando com diferentes áreas do negócio, como:

- 💰 Financeiro
- 🛒 Vendas
- 👥 Clientes
- 📦 Produtos
- 👨‍💼 Vendedores
- 🧑‍💼 Recursos Humanos

A solução percorre diferentes etapas de um projeto de dados:

```text
Banco PostgreSQL
       ↓
Extração SQL
       ↓
JOINs entre tabelas
       ↓
Tratamento dos dados
       ↓
Transformação com Pandas
       ↓
Análise e criação de KPIs
       ↓
Visualização
       ↓
Dashboard
       ↓
Insights para o negócio
🎯 Objetivo do Projeto

O principal objetivo é desenvolver um pipeline completo de Data Analytics, demonstrando na prática como transformar dados transacionais em informações úteis para o negócio.

O projeto busca responder perguntas como:

🛒 Vendas
Quanto a empresa vende?
Como as vendas evoluem ao longo do tempo?
Quais vendedores apresentam melhor desempenho?
Quais produtos possuem maior volume de vendas?
Quais categorias geram maior faturamento?
Quais formas de pagamento são mais utilizadas?
👥 Clientes
Quantos clientes existem?
Qual a distribuição entre pessoas físicas e jurídicas?
Quais clientes possuem maior participação nas vendas?
Como os clientes estão distribuídos geograficamente?
📦 Produtos
Quais produtos vendem mais?
Quais produtos geram maior receita?
Qual a relação entre preço de venda e custo?
Quais categorias possuem maior desempenho?
💰 Financeiro
Quanto existe em contas a pagar?
Quanto existe em contas a receber?
Quais títulos estão em determinada situação?
Como os valores financeiros estão distribuídos?
👨‍💼 Vendedores
Quem são os vendedores?
Qual o faturamento por vendedor?
Qual vendedor apresenta maior volume de vendas?
Como relacionar o desempenho comercial às informações de RH?
🏢 Contexto do Banco de Dados

O banco utilizado pelo projeto possui diferentes schemas que representam áreas distintas da organização.

PostgreSQL
│
├── financeiro
│
├── geral
│
├── rh
│
└── vendas

Essa estrutura permite trabalhar com dados distribuídos em diferentes domínios de negócio e realizar integrações através de relacionamentos e JOINs.

🗄️ Estrutura do Banco
💰 Schema financeiro
financeiro
│
├── conta_pagar
├── conta_receber
└── situacao_titulo

Principais informações:

Contas a pagar
Contas a receber
Valor original
Valor atualizado
Vencimento
Data de pagamento
Situação do título
Forma de pagamento
👥 Schema geral
geral
│
├── bairro
├── cidade
├── contato
├── endereco
├── estado
├── pessoa
├── pessoa_fisica
├── pessoa_juridica
├── responsavel_juridico
└── tipo_contato

Responsável principalmente pelas informações cadastrais das pessoas e localização.

Permite relacionar:

Pessoa
  ↓
Pessoa Física / Jurídica
  ↓
Endereço
  ↓
Bairro
  ↓
Cidade
  ↓
Estado
🧑‍💼 Schema rh
rh
│
├── cargo
├── departamento
├── escolaridade
├── funcionario
└── lotacao

Principais informações:

Funcionários
Escolaridade
Cargo
Departamento
Salário
Data de admissão
Data de desligamento
Lotação
🛒 Schema vendas
vendas
│
├── categoria
├── forma_pagamento
├── item_nota_fiscal
├── nota_fiscal
├── parcela
└── produto

Esse schema concentra os principais dados utilizados na análise comercial.

🔗 Integração entre os Dados

Uma das partes importantes do projeto é a integração entre tabelas de diferentes schemas.

Exemplo conceitual:

                    NOTA FISCAL
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
       CLIENTE        VENDEDOR     PAGAMENTO
          │              │
          │              ▼
          │          FUNCIONÁRIO
          │              │
          │       ┌──────┴──────┐
          │       ▼             ▼
          │     CARGO      DEPARTAMENTO
          │
          ▼
     PESSOA FÍSICA
          │
          ▼
      ENDEREÇO
          │
          ▼
       CIDADE
          │
          ▼
       ESTADO

Além disso:

NOTA FISCAL
     │
     ▼
ITEM NOTA FISCAL
     │
     ▼
PRODUTO
     │
     ▼
CATEGORIA

Essa integração possibilita construir datasets analíticos mais completos.

🔄 Pipeline de Dados

O projeto foi estruturado seguindo uma arquitetura simples de pipeline:

┌───────────────────────┐
│       PostgreSQL      │
│                       │
│ Financeiro            │
│ Geral                 │
│ RH                    │
│ Vendas                │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│       EXTRAÇÃO        │
│                       │
│ SQL                   │
│ JOINs                 │
│ Consultas             │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│     TRANSFORMAÇÃO     │
│                       │
│ Pandas                │
│ Limpeza               │
│ Padronização          │
│ Tratamento            │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│        ANÁLISE        │
│                       │
│ KPIs                  │
│ Métricas              │
│ Rankings              │
│ Indicadores           │
└───────────┬───────────┘
            │
       ┌────┴────┐
       ▼         ▼
┌──────────┐ ┌──────────────┐
│Dashboard │ │ Inteligência │
│Streamlit │ │ Artificial   │
│ Plotly   │ │ Insights     │
└──────────┘ └──────────────┘
📂 Estrutura do Projeto
digital-corporativo-data-analytics/
│
├── 📄 app.py
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 .gitignore
├── 📄 .env
│
├── 📁 src/
│   │
│   ├── 📄 __init__.py
│   ├── 📄 database.py
│   ├── 📄 extraction.py
│   ├── 📄 transformation.py
│   ├── 📄 analysis.py
│   └── 📄 ai_analysis.py
│
└── 📁 docs/
    │
    └── 📄 documentação-projeto.pdf

⚠️ O arquivo .env contém informações sensíveis e deve permanecer fora do GitHub.

🧩 Responsabilidade dos Arquivos
database.py

Responsável pela conexão entre a aplicação Python e o banco PostgreSQL.

Tecnologias utilizadas:

SQLAlchemy
PostgreSQL
python-dotenv

Fluxo:

Python
  ↓
SQLAlchemy
  ↓
PostgreSQL

Também é utilizado para validar se a conexão com o banco está funcionando corretamente.

extraction.py

Responsável pela etapa de extração dos dados.

Entre suas responsabilidades:

Consultar schemas;
Identificar tabelas;
Consultar colunas;
Explorar o banco;
Executar consultas SQL;
Realizar JOINs;
Extrair informações para análise.

Exemplo:

SELECT
    nf.id,
    nf.numero_nf,
    nf.data_venda,
    nf.valor,
    nf.id_cliente
FROM vendas.nota_fiscal nf;
transformation.py

Responsável pelo tratamento dos dados após a extração.

Principais atividades:

Dados brutos
     ↓
Tratamento de nulos
     ↓
Conversão de tipos
     ↓
Padronização
     ↓
Criação de métricas
     ↓
Dataset analítico

Utiliza principalmente:

Pandas
NumPy
analysis.py

Responsável pela camada de análise.

É onde são concentradas métricas e indicadores utilizados pelo projeto.

Exemplos:

Faturamento
Ticket Médio
Quantidade de Vendas
Ranking de Vendedores
Ranking de Clientes
Desempenho por Categoria
Desempenho por Produto
ai_analysis.py

Responsável pela integração da aplicação com uma API de Inteligência Artificial.

A ideia é utilizar os indicadores gerados pelo pipeline para produzir:

interpretações;
análises;
recomendações;
insights de negócio.

Fluxo:

Indicadores
     ↓
Python
     ↓
API de IA
     ↓
Interpretação
     ↓
Recomendação

A Inteligência Artificial funciona como uma camada complementar de análise.

Os cálculos dos indicadores continuam sendo realizados pelo próprio pipeline de dados.

app.py

Responsável pela aplicação visual.

Utiliza:

Streamlit
Plotly

O objetivo é disponibilizar os resultados de forma interativa e facilitar a interpretação dos indicadores.

📊 Análises Desenvolvidas
🛒 Análise de Vendas

Indicadores trabalhados:

Faturamento
Quantidade de vendas
Evolução temporal
Ticket médio
Vendas por vendedor
Vendas por cliente
Vendas por produto
Vendas por categoria
Vendas por forma de pagamento
👨‍💼 Ranking de Vendedores

O projeto realiza a identificação dos vendedores presentes nas notas fiscais e permite relacionar esses IDs com as informações existentes no schema de RH.

Exemplo do processo:

nota_fiscal
     │
     ▼
id_vendedor
     │
     ▼
funcionario
     │
     ▼
pessoa
     │
     ▼
nome do vendedor

Essa integração permite transformar um identificador técnico em uma informação útil para análise de negócio.

👥 Perfil dos Clientes

Durante a exploração inicial da base foram identificadas:

Indicador	Quantidade
👥 Total de pessoas	15.962
👤 Pessoas físicas	14.155
🏢 Pessoas jurídicas	1.807

Distribuição:

Pessoas Físicas
14.155
████████████████████████████████████████

Pessoas Jurídicas
1.807
█████

Essas informações podem ser utilizadas para análises de segmentação e comportamento de clientes.

💰 Análise Financeira

O projeto também trabalha com informações financeiras.

Principais campos:

Conta a pagar
Conta a receber
Valor original
Valor atual
Vencimento
Data de pagamento
Situação
Forma de pagamento

Possíveis indicadores:

Total a pagar
Total a receber
Valores vencidos
Valores pagos
Valores recebidos
Distribuição por situação
Distribuição por forma de pagamento
📦 Análise de Produtos

A estrutura de vendas permite relacionar:

Produto
   ↓
Categoria
   ↓
Item da Nota Fiscal
   ↓
Nota Fiscal
   ↓
Cliente
   ↓
Vendedor

Com isso podem ser analisados:

Produtos mais vendidos
Produtos com maior faturamento
Categorias com maior faturamento
Quantidade vendida
Valor de venda
Valor de custo
Margem
📈 Indicadores de Negócio

A camada analítica foi pensada para transformar os dados em indicadores de fácil interpretação.

Exemplo:

┌─────────────────────┐
│     FATURAMENTO     │
│     R$ XXXXX        │
└─────────────────────┘

┌─────────────────────┐
│    TICKET MÉDIO     │
│     R$ XXXXX        │
└─────────────────────┘

┌─────────────────────┐
│    Nº DE VENDAS     │
│       XXXXX         │
└─────────────────────┘

┌─────────────────────┐
│ MELHOR VENDEDOR     │
│      XXXXX          │
└─────────────────────┘
📊 Dashboard

A aplicação utiliza Streamlit para disponibilizar os resultados de forma interativa.

A estrutura do dashboard foi planejada para organizar as informações por domínio:

🏠 Visão Geral
│
├── 🛒 Vendas
│
├── 👥 Clientes
│
├── 📦 Produtos
│
├── 👨‍💼 Vendedores
│
└── 💰 Financeiro

Para visualização dos dados, o projeto utiliza gráficos interativos através do Plotly.

🤖 Inteligência Artificial Aplicada aos Dados

Uma das características do projeto é a utilização de IA como apoio à interpretação dos indicadores.

O processo funciona da seguinte maneira:

              BANCO
                │
                ▼
             EXTRAÇÃO
                │
                ▼
           TRANSFORMAÇÃO
                │
                ▼
               KPIs
                │
                ▼
        ┌───────────────┐
        │      IA       │
        └───────┬───────┘
                │
        ┌───────┴────────┐
        ▼                ▼
    INSIGHTS       RECOMENDAÇÕES

Exemplo conceitual:

Faturamento: R$ 100.000
Margem: 8%
Região: CE

        ↓

IA

        ↓

Análise dos indicadores

        ↓

Recomendação para tomada de decisão
🛠️ Tecnologias
Tecnologia	Utilização
🐍 Python	Desenvolvimento da aplicação
🐘 PostgreSQL	Banco de dados
🔗 SQLAlchemy	Conexão com banco
🧮 SQL	Consultas e JOINs
🐼 Pandas	Tratamento e análise
🔢 NumPy	Operações numéricas
📊 Plotly	Visualizações
🎨 Streamlit	Dashboard
🤖 API de IA	Insights e recomendações
🔐 python-dotenv	Variáveis de ambiente
🌿 Git	Controle de versão
🐙 GitHub	Versionamento e portfólio
🔐 Segurança

As credenciais do banco de dados e as chaves de API não devem ser armazenadas diretamente no código.

O projeto utiliza variáveis de ambiente.

Exemplo:

DB_HOST=seu_host
DB_PORT=5432
DB_NAME=seu_database
DB_USER=seu_usuario
DB_PASSWORD=sua_senha

GROQ_API_KEY=sua_chave

O arquivo:

.env

deve estar no .gitignore.

🚨 Nunca publique no GitHub:
❌ Senha do banco
❌ API Key
❌ Tokens
❌ Credenciais
❌ Informações privadas

Para facilitar a configuração de novos ambientes, recomenda-se utilizar:

.env.example

com valores fictícios.

⚙️ Instalação
1. Clonar o repositório
git clone https://github.com/SamuelFreitasSouza/digital-corporativo-data-analytics.git
2. Entrar na pasta
cd digital-corporativo-data-analytics
3. Criar ambiente virtual
python -m venv venv
4. Ativar ambiente virtual
Windows PowerShell
.\venv\Scripts\Activate.ps1
5. Instalar dependências
python -m pip install -r requirements.txt
🔌 Configuração do Banco

Crie um arquivo:

.env

e configure as variáveis necessárias para conexão com o PostgreSQL.

Exemplo:

DB_HOST=postgresql-host
DB_PORT=5432
DB_NAME=database
DB_USER=user
DB_PASSWORD=password

Não utilize credenciais reais diretamente neste README.

🧪 Testando a Conexão

Execute:

python src/database.py

Resultado esperado:

Conexão realizada com sucesso!

(1,)
🔎 Testando a Extração

Execute:

python src/extraction.py

O módulo realiza consultas de exploração e extração dos dados.

▶️ Executando o Dashboard

Com o ambiente virtual ativado:

python -m streamlit run app.py

O Streamlit iniciará a aplicação localmente.

📋 Requirements

As principais dependências do projeto incluem:

SQLAlchemy
psycopg2
pandas
numpy
plotly
streamlit
python-dotenv

As versões utilizadas no ambiente podem ser consultadas em:

requirements.txt
🧪 Validação do Pipeline

A execução pode ser validada seguindo esta ordem:

1. database.py
       ↓
2. extraction.py
       ↓
3. transformation.py
       ↓
4. analysis.py
       ↓
5. app.py

Cada etapa possui uma responsabilidade específica.

📚 Conceitos Aplicados

Este projeto permite demonstrar conhecimentos em diferentes etapas de um projeto de dados.

🗄️ Banco de Dados
PostgreSQL
Schemas
Tabelas
Relacionamentos
Chaves
SQL
JOINs
🐍 Python
Funções
Módulos
Imports
Ambiente virtual
Variáveis de ambiente
Tratamento de erros
Integração com APIs
🔄 ETL
Extract
   ↓
Transform
   ↓
Load / Analysis
📊 Data Analytics
Análise exploratória
KPIs
Métricas
Rankings
Segmentação
Análise temporal
Análise financeira
Análise comercial
📈 Business Intelligence
Indicadores
Dashboard
Storytelling
Visualização
Apoio à decisão
🧠 Principais Aprendizados

Durante o desenvolvimento foram trabalhados conceitos importantes de um projeto real de dados:

Banco de Dados
      ↓
Exploração
      ↓
SQL
      ↓
JOINs
      ↓
Extração
      ↓
Tratamento
      ↓
Pandas
      ↓
Análise
      ↓
KPIs
      ↓
Visualização
      ↓
Dashboard
      ↓
IA
      ↓
Insights

O projeto demonstra que uma solução de dados não consiste apenas em criar gráficos.

É necessário compreender:

DADO
 ↓
CONTEXTO
 ↓
TRATAMENTO
 ↓
ANÁLISE
 ↓
INFORMAÇÃO
 ↓
DECISÃO
🗺️ Roadmap
✅ Concluído
 Configuração do ambiente Python
 Criação do ambiente virtual
 Conexão com PostgreSQL
 Exploração dos schemas
 Identificação das tabelas
 Criação do dicionário de dados
 Testes de conexão
 Testes de extração
 Análise inicial de vendas
 Análise inicial de clientes
 Identificação de vendedores
 Estruturação dos módulos
 Estruturação do dashboard
 Integração inicial com IA
 Versionamento com Git
 Publicação no GitHub
🔄 Em evolução
 Refinamento dos JOINs
 Padronização dos datasets
 Tratamento completo dos dados
 Consolidação dos KPIs
 Refinamento do dashboard
 Melhorias de UX/UI
 Validação das recomendações da IA
🚀 Futuro
 Deploy do dashboard
 Automação do pipeline
 Atualização automática dos dados
 Testes automatizados
 Monitoramento
 Documentação de métricas
 Evolução da camada de IA
📖 Documentação

A documentação técnica detalhada do projeto está disponível na pasta:

docs/
└── documentação-projeto.pdf

A documentação apresenta informações sobre:

Arquitetura
Banco de dados
Extração
Transformação
Análise
Dashboard
Inteligência Artificial
Segurança
Execução
🎯 Objetivo Profissional

Este projeto faz parte da construção de um portfólio prático voltado para a área de:

📊 Data Analytics
📈 Business Intelligence
🐍 Python
🗄️ SQL
📊 Power BI
🧠 Inteligência Artificial

O foco é demonstrar não apenas conhecimento de ferramentas, mas a capacidade de construir um fluxo completo:

DADO
 ↓
EXTRAÇÃO
 ↓
TRATAMENTO
 ↓
ANÁLISE
 ↓
VISUALIZAÇÃO
 ↓
INSIGHT
 ↓
DECISÃO
👨‍💻 Autor
<div align="center">
Samuel Freitas Souza
Data Analyst | BI Specialist | SQL & Power BI

Transformando dados em informações para apoiar decisões de negócio.

<br> <a href="https://github.com/SamuelFreitasSouza"> <img src="https://img.shields.io/badge/GitHub-SamuelFreitasSouza-181717?style=for-the-badge&logo=github&logoColor=white"> </a> <a href="https://www.linkedin.com/in/samuel-freitas-944288180/"> <img src="https://img.shields.io/badge/LinkedIn-Samuel%20Freitas-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"> </a> </div>
<div align="center">
⭐ Gostou do projeto?

Considere deixar uma ⭐ no repositório.

<br>

Digital Corporativo — Data Analytics

Python • SQL • PostgreSQL • Pandas • Plotly • Streamlit • IA

</div> ```