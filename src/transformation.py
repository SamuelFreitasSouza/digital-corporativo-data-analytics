import pandas as pd

from .extraction import extrair_dados


def tratar_dados(df):
    df = df.copy()

    # -------------------------
    # TIPOS
    # -------------------------

    df["data_venda"] = pd.to_datetime(
        df["data_venda"],
        errors="coerce"
    )

    colunas_numericas = [
        "valor_nota",
        "quantidade",
        "valor_unitario",
        "valor_venda_real",
        "preco_cadastro",
        "valor_custo",
        "valor_inadimplente"
    ]

    for coluna in colunas_numericas:
        df[coluna] = pd.to_numeric(
            df[coluna],
            errors="coerce"
        )

    # -------------------------
    # TRATAMENTO DE NULOS
    # -------------------------

    colunas_texto = [
        "cliente",
        "tipo_pessoa",
        "uf",
        "vendedor",
        "forma_pagamento",
        "produto",
        "categoria"
    ]

    for coluna in colunas_texto:
        df[coluna] = df[coluna].fillna("Não informado")

    df["quantidade"] = df["quantidade"].fillna(0)
    df["valor_venda_real"] = df["valor_venda_real"].fillna(0)
    df["valor_custo"] = df["valor_custo"].fillna(0)
    df["valor_inadimplente"] = df["valor_inadimplente"].fillna(0)

    # -------------------------
    # REMOVER REGISTROS
    # -------------------------

    df = df.dropna(
        subset=["data_venda"]
    )

    # -------------------------
    # FEATURE ENGINEERING
    # -------------------------

    # Receita do item
    df["receita_item"] = (
        df["quantidade"] *
        df["valor_venda_real"]
    )

    # Custo do item
    df["custo_item"] = (
        df["quantidade"] *
        df["valor_custo"]
    )

    # Lucro
    df["lucro"] = (
        df["receita_item"] -
        df["custo_item"]
    )

    # Margem
    df["margem"] = 0.0

    mask = df["receita_item"] > 0

    df.loc[mask, "margem"] = (
        df.loc[mask, "lucro"] /
        df.loc[mask, "receita_item"]
    )

    # Comissão de 2,5%
    df["comissao"] = (
        df["receita_item"] * 0.025
    )

    # Indicador de inadimplência
    df["inadimplente"] = (
        df["possui_inadimplencia"]
        .fillna(0)
        .astype(int)
    )

    # -------------------------
    # DATAS
    # -------------------------

    df["ano"] = df["data_venda"].dt.year

    df["mes"] = df["data_venda"].dt.month

    df["mes_nome"] = (
        df["data_venda"]
        .dt.strftime("%b")
    )

    df["ano_mes"] = (
        df["data_venda"]
        .dt.to_period("M")
        .astype(str)
    )

    # -------------------------
    # LIMPEZA
    # -------------------------

    df = df.drop_duplicates()

    return df


def gerar_dataset():
    df = extrair_dados()

    print("\nTratando dados...")

    df = tratar_dados(df)

    print("Tratamento concluído.")
    print(f"Registros finais: {len(df):,}")

    return df


if __name__ == "__main__":
    df = gerar_dataset()

    print("\n=== DATASET TRATADO ===")
    print(df.head())

    print("\n=== NULOS ===")
    print(
        df.isnull()
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )