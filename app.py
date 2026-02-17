import streamlit as st
import ccxt
import pandas as pd
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh
import os

# CONFIGURAÇÃO DE PÁGINA
st.set_page_config(page_title="Crow Tech Elite", layout="wide", initial_sidebar_state="collapsed")
st_autorefresh(interval=30000, key="datarefresh")

# --- CSS PARA DEIXAR TUDO DARK (INCLUINDO MENUS) ---
st.markdown("""
    <style>
    /* Fundo Principal */
    .stApp {
        background-color: #0e1117;
        background-image: linear-gradient(rgba(14, 17, 23, 0.93), rgba(14, 17, 23, 0.93)), 
                          url("https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/logo.png");
        background-attachment: fixed;
        background-size: 45%;
        background-repeat: no-repeat; background-position: center;
    }
    
    /* MENU LATERAL TOTAL DARK */
    [data-testid="stSidebar"] { background-color: #161b22 !important; border-right: 1px solid #30363d; }
    [data-testid="stSidebarNav"] { background-color: #161b22 !important; }
    
    /* REMOVER FUNDO BRANCO DOS SUBMENUS (EXPANDERS) */
    .streamlit-expanderHeader { background-color: #1c2128 !important; border: 1px solid #30363d !important; border-radius: 8px !important; }
    .streamlit-expanderContent { background-color: #161b22 !important; color: white !important; border: none !important; }
    
    /* METRICS E TEXTOS */
    [data-testid="stMetric"] { background-color: rgba(28, 33, 40, 0.95) !important; border-radius: 15px; padding: 25px !important; }
    .titulo-main { font-size: 4rem !important; font-weight: 800; color: white; line-height: 1; }
    .slogan-main { font-size: 1.6rem !important; color: #8b949e !important; font-style: italic; }
    h1, h2, h3, p, span, label { color: white !important; }
    
    /* Ajuste das tabelas para Dark */
    .stTable { background-color: transparent !important; }
    thead tr th { border-bottom: 2px solid #30363d !important; color: #0ea5e9 !important; }
    tbody tr td { border-bottom: 1px solid #30363d !important; }
    </style>
    """, unsafe_allow_html=True)

# --- MENU LATERAL (SIDEBAR) ---
with st.sidebar:
    st.image("assets/logo.png", width=120)
    st.markdown("### 🖥️ PAINEL DE CONTROLE")
    
    with st.expander("🔄 GESTÃO DE PARES"):
        lista_20 = ['SOL/USDT', 'BTC/USDT', 'ETH/USDT', 'XRP/USDT', 'DOGE/USDT', 'TRX/USDT', 'ADA/USDT', 'LINK/USDT', 'AVAX/USDT']
        selecionados = st.multiselect("Selecione (Min. 4):", lista_20, default=['SOL/USDT', 'BTC/USDT', 'ETH/USDT', 'XRP/USDT'])

    with st.expander("💰 FINANCEIRO"):
        st.button("➕ ADICIONAR FUNDOS", use_container_width=True)
        st.button("➖ RETIRAR LUCROS", use_container_width=True)

    with st.expander("⚙️ CONFIGURAÇÕES"):
        st.text_input("E-mail para alertas")
        st.text_input("Nova Senha", type="password")
        st.button("SALVAR")

    st.divider()
    st.caption("CROW TECH v3.5 | 23:45")

# --- CABEÇALHO ---
col_logo, col_titulo = st.columns([1, 5])
with col_logo:
    if os.path.exists("assets/logo.png"): st.image("assets/logo.png", width=130)
with col_titulo:
    st.markdown("<h1 class='titulo-main'>CROW <span style='color:#0ea5e9;'>TECH</span></h1>", unsafe_allow_html=True)
    st.markdown("<p class='slogan-main'>Inteligência em cada movimento</p>", unsafe_allow_html=True)

# --- CORPO PRINCIPAL ---
st.write("")
c1, c2, c3 = st.columns(3)
with c1: st.metric("SALDO BITGET", "$ 185.50")
with c2: st.metric("LUCRO HOJE", "$ 5.20", delta="Win")
with c3: st.metric("STATUS", "REAL MODE", delta="OPERANDO")

st.divider()
col_left, col_right = st.columns([1.6, 1.4])

with col_left:
    st.subheader("📡 Radar de Ativos")
    df = pd.DataFrame({
        "Ativo": [p.split('/')[0] for p in selecionados],
        "Preço": ["$ ---" for _ in selecionados],
        "Sinal": ["Aguardando..." for _ in selecionados]
    })
    st.table(df)

with col_right:
    st.subheader("🎯 Performance")
    fig = go.Figure(go.Pie(labels=['Wins', 'Losses'], values=[85, 15], hole=.6, marker_colors=['#00ff00', '#ff4b4b']))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='white', height=350, showlegend=True,
                      legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5, font=dict(color="white")))
    st.plotly_chart(fig, use_container_width=True)
