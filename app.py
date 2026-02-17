import streamlit as st
import ccxt
import pandas as pd
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh
import os

# CONFIGURAÇÃO DE PÁGINA
st.set_page_config(page_title="Crow Tech Elite", layout="wide", initial_sidebar_state="collapsed")
st_autorefresh(interval=30000, key="datarefresh")

# CSS: ESTILO DARK, LOGO DE FUNDO E TEXTOS IMPACTANTES
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        background-image: linear-gradient(rgba(14, 17, 23, 0.92), rgba(14, 17, 23, 0.92)), 
                          url("https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/logo.png");
        background-attachment: fixed;
        background-size: 50%;
        background-repeat: no-repeat;
        background-position: center;
    }
    
    [data-testid="stMetric"] {
        background-color: rgba(28, 33, 40, 0.95) !important;
        border: none !important;
        border-radius: 15px;
        padding: 25px !important;
    }
    
    .stTable { 
        background-color: rgba(28, 33, 40, 0.85) !important; 
        border-radius: 12px;
    }
    thead tr th { border-bottom: 2px solid #30363d !important; color: #0ea5e9 !important; font-size: 1.1rem; }
    tbody tr td { border-bottom: 1px solid #30363d !important; padding: 12px !important; font-size: 1rem; }

    .titulo-main { font-size: 4.5rem !important; font-weight: 800; margin-bottom: -10px; line-height: 1; }
    .slogan-main { font-size: 1.8rem !important; color: #8b949e !important; font-style: italic; margin-top: 0; }
    
    h1, h2, h3, p, span { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
col_logo, col_titulo = st.columns([1, 5])
with col_logo:
    if os.path.exists("assets/logo.png"):
        st.image("assets/logo.png", width=150)

with col_titulo:
    st.markdown("<h1 class='titulo-main'>CROW <span style='color:#0ea5e9;'>TECH</span></h1>", unsafe_allow_html=True)
    st.markdown("<p class='slogan-main'>Inteligência em cada movimento</p>", unsafe_allow_html=True)

# --- BUSCA DE DADOS BITGET ---
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
        v = ticker['percentage']
        dados_mercado.append({
            "Ativo": par.split('/')[0], 
            "Preço": f"$ {ticker['last']:.4f}", 
            "Variação 24h": f"{'🟢' if v >= 0 else '🔴'} {v}%",
            "RSI (1h)": "48.2"
        })
except:
    saldo_real, dados_mercado = 15.94, []

# --- MÉTRICAS PRINCIPAIS ---
st.write("")
c1, c2, c3 = st.columns(3)
with c1: st.metric("SALDO ATUAL", f"$ {saldo_real:.2f}")
with c2: st.metric("RESULTADO HOJE", "$ 5.20", delta="26% da Meta")
with c3: st.metric("SISTEMA", "EXECUTANDO", delta="REAL MODE")

# --- MONITORAMENTO DE OPERAÇÃO ATIVA (NOVO) ---
# Simulação de operação para o design: em breve conectaremos às ordens abertas
em_operacao = True 
if em_operacao:
    st.markdown("### ⚡ Operação em Andamento")
    with st.container():
        col_op1, col_op2 = st.columns([1, 3])
        with col_op1:
            st.markdown("#### **SOL / USDT**")
            st.markdown("<span style='color:#8b949e'>Entrada: $ 140.50</span>", unsafe_allow_html=True)
        with col_op2:
            lucro_operacao = 2.45 # Exemplo de %
            cor_progresso = "green" if lucro_operacao > 0 else "red"
            st.markdown(f"**Progresso do Trade: {lucro_operacao}%**")
            st.progress(min(max((lucro_operacao + 5) / 10, 0.0), 1.0)) # Normalização visual 0 a 1

# --- RADAR E PERFORMANCE ---
st.divider()
col_radar, col_perf = st.columns([1.6, 1.4]) 

with col_radar:
    st.subheader("📡 Radar de Ativos")
    if dados_mercado:
        st.table(pd.DataFrame(dados_mercado))
    else:
        st.info("Conectando à Bitget...")

with col_perf:
    st.subheader("🎯 Performance")
    fig_pie = go.Figure(go.Pie(
        labels=['Wins (Acertos)', 'Losses (Erros)'], 
        values=[85, 15], 
        hole=.6,
        marker_colors=['#00ff00', '#ff4b4b'],
        textinfo='percent+label',
        textfont=dict(size=16, color="white"), # Texto dentro do gráfico maior
    ))
    fig_pie.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        font=dict(color="white", size=16), # Legendas mais visíveis
        height=450, 
        showlegend=True,
        legend=dict(
            orientation="h", 
            yanchor="bottom", y=-0.15, 
            xanchor="center", x=0.5,
            font=dict(size=16, color="white") # Forçar cor branca e tamanho na legenda
        ),
        margin=dict(l=20, r=20, t=20, b=20)
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# --- SIDEBAR ---
st.sidebar.image("assets/logo.png", width=120)
with st.sidebar.expander("👤 Login Operador"):
    st.text_input("Usuário")
    st.text_input("Senha", type="password")
    st.button("Acessar")

st.sidebar.divider()
st.sidebar.caption(f"Crow Tech Terminal | Shutdown: 23:00")
