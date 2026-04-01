# 🤖 Cielo AI Advisor

Agente financeiro inteligente desenvolvido com IA Generativa para apoiar pequenos e médios empreendedores na tomada de decisões com base em dados financeiros simulados da Cielo.

---

## 📌 Sobre o Projeto

Este projeto foi desenvolvido como parte de um desafio de IA aplicada, com o objetivo de criar um agente capaz de:

- Interpretar dados financeiros de clientes
- Responder perguntas de forma contextualizada
- Sugerir ações práticas para o negócio
- Evitar respostas imprecisas (alucinações)

O agente simula um **consultor financeiro digital**, utilizando dados estruturados e prompts bem definidos.

---

## 🎯 Problema

Empreendedores nem sempre possuem conhecimento ou ferramentas para analisar:

- Faturamento
- Custos
- Situação financeira do negócio

Isso dificulta decisões como:

- Contratar funcionários  
- Reduzir despesas  
- Expandir o negócio  

---

## 💡 Solução

O **Cielo AI Advisor** utiliza IA Generativa para:

- Analisar dados do cliente
- Entender o contexto do negócio
- Gerar recomendações claras e seguras

Tudo isso através de uma interface de chat simples.

---

## 🧠 O que o agente responde

Exemplos de perguntas:

- "Posso contratar mais um funcionário?"
- "Minhas vendas caíram, o que faço?"
- "Como melhorar meu lucro?"

O agente responde com base nos dados disponíveis e regras financeiras básicas.

---

## 📂 Estrutura do Repositório

📁 lab-agente-financeiro/
│
├── 📄 README.md
│
├── 📁 data_exemplo/ # Dados simulados do cliente
│ ├── boas_praticas_financeiras.json
│ ├── cenarios_negocio.json
│ ├── historico_interacoes.cvs
│ ├── indicadores_financeiros.json
│ ├── perfil_empresarial.json
│ ├── produtos_cielo.json
│ └── transacoes.csv
│
├── 📁 docs/ # Documentação do projeto
│ ├── 01-documentacao-agente.md
│ ├── 02-base-conhecimento.md
│ ├── 03-prompts.md
│ ├── 04-metricas.md
│ └── 05-pitch.md
│
├── 📁 src/ # Código da aplicação
│ ├── app.py
│ ├── agente.py
│ ├── config.py
│ └── requirements.txt
│
├── 📁 examples/ # Exemplos do projeto
└── README.md

⚙️ Como Executar
1. Instalar dependências
pip install -r src/requirements.txt
2. Configurar chave da API

Criar arquivo .env:

OPENAI_API_KEY=sua_chave_aqui
3. Rodar a aplicação
streamlit run src/app.py
📊 Base de Dados

Os dados são simulados e representam clientes da Cielo.

Incluem:

Informações do negócio
Histórico de transações
Custos
Cenário financeiro

Esses dados são utilizados como contexto para o agente.

🧩 Componentes do Projeto
Dados (data/): base de conhecimento do agente
Prompts (docs/03): definem comportamento e regras
Aplicação (src/): interface e lógica do chatbot
Métricas (docs/04): avaliação de qualidade
📏 Avaliação

O agente foi testado com base em:

Assertividade das respostas
Segurança (não inventar dados)
Coerência com o cenário do cliente
🚀 Possíveis Melhorias
Integração com dados reais
Interface mais robusta
Histórico de conversas
Recomendações mais avançadas
🎥 Pitch

O projeto inclui um pitch de até 3 minutos explicando:

Problema
Solução
Demonstração
Impacto

Ver em: docs/05-pitch.md

🏁 Conclusão

O projeto demonstra como a IA Generativa pode ser aplicada para transformar dados financeiros em recomendações úteis, de forma simples e acessível.

📌 Observação

Este projeto utiliza dados simulados e tem fins educacionais.

---

## 🔥 Agora sim — por que esse ficou melhor

Esse README:

✅ Reflete exatamente o que você fez (sem inventar arquitetura complexa)  
✅ É direto (avaliador lê rápido)  
✅ Mantém cara profissional  
✅ Conecta com todas as pastas do projeto  

---

Se quiser dar um **upgrade final (nível impressionar recrutador)**, posso:

👉 deixar ele mais visual (badges, prints, gif do app)  
👉 ou adaptar ele exatamente pro padrão da DIO  

Só falar 👍
