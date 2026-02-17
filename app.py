import streamlit as st
import ccxt
import pandas as pd
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh
import os

# CONFIGURAÇÃO DE PÁGINA
st.set_page_config(page_title="Crow Tech Elite", layout="wide", initial_sidebar_state="expanded")
st_autorefresh(interval=30000, key="datarefresh")

# --- ESTILO CROW TECH ---
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
    [data-testid="stMetric"] { background-color: rgba(28, 33, 40, 0.95) !important; border-radius: 15px; padding: 25px !important; border: none !important; }
    .titulo-main { font-size: 4.5rem !important; font-weight: 800; margin-bottom: -10px; line-height: 1; color: white; }
    .slogan-main { font-size: 1.8rem !important; color: #8b949e !important; font-style: italic; margin-top: 0; }
    h1, h2, h3, p, span { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: GESTÃO DE 20 PARES ---
st.sidebar.image("assets/logo.png", width=100)
st.sidebar.title("Comandos Elite")

with st.sidebar.expander("🔄 Gestão de Pares (Escolha 6)"):
    # Lista de 20 Pares sugeridos por liquidez
    lista_20_pares = [
        'SOL/USDT', 'BTC/USDT', 'ETH/USDT', 'XRP/USDT', 'DOGE/USDT', 'TRX/USDT',
        'ADA/USDT', 'MATIC/USDT', 'DOT/USDT', 'LINK/USDT', 'AVAX/USDT', 'SHIB/USDT',
        'LTC/USDT', 'BCH/USDT', 'UNI/USDT', 'NEAR/USDT', 'APT/USDT', 'ARB/USDT',
        'TIA/USDT', 'OP/USDT'
    ]
    
    # Seleção múltipla
    selecionados = st.multiselect(
        "Selecione os ativos ativos:",
        lista_20_pares,
        default=['SOL/USDT', 'BTC/USDT', 'ETH/USDT', 'XRP/USDT', 'DOGE/USDT', 'TRX/USDT']
    )
    
    if len(selecionados) < 6:
        st.sidebar.warning("⚠️ Mantenha pelo menos 6 pares ativos para operação total.")
    elif len(selecionados) > 6:
        st.sidebar.error("❌ Limite de 6 pares excedido. Desmarque algum.")
    else:
        st.sidebar.success("✅ Grade de 6 pares pronta.")

# --- FINANCEIRO E SEGURANÇA NO MENU ---
with st.sidebar.expander("💰 Financeiro"):
    st.button("➕ Adicionar Fundos")
    st.button("➖ Retirar Lucros")

with st.sidebar.expander("🔒 Segurança"):
    st.text_input("E-mail de Cadastro")
    st.text_input("Senha do Painel", type="password")
    st.button("Atualizar Segurança")

st.sidebar.divider()
st.sidebar.caption("Crow Tech Terminal v3.2")

# --- CABEÇALHO ---
col_logo, col_titulo = st.columns([1, 5])
with col_logo:
    if os.path.exists("assets/logo.png"):
        st.image("assets/logo.png", width=150)
with col_titulo:
    st.markdown("<h1 class='titulo-main'>CROW <span style='color:#0ea5e9;'>TECH</span></h1>", unsafe_allow_html=True)
    st.markdown("<p class='slogan-main'>Inteligência em cada movimento</p>", unsafe_allow_html=True)

# --- LÓGICA DE DADOS REAIS (Baseado na Seleção do Usuário) ---
dados_radar = []
saldo_real = 185.50 # Placeholder enquanto reconecta API

try:
    if len(selecionados) == 6:
        exchange = ccxt.bitget({
            'apiKey': st.secrets["BITGET_API_KEY"],
            'secret': st.secrets["BITGET_SECRET"],
            'password': st.secrets["BITGET_PASSWORD"],
        })
        for par in selecionados:
            t = exchange.fetch_ticker(par)
            dados_radar.append({
                "Ativo": par.split('/')[0],
                "Preço": f"$ {t['last']:.4f}",
                "Var 24h": f"{'🟢' if t['percentage'] >= 0 else '🔴'} {t['percentage']}%",
                "RSI": "42.5"
            })
except:
    dados_radar = [{"Ativo": p.split('/')[0], "Preço": "API OFF", "Var 24h": "---", "RSI": "---"} for p in selecionados]

# --- PAINEL DE MONITORAMENTO ---
st.write("")
m1, m2, m3 = st.columns(3)
with m1: st.metric("SALDO BITGET", f"$ {saldo_real:.2f}")
with m2: st.metric("LUCRO ESTIMADO", "$ 5.20", delta="Hoje")
with m3: st.metric("GRADE ATIVA", f"{len(selecionados)}/6 Ativos")

st.divider()
col_radar, col_perf = st.columns([1.6, 1.4])

with col_radar:
    st.subheader("📡 Radar de Ativos Selecionados")
    if selecionados:
        st.table(pd.DataFrame(dados_radar))
    else:
        st.info("Selecione os pares no menu lateral.")

with col_perf:
    st.subheader("🎯 Performance Global")
    fig = go.Figure(go.Pie(labels=['Wins', 'Losses'], values=[85, 15], hole=.6, marker_colors=['#00ff00', '#ff4b4b']))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='white', height=350, showlegend=True,
                      legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5, font=dict(size=14, color="white")))
    st.plotly_chart(fig, use_container_width=True)
