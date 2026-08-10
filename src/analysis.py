import pandas as pd

from .transformation import gerar_dataset


def resumo_geral(df):
    total_vendido = df["receita_item"].sum()

    quantidade_notas = df["id_nota"].nunique()

    ticket_medio = (
        total_vendido / quantidade_notas
        if quantidade_notas > 0
        else 0
    )

    total_inadimplente = df[
        "valor_inadimplente"
    ].sum()

    return {
        "total_vendido": total_vendido,
        "ticket_medio": ticket_medio,
        "total_inadimplente": total_inadimplente,
        "quantidade_notas": quantidade_notas
    }


def vendas_mensais(df):
    resultado = (
        df.groupby("ano_mes", as_index=False)
        .agg(
            vendas=("receita_item", "sum"),
            notas=("id_nota", "nunique")
        )
        .sort_values("ano_mes")
    )

    return resultado


def vendas_categoria(df):
    resultado = (
        df.groupby("categoria", as_index=False)
        .agg(
            vendas=("receita_item", "sum"),
            lucro=("lucro", "sum"),
            quantidade=("quantidade", "sum")
        )
        .sort_values(
            "vendas",
            ascending=False
        )
    )

    resultado["margem"] = (
        resultado["lucro"] /
        resultado["vendas"]
    ).fillna(0)

    return resultado


def top_vendedores(df):
    resultado = (
        df.groupby("vendedor", as_index=False)
        .agg(
            vendas=("receita_item", "sum"),
            lucro=("lucro", "sum"),
            quantidade_notas=("id_nota", "nunique")
        )
        .sort_values(
            "vendas",
            ascending=False
        )
        .head(5)
    )

    resultado["comissao"] = (
        resultado["vendas"] * 0.025
    )

    return resultado


def produtos_rentaveis(df):
    resultado = (
        df.groupby(
            ["produto", "categoria"],
            as_index=False
        )
        .agg(
            vendas=("receita_item", "sum"),
            custo=("custo_item", "sum"),
            lucro=("lucro", "sum"),
            quantidade=("quantidade", "sum")
        )
    )

    resultado["margem"] = (
        resultado["lucro"] /
        resultado["vendas"]
    ).fillna(0)

    return resultado.sort_values(
        "lucro",
        ascending=False
    )


def inadimplencia_uf(df):
    resultado = (
        df.groupby("uf", as_index=False)
        .agg(
            valor_vendido=("receita_item", "sum"),
            valor_inadimplente=(
                "valor_inadimplente",
                "sum"
            )
        )
    )

    resultado["taxa_inadimplencia"] = 0.0

    mask = resultado["valor_vendido"] > 0

    resultado.loc[
        mask,
        "taxa_inadimplencia"
    ] = (
        resultado.loc[
            mask,
            "valor_inadimplente"
        ]
        /
        resultado.loc[
            mask,
            "valor_vendido"
        ]
    )

    return resultado.sort_values(
        "taxa_inadimplencia",
        ascending=False
    )


def analise_extra(df):
    """
    Análise adicional solicitada pelo trabalho.
    Vamos identificar os produtos com maior
    contribuição absoluta de lucro.
    """

    resultado = (
        df.groupby("produto", as_index=False)
        .agg(
            lucro=("lucro", "sum"),
            vendas=("receita_item", "sum")
        )
        .sort_values(
            "lucro",
            ascending=False
        )
        .head(10)
    )

    return resultado


if __name__ == "__main__":

    df = gerar_dataset()

    print("\n=== RESUMO ===")
    print(resumo_geral(df))

    print("\n=== TOP 5 VENDEDORES ===")
    print(top_vendedores(df))

    print("\n=== CATEGORIAS ===")
    print(vendas_categoria(df).head())

    print("\n=== INADIMPLÊNCIA POR UF ===")
    print(inadimplencia_uf(df))

    print("\n=== PRODUTOS MAIS RENTÁVEIS ===")
    print(produtos_rentaveis(df).head(10))