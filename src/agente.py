import json
import pandas as pd
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def carregar_dados():
    clientes = pd.read_csv("../data/clientes.csv")
    transacoes = pd.read_csv("../data/transacoes.csv")
    custos = pd.read_csv("../data/custos.csv")

    with open("../data/cenarios.json", "r", encoding="utf-8") as f:
        cenarios = json.load(f)

    return {
        "clientes": clientes,
        "transacoes": transacoes,
        "custos": custos,
        "cenarios": cenarios
    }

def montar_contexto(dados):
    return f"""
Você é um consultor financeiro especializado em pequenos negócios.

DADOS DO CLIENTE:
Clientes:
{dados['clientes'].head().to_string()}

Transações:
{dados['transacoes'].head().to_string()}

Custos:
{dados['custos'].head().to_string()}

Cenários:
{dados['cenarios']}

REGRAS:
- Nunca invente valores
- Use apenas os dados fornecidos
- Seja direto e prático
- Dê recomendações seguras
"""

def gerar_resposta(pergunta, dados):
    contexto = montar_contexto(dados)

    resposta = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": contexto},
            {"role": "user", "content": pergunta}
        ],
        temperature=0.3
    )

    return resposta.choices[0].message.content
