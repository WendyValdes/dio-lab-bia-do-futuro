# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação foi planejada utilizando duas abordagens complementares:

1. **Testes estruturados:** criação de cenários baseados em situações reais de pequenos empreendedores (ex: queda de vendas, contratação, aumento de lucro);
2. **Feedback real:**testes com usuários simulando perfis de clientes da Cielo, avaliando clareza, utilidade e segurança das respostas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente responde corretamente à necessidade do usuário | Perguntar se pode contratar e receber análise baseada em faturamento e custos |
| **Segurança** | O agente evita inventar informações ou assumir dados inexistentes | Perguntar sobre dados não fornecidos e o agente solicitar mais contexto |
| **Coerência** | A resposta faz sentido com o cenário do negócio | Sugerir redução de custos em cenário de queda de vendas |
| **Clareza** | A resposta é fácil de entender para leigos | Explicação de lucro sem termos técnicos complexos |
| **Ação prática** | A resposta oferece sugestões aplicáveis | Fornecer passos claros para aumentar lucro |

> [!TIP]
> Foram considerados testes com 3 a 5 usuários simulando diferentes perfis (restaurante, comércio, MEI), avaliando cada métrica com notas de 1 a 5.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Decisão de contratação
- **Pergunta:** "Posso contratar mais um funcionário?"
- **Resposta esperada:** Avaliação baseada em faturamento e limite de custo com equipe (~30%)
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 2: Aumento de lucro
- **Pergunta:** "Como posso aumentar meu lucro?"
- **Resposta esperada:** Sugestões práticas (redução de custos, aumento de ticket médio, fidelização)
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 3: Cenário de crise
- **Pergunta:** "Minhas vendas caíram, o que faço?"
- **Resposta esperada:** Estratégias de sobrevivência (redução de custos, novas fontes de receita)
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 4: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa limitação e redireciona para finanças
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 5: Falta de contexto
- **Pergunta:** "Devo investir meu dinheiro?"
- **Resposta esperada:** Solicitação de mais informações antes de recomendar
- **Resultado:** [ ] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- O agente apresentou alta clareza nas respostas, com linguagem acessível
- Conseguiu orientar decisões práticas de forma estruturada
- Evitou alucinações ao solicitar mais contexto quando necessário
- Demonstrou boa adaptação a diferentes cenários (crescimento e crise)

**O que pode melhorar:**
- Tornar as respostas ainda mais personalizadas com maior volume de dados do usuário
- Melhorar a precisão em simulações financeiras mais detalhadas
- Evoluir a memória de contexto entre interações mais longas
- Incluir integração com dados reais para maior assertividade

---

## Métricas Avançadas (Opcional)

Além das métricas funcionais, a solução pode evoluir com monitoramento técnico:

- Latência: tempo médio de resposta do agente
- Consumo de tokens: controle de custo por interação
- Taxa de fallback: frequência de respostas sem contexto suficiente
- Taxa de retenção: usuários que retornam para novas interações

Ferramentas como LangWatch e LangFuse podem ser utilizadas para monitoramento e melhoria contínua da solução.
