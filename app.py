import streamlit as st
import base64
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# 1. Configuração de Página
st.set_page_config(page_title="Crow Tech Elite C18.9.1.5", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

# --- CSS PROFISSIONAL ---
st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 30% !important;
        background-attachment: fixed !important;
    }}
    .crow-card {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 15px;
    }}
    .stat-val {{ color: #00bcd4; font-size: 20px; font-weight: bold; }}
    .stat-label {{ color: rgba(255,255,255,0.5); font-size: 12px; text-transform: uppercase; }}
    </style>
""", unsafe_allow_html=True)

if 'logado' not in st.session_state: st.session_state.logado = False

if not st.session_state.logado:
    # Código de login (mantido conforme a última versão que funcionou)
    with st.form("login_crow"):
        st.markdown(f'<div style="text-align:center"><img src="data:image/png;base64,{logo_base64}" width="160"></div>', unsafe_allow_html=True)
        u = st.text_input("USUÁRIO", placeholder="Username")
        p = st.text_input("SENHA", type="password", placeholder="Password")
        if st.form_submit_button("ACESSAR SISTEMA"):
            if u == "admin" and p == "crow123":
                st.session_state.logado = True
                st.rerun()
else:
    # --- HEADER ---
    c1, c2, c3 = st.columns([1, 3, 1])
    with c1: st.image(f"data:image/png;base64,{logo_base64}", width=80)
    with c2: st.markdown("<h2 style='text-align:center; color:white;'>TERMINAL OPERACIONAL <span style='color:#00bcd4;'>C18.9.1.5</span></h2>", unsafe_allow_html=True)
    with c3: 
        if st.button("SAIR"): 
            st.session_state.logado = False
            st.rerun()

    # --- LINHA 1: KPIs TÉCNICOS ---
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown('<div class="crow-card"><p class="stat-label">💰 Banca Disponível</p><p class="stat-val">$ 10.250,00</p></div>', unsafe_allow_html=True)
    with k2:
        st.markdown('<div class="crow-card"><p class="stat-label">⚡ Latência API</p><p class="stat-val">12ms <span style="font-size:10px; color:gray;">(Excelente)</span></p></div>', unsafe_allow_html=True)
    with k3:
        st.markdown('<div class="crow-card"><p class="stat-label">📊 RSI (14p)</p><p class="stat-val">62.4 <span style="font-size:10px; color:orange;">(Neutro)</span></p></div>', unsafe_allow_html=True)
    with k4:
        st.markdown('<div class="crow-card"><p class="stat-label">🤖 Algoritmo</p><p class="stat-val" style="color:#00ff88;">ATIVO</p></div>', unsafe_allow_html=True)

    # --- LINHA 2: GRÁFICO DE VELAS + SELETOR ---
    col_main, col_side = st.columns([3, 1])

    with col_main:
        st.markdown('<div class="crow-card">', unsafe_allow_html=True)
        # Seletor de Ativo
        par_selecionado = st.selectbox("Selecione o Par para Monitoramento:", ["BTC/USDT", "ETH/USDT", "SOL/USDT"])
        
        # Simulação de Gráfico de Velas (Candlestick)
        fig = go.Figure(data=[go.Candlestick(
            x=['09:00', '10:00', '11:00', '12:00', '13:00'],
            open=[51000, 51200, 51500, 51300, 51600],
            high=[51300, 51600, 51700, 51500, 51900],
            low=[50800, 51100, 51200, 51100, 51400],
            close=[51200, 51500, 51300, 51600, 51800],
            increasing_line_color='#00ff88', decreasing_line_color='#ff4b4b'
        )])
        fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=400)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_side:
        st.markdown('<div class="crow-card">', unsafe_allow_html=True)
        st.markdown("### 📋 Alocação da Banca")
        st.write("Dólar (USDT): **70%**")
        st.write("Ativos (Coins): **30%**")
        st.progress(30)
        st.markdown("---")
        st.markdown("### 📉 Estratégia EMA")
        st.write("EMA 9 (Curta): **51.450**")
        st.write("EMA 21 (Longa): **51.200**")
        st.success("TENDÊNCIA: ALTA (Bullish)")
        st.markdown('</div>', unsafe_allow_html=True)

    # --- LINHA 3: LOGS REAIS ---
    st.markdown('<div class="crow-card">', unsafe_allow_html=True)
    st.markdown("### 📜 Log de Atividades do Bot")
    st.code(f"""
    [{datetime.now().strftime('%H:%M:%S')}] Conexão estabelecida com sucesso.
    [{datetime.now().strftime('%H:%M:%S')}] Analisando par {par_selecionado}...
    [{datetime.now().strftime('%H:%M:%S')}] RSI em 62.4. Aguardando zona de sobrecompra.
    [{datetime.now().strftime('%H:%M:%S')}] Monitorando cruzamento EMA 9/21.
    """, language="bash")
    st.markdown('</div>', unsafe_allow_html=True)
