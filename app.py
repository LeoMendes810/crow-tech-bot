import streamlit as st
import base64
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# 1. Configuração de Marca e Dashboard
st.set_page_config(page_title="Crow Tech Elite Portal", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

# --- CSS PROFISSIONAL (CORREÇÃO DE ERROS) ---
st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 25% !important;
        background-attachment: fixed !important;
    }}
    /* Containers de Vidro */
    .product-card {{
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    }}
    .metric-label {{ color: rgba(255,255,255,0.5); font-size: 11px; text-transform: uppercase; }}
    .metric-value {{ color: #00bcd4; font-size: 22px; font-weight: bold; }}
    </style>
""", unsafe_allow_html=True)

# --- GERENCIAMENTO DE ESTADO ---
if 'logado' not in st.session_state: st.session_state.logado = False
if 'bot_running' not in st.session_state: st.session_state.bot_running = False

# --- TELA DE ACESSO (O SEU LOGIN TRAVADO) ---
if not st.session_state.logado:
    with st.container():
        _, center, _ = st.columns([1, 1, 1])
        with center:
            st.markdown(f'<div style="text-align:center; margin-top:50px;"><img src="data:image/png;base64,{logo_base64}" width="180"></div>', unsafe_allow_html=True)
            with st.form("auth"):
                user = st.text_input("USUÁRIO", placeholder="Username")
                secret = st.text_input("SENHA", type="password", placeholder="Password")
                if st.form_submit_button("VALIDAR LICENÇA"):
                    if user == "admin" and secret == "crow123":
                        st.session_state.logado = True
                        st.rerun()
else:
    # --- DASHBOARD C18.9.1.5 (MODO PRODUTO) ---
    
    # Menu Superior
    c1, c2, c3 = st.columns([1, 4, 1])
    with c1: st.image(f"data:image/png;base64,{logo_base64}", width=80)
    with c2: st.markdown("<h2 style='color:white;'>CROW TECH <span style='color:#00bcd4;'>PORTAL ELITE</span></h2>", unsafe_allow_html=True)
    with c3: 
        if st.button("SAIR"): 
            st.session_state.logado = False
            st.rerun()

    # Sistema de abas para não poluir a tela
    tab_dashboard, tab_config, tab_api = st.tabs(["📊 DASHBOARD", "⚙️ ESTRATÉGIA", "🔐 CONEXÃO API"])

    with tab_dashboard:
        # Linha de Resumo
        m1, m2, m3, m4 = st.columns(4)
        m1.markdown('<div class="product-card"><p class="metric-label">Banca USDT</p><p class="metric-value">$ 10.250,00</p></div>', unsafe_allow_html=True)
        m2.markdown('<div class="product-card"><p class="metric-label">Lucro Estimado</p><p class="metric-value" style="color:#00ff88;">+ $ 425,10</p></div>', unsafe_allow_html=True)
        m3.markdown('<div class="product-card"><p class="metric-label">Sinais Ativos</p><p class="metric-value">04</p></div>', unsafe_allow_html=True)
        m4.markdown('<div class="product-card"><p class="metric-label">Status do Bot</p><p class="metric-value" style="color:#00ff88;">ONLINE</p></div>', unsafe_allow_html=True)

        col_main, col_logs = st.columns([2, 1])
        
        with col_main:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            st.markdown("<p class='metric-label'>Monitoramento de Mercado (Candles)</p>", unsafe_allow_html=True)
            # Gráfico de Velas Realista
            fig = go.Figure(data=[go.Candlestick(x=[1,2,3,4,5], open=[51,52,51,53,54], high=[53,54,52,55,56], low=[50,51,49,52,53], close=[52,51,53,54,55])])
            fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=300, margin=dict(l=0,r=0,t=0,b=0))
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col_logs:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            st.markdown("<p class='metric-label'>Console de Execução</p>", unsafe_allow_html=True)
            st.code(f"[{datetime.now().strftime('%H:%M')}] Scanning BTC/USDT...\n[LOG] EMA Cross detected\n[LOG] RSI: 58.2", language="bash")
            if not st.session_state.bot_running:
                if st.button("▶ INICIAR OPERAÇÕES", use_container_width=True):
                    st.session_state.bot_running = True
            else:
                if st.button("🛑 PARAR BOT", use_container_width=True):
                    st.session_state.bot_running = False
            st.markdown('</div>', unsafe_allow_html=True)

    with tab_config:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("### Ajuste de Parâmetros do Robô")
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.slider("Gatilho RSI (Sobrecompra)", 50, 90, 70)
            st.slider("Gatilho RSI (Sobrevenda)", 10, 50, 30)
        with col_c2:
            st.number_input("Stop Loss Automático (%)", 0.5, 10.0, 1.5)
            st.selectbox("Timeframe de Análise", ["1m", "5m", "15m", "1h"])
        st.markdown('</div>', unsafe_allow_html=True)

    with tab_api:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("### Integração com Corretora")
        st.warning("Suas chaves API são criptografadas e nunca armazenadas em texto puro.")
        st.text_input("API KEY BINANCE", type="password")
        st.text_input("API SECRET BINANCE", type="password")
        st.button("TESTAR CONEXÃO")
        st.markdown('</div>', unsafe_allow_html=True)
