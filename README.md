<div align="center">

# 📊 Digital Corporativo
## Data Analytics & Business Intelligence

### Transformando dados corporativos em decisões estratégicas.

<br>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/python/)

<br>

**Python • SQL • PostgreSQL • ETL • Pandas • Data Visualization • Streamlit • IA**

</div>

---

# 📌 Sobre o projeto

O **Digital Corporativo — Data Analytics** é um projeto desenvolvido em Python com o objetivo de transformar dados corporativos armazenados em PostgreSQL em **informações analíticas, indicadores e insights para apoio à tomada de decisão**.

O projeto integra diferentes áreas do negócio:

| Área | Análises |
|---|---|
| 💰 **Financeiro** | Contas a pagar, contas a receber e situação dos títulos |
| 🛒 **Vendas** | Faturamento, evolução e desempenho comercial |
| 👥 **Clientes** | Perfil, segmentação e comportamento |
| 📦 **Produtos** | Vendas, custos, margem e categorias |
| 👨‍💼 **Vendedores** | Ranking e desempenho |
| 🧑‍💼 **RH** | Funcionários, cargos e departamentos |

---

# 🎯 Objetivo

O objetivo principal é demonstrar, na prática, um **pipeline completo de Data Analytics**, desde a conexão com o banco de dados até a apresentação dos resultados em um dashboard interativo.

### O projeto segue o seguinte fluxo:

```text
                    ┌─────────────────────┐
                    │     PostgreSQL      │
                    │                     │
                    │ Financeiro         │
                    │ Geral              │
                    │ Vendas             │
                    │ RH                 │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      EXTRAÇÃO       │
                    │       SQL           │
                    │       JOINs         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   TRANSFORMAÇÃO     │
                    │       Pandas        │
                    │                     │
                    │ Limpeza             │
                    │ Padronização         │
                    │ Tratamentos         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       ANÁLISE       │
                    │                     │
                    │ KPIs                │
                    │ Métricas             │
                    │ Rankings             │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
          ┌─────────────────┐   ┌─────────────────┐
          │    DASHBOARD    │   │       IA        │
          │    Streamlit    │   │    Insights     │
          │     Plotly      │   │ Recomendações   │
          └─────────────────┘   └─────────────────┘