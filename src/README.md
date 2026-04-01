# Código da Aplicação

# Código da Aplicação

Esta pasta contém a implementação do **Cielo AI Advisor**, um agente financeiro inteligente que auxilia pequenos e médios empreendedores na tomada de decisões.

A aplicação utiliza IA generativa combinada com dados estruturados da pasta `data/` para fornecer respostas personalizadas, seguras e acionáveis.

---

## 🏗️ Estrutura do Projeto


## Estrutura Sugerida

```
src/
├── app.py # Interface do chatbot (Streamlit)
├── agente.py # Lógica do agente (prompt + integração com IA)
├── config.py # Configurações (API Key, parâmetros)
└── requirements.txt # Dependências do projeto
```


---

## ⚙️ Tecnologias Utilizadas

- Python
- Streamlit (interface interativa)
- OpenAI API (LLM)
- JSON/CSV (base de conhecimento)

---

## 🧠 Funcionamento do Agente

O fluxo da aplicação é:

1. O usuário envia uma pergunta pelo chat  
2. O sistema carrega dados do cliente (pasta `data/`)  
3. O agente monta um contexto com:
   - Perfil empresarial  
   - Regras financeiras  
   - Cenário do negócio  
4. O prompt é enviado para o modelo de IA  
5. O agente retorna uma resposta clara e personalizada  

---

## 📦 Instalação

### 1. Criar ambiente virtual (opcional)

```bash
python -m venv venv

```
- Ativar Windows:
  
```bash
venv\Scripts\activate

```
- Instalar dependências:

```bash
pip install -r requirements.txt

```
- Configuração da API

``` OPENAI_API_KEY=sua_chave_aqui```

- Como Rodar

```bash
streamlit run app.py

```
- Depois disso, abra no navegador: ``` http://localhost:8501```

💬 Exemplos de Uso

Você pode testar perguntas como:

"Posso contratar mais um funcionário?"
"Como aumentar meu lucro?"
"Minhas vendas caíram, o que faço?"

🚀 Possíveis Evoluções
- Integração com dados reais da Cielo
- Dashboard financeiro interativo
- Memória de longo prazo do usuário
- Recomendações mais avançadas com base em histórico

🎯 Objetivo
Demonstrar na prática como criar um agente inteligente que combina:
- IA generativa
- Dados estruturados
- Experiência do usuário

Para apoiar decisões financeiras no dia a dia de empreendedores.


