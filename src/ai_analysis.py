import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


def gerar_recomendacoes(
    vendas_totais,
    inadimplencia,
    uf_maior_risco
):

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return """
### ⚠️ IA não configurada

A chave `GROQ_API_KEY` não foi encontrada no arquivo `.env`.

Configure a chave para habilitar a análise automática.
"""

    try:

        client = Groq(
            api_key=api_key
        )

        prompt = f"""
Você é um analista de dados e consultor financeiro.

Analise os seguintes indicadores:

Vendas totais:
R$ {vendas_totais:,.2f}

Taxa de inadimplência:
{inadimplencia:.2%}

UF com maior risco:
{uf_maior_risco}

Produza uma análise executiva contendo:

1. Diagnóstico do cenário.
2. Três ações práticas para reduzir a inadimplência.
3. Uma recomendação para a diretoria.

Regras:
- Não invente dados.
- Use somente os indicadores fornecidos.
- Seja objetivo.
- Escreva em português.
- Utilize linguagem profissional.
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as erro:

        return f"""
### ❌ Erro ao consultar a IA

{erro}
"""