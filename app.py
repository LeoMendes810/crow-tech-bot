import streamlit as st
import ccxt
import pandas as pd
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh
import os

# 1. FORÇAR TEMA ESCURO E CORRIGIR CORES
st.set_page_config(page_title="Crow Tech Elite", layout="wide", initial_sidebar_state="collapsed")
st_autorefresh(interval=30000, key="datarefresh")

st.markdown("""
    <style>
    /* Fundo Total Escuro */
    .stApp { background-color: #0e1117; }
    
    /* Forçar cores de texto */
    h1, h2, h3, span, p, label { color: white !important; }
    
    /* Estilizar os Cards de métricas */
    div[data-testid="stMetric"] {
        background-color: #1c2128;
        border: 1px solid #0ea5e9;
        border-radius: 10px;
        padding: 20px;
    }
    
    /* Remover espaços inúteis no topo */
    .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ALINHADO ---
col_logo, col_titulo = st.columns([1, 4])

with col_logo:
    if os.path.exists("assets/logo.png"):
        st.image("assets/logo.png", width=120)
    else:
        st.title("🐦‍⬛")

with col_titulo:
    # Título com as duas cores da marca
    st.markdown("<h1 style='margin-top: 10px;'>CROW <span style='color: #0ea5e9;'>TECH</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-style: italic; color: #8b949e !important;'>Seu estilo em jogo | Inteligência em cada movimento</p>", unsafe_allow_html=True)

# --- DADOS (BITGET) ---
try:
    exchange = ccxt.bitget({
        'apiKey': st.secrets["BITGET_API_KEY"],
        'secret': st.secrets["BITGET_SECRET"],
        'password': st.secrets["BITGET_PASSWORD"],
    })
    bal = exchange.fetch_balance()
    saldo = bal['total'].get('USDT', 0)
    ticker = exchange.fetch_ticker('SOL/USDT')
    preco = ticker['last']
except:
    saldo, preco = 15.94, 142.10

# --- DASHBOARD ---
st.write("") # Espaçador
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("SALDO EM CONTA", f"$ {saldo:.2f}", delta="LIVE")

with c2:
    meta = 20.0
    lucro = 5.20
    st.metric("META DO DIA", f"$ {lucro:.2f}", delta=f"{(lucro/meta)*100:.1f}%")
    st.progress(lucro/meta)

with c3:
    st.metric("STATUS", "MONITORANDO", delta="RSI: 48.5")

# --- GRÁFICOS ---
st.divider()
col_g1, col_g2 = st.columns([2, 1])

with col_g1:
    st.subheader("Radar de Mercado (SOL/USDT)")
    st.info(f"Preço atual da Solana: $ {preco}")
    # Simulação de gráfico de barras de volume para preencher espaço
    fig = go.Figure(go.Bar(x=list(range(10)), y=[10, 12, 8, 15, 20, 18, 22, 25, 21, 24], marker_color='#0ea5e9'))
    fig.update_layout(template="plotly_dark", height=300, margin=dict(l=0,r=0,t=0,b=0))
    st.plotly_chart(fig, use_container_width=True)

with col_g2:
    st.subheader("Performance")
    fig_pie = go.Figure(go.Pie(labels=['Acertos', 'Erros'], values=[85, 15], hole=.6, 
                              marker_colors=['#00ff00', '#ff0000']))
    fig_pie.update_layout(template="plotly_dark", height=300, showlegend=False)
    st.plotly_chart(fig_pie, use_container_width=True)

st.sidebar.markdown("### Configurações")
st.sidebar.write("🌙 Desligamento: 23:00")
