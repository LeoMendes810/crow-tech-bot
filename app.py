import streamlit as st
import ccxt
import pandas as pd
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh
import os

# CONFIGURAÇÃO DE PÁGINA
st.set_page_config(page_title="Crow Tech Elite", layout="wide", initial_sidebar_state="collapsed")

# Atualiza os dados a cada 30 segundos sem "matar" o visual
st_autorefresh(interval=30000, key="datarefresh")

# CSS AVANÇADO: FUNDO COM LOGO E SEM PISCAR
st.markdown("""
    <style>
    /* Fundo Total Escuro com Imagem de Fundo (Corvo) */
    .stApp {
        background-color: #0e1117;
        background-image: linear-gradient(rgba(14, 17, 23, 0.85), rgba(14, 17, 23, 0.85)), 
                          url("https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/logo.png");
        background-attachment: fixed;
        background-size: 60%; /* Tamanho do corvo no fundo */
        background-repeat: no-repeat;
        background-position: center;
    }
    
    /* Remover o "piscar" visual e bordas brancas */
    .block-container { padding-top: 1rem; }
    
    /* Estilizar Tabelas e Métricas para modo transparente */
    [data-testid="stMetric"] {
        background-color: rgba(28, 33, 40, 0.9) !important;
        border: 1px solid #0ea5e9 !important;
        backdrop-filter: blur(5px);
    }
    
    .stTable { 
        background-color: rgba(28, 33, 40, 0.9) !important; 
        border-radius: 10px;
    }

    h1, h2, h3, p, span { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
col_logo, col_titulo = st.columns([1, 4])
with col_logo:
    if os.path.exists("assets/logo.png"):
        st.image("assets/logo.png", width=120)

with col_titulo:
    st.markdown("<h1 style='margin-bottom:0;'>CROW <span style='color:#0ea5e9;'>TECH</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-style:italic; color:#8b949e;'>Seu estilo em jogo | Inteligência em cada movimento</p>", unsafe_allow_html=True)

# --- BUSCA DE DADOS (6 MOEDAS) ---
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
        # Lógica de cor para variação
        var = ticker['percentage']
        cor_var = "🟢" if var >= 0 else "🔴"
        
        dados_mercado.append({
            "Ativo": par.split('/')[0], 
            "Preço": f"$ {ticker['last']:.4f}", 
            "24h %": f"{cor_var} {var}%",
            "RSI (1h)": "48.2" # Calibração em breve
        })
except:
    saldo_real = 185.50
    dados_mercado = [{"Ativo": p, "Preço": "API Offline", "24h %": "---", "RSI (1h)": "---"} for p in pares]

# --- PAINEL PRINCIPAL ---
st.write("")
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("CARTEIRA BITGET", f"$ {saldo_real:.2f}", delta="Saldo Real")

with c2:
    meta, ganho = 20.0, 5.20
    st.metric("META DIÁRIA", f"$ {ganho:.2f}", delta=f"{(ganho/meta)*100:.1f}% para o objetivo")
    st.progress(ganho/meta)

with c3:
    st.metric("BOT STATUS", "OPERANDO", delta=f"{len(pares)} Pares Ativos")

# --- RADAR E PERFORMANCE ---
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
    fig_pie.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=280,
        showlegend=False,
        margin=dict(l=10, r=10, t=10, b=10)
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# --- SIDEBAR (LOGIN E OPÇÕES) ---
st.sidebar.image("assets/logo.png", width=100)
st.sidebar.markdown("### Área Restrita")
if st.sidebar.button("👤 Acessar Login"):
    st.sidebar.warning("Módulo de Login em desenvolvimento.")

st.sidebar.divider()
st.sidebar.write(f"🛑 Shutdown: 23:00")
st.sidebar.caption("Crow Tech Bot v2.0")
