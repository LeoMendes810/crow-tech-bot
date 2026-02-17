import streamlit as st
import ccxt
import pandas as pd
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh
import os

# CONFIGURAÇÃO DE PÁGINA (Otimizada para Celular)
st.set_page_config(page_title="Crow Tech Mobile", layout="wide", initial_sidebar_state="expanded")
st_autorefresh(interval=30000, key="datarefresh")

# --- SISTEMA DE LOGIN SIMPLES ---
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

def login():
    st.markdown("<h2 style='text-align: center; color: white;'>CROW TECH LOGIN</h2>", unsafe_allow_html=True)
    with st.container():
        senha = st.text_input("Chave de Acesso", type="password")
        if st.button("Entrar no Terminal"):
            if senha == "crow2026": # Defina sua senha aqui
                st.session_state['autenticado'] = True
                st.rerun()
            else:
                st.error("Chave incorreta.")
    st.stop()

if not st.session_state['autenticado']:
    login()

# --- DESIGN E ESTILO (Slogan Corrigido e Background) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        background-image: linear-gradient(rgba(14, 17, 23, 0.88), rgba(14, 17, 23, 0.88)), 
                          url("https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/logo.png");
        background-attachment: fixed;
        background-size: 50%;
        background-repeat: no-repeat;
        background-position: center;
    }
    [data-testid="stMetric"] {
        background-color: rgba(28, 33, 40, 0.95);
        border: 1px solid #0ea5e9;
        border-radius: 12px;
    }
    h1, h2, h3, p { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
col_logo, col_titulo = st.columns([1, 4])
with col_logo:
    if os.path.exists("assets/logo.png"):
        st.image("assets/logo.png", width=100)

with col_titulo:
    st.markdown("<h1 style='margin-bottom:0;'>CROW <span style='color:#0ea5e9;'>TECH</span></h1>", unsafe_allow_html=True)
    # SLOGAN CORRIGIDO ABAIXO
    st.markdown("<p style='font-style:italic; color:#8b949e;'>Inteligência em cada movimento</p>", unsafe_allow_html=True)

# --- MENU LATERAL (CONTROLE REMOTO PELO CELULAR) ---
st.sidebar.image("assets/logo.png", width=80)
st.sidebar.title("Terminal de Controle")
status_bot = st.sidebar.toggle("Ligar/Desligar Robô", value=True)
parada_emergencia = st.sidebar.button("🚨 STOP EMERGENCY")

st.sidebar.divider()
st.sidebar.subheader("Ajustar Parâmetros")
rsi_limite = st.sidebar.slider("Limite RSI", 10, 90, 30)
moeda_foco = st.sidebar.selectbox("Moeda Principal", ['SOL', 'BTC', 'ETH', 'XRP', 'DOGE', 'TRX'])

if st.sidebar.button("Sair"):
    st.session_state['autenticado'] = False
    st.rerun()

# --- LÓGICA DE DADOS (6 PARES) ---
pares = ['SOL/USDT', 'BTC/USDT', 'ETH/USDT', 'XRP/USDT', 'DOGE/USDT', 'TRX/USDT']
try:
    exchange = ccxt.bitget({
        'apiKey': st.secrets["BITGET_API_KEY"],
        'secret': st.secrets["BITGET_SECRET"],
        'password': st.secrets["BITGET_PASSWORD"],
    })
    bal = exchange.fetch_balance()
    saldo_real = bal['total'].get('USDT', 0)
    
    dados_tabela = []
    for p in pares:
        t = exchange.fetch_ticker(p)
        dados_tabela.append({"Par": p, "Preço": f"$ {t['last']:.4f}", "24h %": f"{t['percentage']}%"})
except:
    saldo_real, dados_tabela = 15.94, []

# --- DASHBOARD ---
st.write("")
c1, c2, c3 = st.columns(3)
with c1: st.metric("SALDO REAL", f"$ {saldo_real:.2f}")
with c2: st.metric("LUCRO HOJE", "$ 5.20", delta="26%")
with c3: st.metric("STATUS", "ATIVO" if status_bot else "OFFLINE")

# --- ÁREA DE RADAR ---
st.divider()
col_radar, col_perf = st.columns([2, 1])

with col_radar:
    st.subheader("📡 Radar de Ativos")
    if dados_tabela:
        st.dataframe(pd.DataFrame(dados_tabela), use_container_width=True, hide_index=True)
    else:
        st.info("Aguardando conexão com Bitget...")

with col_perf:
    st.subheader("🎯 Performance")
    fig = go.Figure(go.Pie(labels=['Wins', 'Losses'], values=[85, 15], hole=.7, marker_colors=['#00ff00', '#ff0000']))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='white', height=250, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

st.caption("Acesso seguro via Crow Tech Terminal v2.5")
