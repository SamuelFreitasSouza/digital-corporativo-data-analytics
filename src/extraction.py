import pandas as pd
from sqlalchemy import text

from .database import engine

def extrair_dados():
    query = """
    WITH clientes AS (
        SELECT
            p.id AS id_cliente,
            COALESCE(
                pf.nome,
                pj.razao_social,
                'Cliente não identificado'
            ) AS cliente,
            CASE
                WHEN pf.id IS NOT NULL THEN 'Pessoa Física'
                WHEN pj.id IS NOT NULL THEN 'Pessoa Jurídica'
                ELSE 'Não identificado'
            END AS tipo_pessoa
        FROM geral.pessoa p
        LEFT JOIN geral.pessoa_fisica pf
            ON p.id = pf.id
        LEFT JOIN geral.pessoa_juridica pj
            ON p.id = pj.id
    ),

    endereco_cliente AS (
        SELECT DISTINCT ON (e.id_pessoa)
            e.id_pessoa,
            est.sigla AS uf
        FROM geral.endereco e
        LEFT JOIN geral.bairro b
            ON e.id_bairro = b.id
        LEFT JOIN geral.cidade c
            ON b.id_cidade = c.id
        LEFT JOIN geral.estado est
            ON c.id_estado = est.id
        ORDER BY e.id_pessoa, e.id
    ),

    vendedores AS (
        SELECT
            p.id AS id_vendedor,
            COALESCE(
                pf.nome,
                pj.razao_social,
                'Vendedor não identificado'
            ) AS vendedor
        FROM geral.pessoa p
        LEFT JOIN geral.pessoa_fisica pf
            ON p.id = pf.id
        LEFT JOIN geral.pessoa_juridica pj
            ON p.id = pj.id
    ),

    financeiro AS (
        SELECT
            pa.id_nota_fiscal,

            SUM(
                CASE
                    WHEN st.descricao ILIKE '%inadimpl%'
                      OR st.descricao ILIKE '%venc%'
                    THEN cr.valor_atual
                    ELSE 0
                END
            ) AS valor_inadimplente,

            MAX(
                CASE
                    WHEN st.descricao ILIKE '%inadimpl%'
                      OR st.descricao ILIKE '%venc%'
                    THEN 1
                    ELSE 0
                END
            ) AS possui_inadimplencia

        FROM vendas.parcela pa

        LEFT JOIN financeiro.conta_receber cr
            ON cr.id_parcela = pa.id

        LEFT JOIN financeiro.situacao_titulo st
            ON cr.id_situacao = st.id

        GROUP BY pa.id_nota_fiscal
    )

    SELECT
        nf.id AS id_nota,
        nf.numero_nf,
        nf.data_venda,
        nf.valor AS valor_nota,

        nf.id_cliente,
        c.cliente,
        c.tipo_pessoa,
        ec.uf,

        nf.id_vendedor,
        COALESCE(v.vendedor, 'Vendedor não identificado') AS vendedor,

        nf.id_forma_pagto,
        fp.descricao AS forma_pagamento,

        inf.id AS id_item,
        inf.id_produto,
        inf.quantidade,
        inf.valor_unitario,
        inf.valor_venda_real,

        pr.nome AS produto,
        pr.valor_venda AS preco_cadastro,
        pr.valor_custo,

        cat.id AS id_categoria,
        cat.descricao AS categoria,

        COALESCE(fin.valor_inadimplente, 0) AS valor_inadimplente,

        COALESCE(fin.possui_inadimplencia, 0) AS possui_inadimplencia

    FROM vendas.nota_fiscal nf

    LEFT JOIN clientes c
        ON nf.id_cliente = c.id_cliente

    LEFT JOIN endereco_cliente ec
        ON nf.id_cliente = ec.id_pessoa

    LEFT JOIN vendedores v
        ON nf.id_vendedor = v.id_vendedor

    LEFT JOIN vendas.forma_pagamento fp
        ON nf.id_forma_pagto = fp.id

    LEFT JOIN vendas.item_nota_fiscal inf
        ON nf.id = inf.id_nota_fiscal

    LEFT JOIN vendas.produto pr
        ON inf.id_produto = pr.id

    LEFT JOIN vendas.categoria cat
        ON pr.id_categoria = cat.id

    LEFT JOIN financeiro fin
        ON nf.id = fin.id_nota_fiscal

    ORDER BY nf.data_venda, nf.id;
    """

    print("Extraindo dados do PostgreSQL...")

    with engine.connect() as connection:
        df = pd.read_sql(text(query), connection)

    print(f"Extração concluída: {len(df):,} registros.")

    return df


if __name__ == "__main__":
    df = extrair_dados()

    print("\n=== AMOSTRA ===")
    print(df.head())

    print("\n=== COLUNAS ===")
    print(df.columns.tolist())

    print("\n=== DIMENSÃO ===")
    print(df.shape)