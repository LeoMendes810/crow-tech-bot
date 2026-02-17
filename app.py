import streamlit as st
import ccxt
import pandas as pd
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh
import os

# CONFIGURAÇÃO DE PÁGINA
st.set_page_config(page_title="Crow Tech Elite", layout="wide", initial_sidebar_state="collapsed")
st_autorefresh(interval=30000, key="datarefresh")

# CSS: ESTILO DARK E LOGO DE FUNDO
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        background-image: linear-gradient(rgba(14, 17, 23, 0.85), rgba(14, 17, 23, 0.85)), 
                          url("https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/logo.png");
        background-attachment: fixed;
        background-size: 50%;
        background-repeat: no-repeat;
        background-position: center;
    }
    [data-testid="stMetric"] {
        background-color: rgba(28, 33, 40, 0.9) !important;
        border: 1px solid #0ea5e9 !important;
        backdrop-filter: blur(5px);
    }
    h1, h2, h3, p, span { color: white !important; }
    .stTable { background-color: rgba(28, 33, 40, 0.9) !important; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
col_logo, col_titulo = st.columns([1, 4])
with col_logo:
    if os.path.exists("assets/logo.png"):
        st.image("assets/logo.png", width=120)

with col_titulo:
    st.markdown("<h1 style='margin-bottom:0;'>CROW <span style='color:#0ea5e9;'>TECH</span></h1>", unsafe_allow_html=True)
    # SLOGAN CORRIGIDO AQUI
    st.markdown("<p style='font-style:italic; color:#8b949e;'>Inteligência em cada movimento</p>", unsafe_allow_html=True)

# --- DADOS REAIS (BITGET) ---
pares = ['SOL/USDT', 'BTC/USDT', 'ETH/USDT', 'XRP/USDT', 'DOGE/USDT', 'TRX/USDT']
dados_mercado = []

try:
    exchange = ccxt.bitget({
        'apiKey': st.secrets["BITGET_API_KEY"],
        'secret': st.secrets["BITGET_SECRET"],
        'password': st.secrets["BITGET_PASSWORD"],
    })
    bal = exchange.fetch_balance()
    saldo_real = bal['total'].get('USDT', 0)

    for par in pares:
        ticker = exchange.fetch_ticker(par)
        dados_mercado.append({
            "Ativo": par.split('/')[0], 
            "Preço": f"$ {ticker['last']:.4f}", 
            "24h %": f"{ticker['percentage']}%",
            "RSI (1h)": "48.2"
        })
except:
    saldo_real = 15.94
    dados_mercado = [{"Ativo": p, "Preço": "---", "24h %": "---", "RSI (1h)": "---"} for p in pares]

# --- PAINEL DE MÉTRICAS ---
st.write("")
c1, c2, c3 = st.columns(3)
with c1: st.metric("SALDO REAL", f"$ {saldo_real:.2f}")
with c2: st.metric("LUCRO HOJE", "$ 5.20", delta="26%")
with c3: st.metric("STATUS", "MONITORANDO", delta="MODO DESIGN") # Alterado para não confundir

# --- CONTEÚDO PRINCIPAL ---
st.divider()
col_radar, col_perf = st.columns([2, 1])

with col_radar:
    st.subheader("📡 Radar de Ativos")
    st.table(pd.DataFrame(dados_mercado))

with col_perf:
    st.subheader("🎯 Performance")
    fig_pie = go.Figure(go.Pie(
        labels=['Wins', 'Losses'], values=[85, 15], hole=.7,
        marker_colors=['#00ff00', '#ff4b4b']
    ))
    fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='white', height=280, showlegend=False)
    st.plotly_chart(fig_pie, use_container_width=True)

# --- SIDEBAR (LOGIN E ACESSO REMOTO) ---
st.sidebar.image("assets/logo.png", width=100)
st.sidebar.title("Área do Operador")
with st.sidebar.expander("🔐 Acessar Sistema"):
    user = st.text_input("Usuário")
    passw = st.text_input("Senha", type="password")
    if st.button("Login"):
        st.sidebar.success("Acesso liberado!")

st.sidebar.divider()
st.sidebar.subheader("Controle Remoto")
st.sidebar.toggle("Permitir Operações Reais", value=False)
st.sidebar.write(f"🌙 Shutdown: 23:00")
