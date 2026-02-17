import streamlit as st
import ccxt
import pandas as pd
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh
import os

# CONFIGURAÇÃO DE PÁGINA
st.set_page_config(page_title="Crow Tech Elite", layout="wide", initial_sidebar_state="collapsed")
st_autorefresh(interval=30000, key="datarefresh")

# CSS: ESTILO DARK, FUNDO COM LOGO E REMOÇÃO DE CONTORNOS
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        background-image: linear-gradient(rgba(14, 17, 23, 0.88), rgba(14, 17, 23, 0.88)), 
                          url("https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/logo.png");
        background-attachment: fixed;
        background-size: 55%;
        background-repeat: no-repeat;
        background-position: center;
    }
    
    /* REMOVER CONTORNOS AZUIS DOS METRICS */
    [data-testid="stMetric"] {
        background-color: rgba(28, 33, 40, 0.85) !important;
        border: none !important; /* Retira o contorno azul */
        border-radius: 12px;
        padding: 20px !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    /* AJUSTE DAS LINHAS DA TABELA (RADAR) */
    .stTable { 
        background-color: rgba(28, 33, 40, 0.85) !important; 
        border-radius: 10px;
    }
    th { color: #0ea5e9 !important; border-bottom: 1px solid #30363d !important; }
    td { border-bottom: 1px solid #30363d !important; color: white !important; }

    /* TEXTOS MAIORES */
    h1 { font-size: 3.5rem !important; margin-bottom: 0 !important; }
    .slogan { font-size: 1.5rem !important; color: #8b949e !important; font-style: italic; }
    
    h1, h2, h3, p, span { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO (LOGO E TÍTULO AMPLIADOS) ---
col_logo, col_titulo = st.columns([1, 5])
with col_logo:
    if os.path.exists("assets/logo.png"):
        st.image("assets/logo.png", width=140)

with col_titulo:
    st.markdown("<h1>CROW <span style='color:#0ea5e9;'>TECH</span></h1>", unsafe_allow_html=True)
    st.markdown("<p class='slogan'>Inteligência em cada movimento</p>", unsafe_allow_html=True)

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
        var = ticker['percentage']
        cor_var = "🟢" if var >= 0 else "🔴"
        dados_mercado.append({
            "Ativo": par.split('/')[0], 
            "Preço": f"$ {ticker['last']:.4f}", 
            "24h %": f"{cor_var} {var}%",
            "RSI (1h)": "48.2"
        })
except:
    saldo_real = 15.94
    dados_mercado = [{"Ativo": p, "Preço": "API Offline", "24h %": "---", "RSI (1h)": "---"} for p in pares]

# --- PAINEL DE MÉTRICAS ---
st.write("")
c1, c2, c3 = st.columns(3)
with c1: st.metric("SALDO EM CARTEIRA", f"$ {saldo_real:.2f}")
with c2: st.metric("LUCRO SESSÃO", "$ 5.20", delta="26% da Meta")
with c3: st.metric("SISTEMA", "MONITORANDO", delta="MODO DESIGN")

# --- CONTEÚDO PRINCIPAL ---
st.divider()
col_radar, col_perf = st.columns([1.8, 1.2]) # Gráfico de performance agora tem mais espaço

with col_radar:
    st.subheader("📡 Radar de Ativos (Grade Completa)")
    st.table(pd.DataFrame(dados_mercado))

with col_perf:
    st.subheader("🎯 Performance de Operações")
    # Gráfico maior e com legenda
    fig_pie = go.Figure(go.Pie(
        labels=['Wins (Acertos)', 'Losses (Erros)'], 
        values=[85, 15], 
        hole=.6,
        marker_colors=['#00ff00', '#ff4b4b'],
        textinfo='percent+label'
    ))
    fig_pie.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        font_color='white', 
        height=400, # Aumentado
        showlegend=True, # Legenda ativada
        legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5),
        margin=dict(l=10, r=10, t=10, b=10)
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# --- SIDEBAR ---
st.sidebar.image("assets/logo.png", width=100)
st.sidebar.title("Configurações")
with st.sidebar.expander("👤 Login do Operador"):
    st.text_input("User")
    st.text_input("Pass", type="password")
    st.button("Entrar")

st.sidebar.divider()
st.sidebar.write(f"🛑 Shutdown: 23:00")
st.sidebar.caption("Crow Tech Terminal v2.6")
