import streamlit as st
from agente import gerar_resposta, carregar_dados

st.set_page_config(page_title="Cielo AI Advisor", layout="centered")

st.title("🤖 Cielo AI Advisor")
st.markdown("Seu assistente financeiro inteligente")

# Carregar dados
dados = carregar_dados()

# Histórico de conversa
if "historico" not in st.session_state:
    st.session_state.historico = []

# Input do usuário
pergunta = st.text_input("Digite sua pergunta:")

if st.button("Enviar") and pergunta:
    resposta = gerar_resposta(pergunta, dados)
    
    st.session_state.historico.append(("Você", pergunta))
    st.session_state.historico.append(("Agente", resposta))

# Exibir histórico
for autor, msg in st.session_state.historico:
    if autor == "Você":
        st.markdown(f"**🧑 {autor}:** {msg}")
    else:
        st.markdown(f"**🤖 {autor}:** {msg}")
