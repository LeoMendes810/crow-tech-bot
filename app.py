import streamlit as st
import ccxt
import pandas as pd

st.set_page_config(page_title="Crow Tech Elite", layout="wide")

# Cabeçalho Crow Tech
st.title("🐦‍⬛ CROW TECH")
st.subheader("Inteligência em cada movimento")

# Simulação de Dashboard (Enquanto conectamos a API)
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Saldo Atual", "$ 185.50", "+$ 5.20")

with col2:
    st.metric("Meta do Dia", "$ 20.00", "25%")
    st.progress(0.25)

with col3:
    st.metric("Status do Bot", "Monitorando", "RSI")

st.info("O mercado está sendo monitorado em tempo real. Estratégia: RSI < 30 (Compra)")
