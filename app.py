import streamlit as st
import plotly.express as px

from src.ai_analysis import gerar_recomendacoes
from src.transformation import gerar_dataset

from src.analysis import (
    resumo_geral,
    vendas_mensais,
    vendas_categoria,
    top_vendedores,
    produtos_rentaveis,
    inadimplencia_uf
)

st.set_page_config(
    page_title="TechVendas Analytics",
    page_icon="📊",
    layout="wide"
)


@st.cache_data
def carregar_dados():
    return gerar_dataset()


df = carregar_dados()


# =========================================
# TÍTULO
# =========================================

st.title("📊 TechVendas Analytics")

st.markdown(
    """
    ### Inteligência de Negócios

    Dashboard para análise de vendas, produtos,
    vendedores e risco financeiro.
    """
)


# =========================================
# SIDEBAR
# =========================================

st.sidebar.header("🔎 Filtros")


anos = sorted(
    df["ano"].dropna().unique()
)

ano_selecionado = st.sidebar.multiselect(
    "Ano",
    options=anos,
    default=anos
)


categorias = sorted(
    df["categoria"]
    .dropna()
    .unique()
)

categoria_selecionada = st.sidebar.multiselect(
    "Categoria",
    options=categorias,
    default=categorias
)


vendedores = sorted(
    df["vendedor"]
    .dropna()
    .unique()
)

vendedor_selecionado = st.sidebar.multiselect(
    "Vendedor",
    options=vendedores,
    default=vendedores
)


# =========================================
# FILTROS
# =========================================

df_filtrado = df[
    df["ano"].isin(ano_selecionado)
    &
    df["categoria"].isin(categoria_selecionada)
    &
    df["vendedor"].isin(vendedor_selecionado)
].copy()


# =========================================
# KPIs
# =========================================

resumo = resumo_geral(df_filtrado)


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "💰 Total Vendido",
        f"R$ {resumo['total_vendido']:,.2f}"
    )


with col2:
    st.metric(
        "🎟️ Ticket Médio",
        f"R$ {resumo['ticket_medio']:,.2f}"
    )


with col3:
    st.metric(
        "⚠️ Total Inadimplente",
        f"R$ {resumo['total_inadimplente']:,.2f}"
    )


with col4:
    st.metric(
        "🧾 Notas",
        f"{resumo['quantidade_notas']:,}"
    )


st.divider()


# =========================================
# EVOLUÇÃO MENSAL
# =========================================

st.subheader("📈 Evolução das Vendas")

df_mensal = vendas_mensais(df_filtrado)

fig_mensal = px.line(
    df_mensal,
    x="ano_mes",
    y="vendas",
    markers=True,
    title="Evolução mensal das vendas"
)

fig_mensal.update_layout(
    xaxis_title="Período",
    yaxis_title="Vendas"
)

st.plotly_chart(
    fig_mensal,
    use_container_width=True
)


# =========================================
# CATEGORIAS
# =========================================

col1, col2 = st.columns(2)


with col1:

    st.subheader("📦 Vendas por Categoria")

    df_cat = vendas_categoria(
        df_filtrado
    )

    fig_cat = px.bar(
        df_cat,
        x="categoria",
        y="vendas",
        text_auto=".2s",
        title="Vendas por categoria"
    )

    st.plotly_chart(
        fig_cat,
        use_container_width=True
    )


with col2:

    st.subheader("💹 Margem por Categoria")

    fig_margem = px.bar(
        df_cat,
        x="categoria",
        y="margem",
        text_auto=".2%",
        title="Margem de lucro"
    )

    st.plotly_chart(
        fig_margem,
        use_container_width=True
    )


# =========================================
# VENDEDORES
# =========================================

st.subheader("🏆 Top 5 Vendedores")

df_vendedores = top_vendedores(
    df_filtrado
)

st.dataframe(
    df_vendedores,
    use_container_width=True,
    hide_index=True
)


# =========================================
# PRODUTOS
# =========================================

st.subheader("⭐ Produtos Mais Rentáveis")

df_produtos = produtos_rentaveis(
    df_filtrado
)

st.dataframe(
    df_produtos.head(10),
    use_container_width=True,
    hide_index=True
)


# =========================================
# INADIMPLÊNCIA
# =========================================

st.subheader("⚠️ Inadimplência por Estado")

df_uf = inadimplencia_uf(
    df_filtrado
)

fig_uf = px.bar(
    df_uf,
    x="uf",
    y="taxa_inadimplencia",
    text_auto=".2%",
    title="Taxa de inadimplência por UF"
)

st.plotly_chart(
    fig_uf,
    use_container_width=True
)


# =========================================
# TABELA DE INADIMPLÊNCIA
# =========================================

st.dataframe(
    df_uf,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.subheader("🤖 Análise Inteligente")

if not df_uf.empty:

    maior_risco = df_uf.iloc[0]

    taxa_inadimplencia = (
        df_filtrado["valor_inadimplente"].sum()
        /
        df_filtrado["receita_item"].sum()
        if df_filtrado["receita_item"].sum() > 0
        else 0
    )

    if st.button("🤖 Gerar recomendações com IA"):

        with st.spinner("Analisando os indicadores..."):

            recomendacao = gerar_recomendacoes(
                vendas_totais=resumo["total_vendido"],
                inadimplencia=taxa_inadimplencia,
                uf_maior_risco=maior_risco["uf"]
            )

        st.markdown(recomendacao)