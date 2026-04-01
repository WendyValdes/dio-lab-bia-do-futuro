# 🤖 Cielo AI Advisor

Agente financeiro inteligente desenvolvido com IA Generativa para apoiar pequenos e médios empreendedores na tomada de decisões com base em dados simulados.

---

## 📌 Sobre o Projeto

O **Cielo AI Advisor** é um chatbot que atua como um consultor financeiro digital, utilizando:

- Dados estruturados (clientes, transações, custos e cenários)
- IA Generativa (OpenAI)
- Interface interativa com Streamlit

O objetivo é transformar dados financeiros em **respostas claras, seguras e acionáveis**.

---

## 🎯 Problema

Empreendedores têm dificuldade em analisar seus dados financeiros e tomar decisões como:

- Contratar funcionários  
- Reduzir custos  
- Reagir a quedas de vendas  
- Aumentar lucro  

---

## 💡 Solução

O agente:

- Interpreta dados do cliente  
- Entende o contexto do negócio  
- Responde perguntas em linguagem natural  
- Sugere ações práticas  

Tudo via chat.

---

## 💬 Exemplos de uso

- "Posso contratar mais um funcionário?"
- "Minhas vendas caíram, o que faço?"
- "Como posso aumentar meu lucro?"

---

## 📂 Estrutura do Projeto


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
├── .env
└── README.md 

⚙️ Como Executar

1. Instalar dependências
pip install -r src/requirements.txt

2. Criar arquivo .env

Na raiz do projeto, crie um arquivo chamado:

.env

E adicione sua chave da OpenAI:

OPENAI_API_KEY=sua_chave_aqui

3. Rodar a aplicação
streamlit run src/app.py

Abra no navegador:

http://localhost:8501

🧠 Funcionamento do Agente

O fluxo é:

1- Usuário envia uma pergunta
2- O sistema carrega dados da pasta data/
3- O agente monta um contexto com esses dados
4- A pergunta é enviada para o modelo de IA
5- A resposta é gerada com base no contexto

📊 Base de Dados: data_exemplo
Os dados são simulados e representam clientes reais:
Esses dados alimentam o contexto do agente.

📏 Avaliação
O agente foi avaliado com base em:
- Assertividade
- Segurança (não inventar informações)
- Coerência com os dados

🚀 Possíveis Melhorias
- Seleção de cliente no app
- Cálculo automático de métricas (lucro, margem)
- Interface mais avançada
- Integração com dados reais

⚠️ Observações Importantes
- O arquivo .env não deve ser enviado para o GitHub
- Este projeto utiliza dados simulados
- Uso educacional

🏁 Conclusão

O projeto demonstra como a IA Generativa pode ser aplicada para apoiar decisões financeiras de forma simples, prática e contextualizada.
