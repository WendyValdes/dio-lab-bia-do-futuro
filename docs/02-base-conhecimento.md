# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `perfil_empresarial.json` | JSON | Armazena dados do negócio (faturamento, segmento, custos) para personalizar recomendações |
| `indicadores_financieiros.json` | JSON | Contém regras de cálculo (lucro, margem, ponto de equilíbrio) |
| `boas_praticas_financeiras.json` | JSON | Base de conhecimento com orientações sobre gestão financeira |
| `produtos_cielo.json` | JSON | Informações sobre soluções da Cielo (maquininha, taxas, antecipação) |
| `cenarios_crise.json` | JSON | Estratégias para momentos de queda de receita ou crises econômicas |

> [!TIP]
> Também podem ser incorporados datasets públicos de comportamento financeiro para enriquecer recomendações e simulações.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados foram adaptados para simular o contexto real de pequenos empreendedores, com foco em negócios como restaurantes, comércios locais e prestadores de serviço.

As principais adaptações incluem:

- Criação de perfis empresariais simplificados (ex: faturamento mensal, custos fixos, número de funcionários)
- Inclusão de regras práticas de negócio (ex: limite saudável de custo com funcionários)
- Estruturação de exemplos de cenários reais (queda de vendas, expansão, contratação)
- Simplificação de conceitos financeiros para facilitar interpretação pelo modelo

Além disso, os dados foram organizados de forma a facilitar o uso por IA generativa, priorizando clareza, contexto e aplicabilidade.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos JSON e CSV são carregados no início da execução da aplicação (por exemplo, via Python em ambiente como Streamlit). Esses dados são estruturados em objetos que podem ser facilmente consultados durante a interação.

Parte das informações mais relevantes é inserida diretamente no contexto do prompt, enquanto outras são acessadas dinamicamente conforme a necessidade da pergunta do usuário.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

A estratégia combina duas abordagens:

- System Prompt (contexto fixo):
  - Regras gerais de negócio
  - Boas práticas financeiras
  - Diretrizes de comportamento do agente
- Contexto dinâmico:
  - Dados do usuário (faturamento, custos, segmento)
  - Histórico de interações
  - Cenário atual (ex: queda de vendas, expansão)

Quando o usuário faz uma pergunta, o agente monta dinamicamente um contexto relevante, incluindo apenas as informações necessárias para gerar uma resposta mais precisa e personalizada.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome do negócio: Restaurante Sabor Caseiro
- Segmento: Alimentação
- Faturamento mensal: R$ 30.000
- Custos fixos: R$ 18.000
- Número de funcionários: 3

Situação atual:
- Queda de 20% nas vendas no último mês
- Interesse em contratar mais um funcionário

Regras relevantes:
- Margem de lucro ideal: acima de 15%
- Custo com funcionários recomendado: até 30% do faturamento

Histórico recente:
- Perguntou sobre redução de custos
- Demonstrou interesse em aumentar lucro

Objetivo do usuário:
- Entender se pode contratar sem comprometer o lucro
```
