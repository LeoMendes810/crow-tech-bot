import streamlit as st
import base64
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# 1. Configuração de Marca e Dashboard SaaS
st.set_page_config(page_title="Crow Tech Elite Portal", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

# --- CSS DE NÍVEL INDUSTRIAL (CORREÇÕES DE VISIBILIDADE) ---
st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 25% !important;
        background-attachment: fixed !important;
    }}
    /* Cards de Vidro */
    .product-card {{
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    }}
    .metric-label {{ color: rgba(255,255,255,0.7); font-size: 11px; text-transform: uppercase; font-weight: bold; }}
    .metric-value {{ color: #00bcd4; font-size: 22px; font-weight: bold; }}
    
    /* Correção do Console */
    .stCodeBlock {{
        background-color: rgba(0, 0, 0, 0.6) !important;
        border: 1px solid rgba(0, 188, 212, 0.3) !important;
        border-radius: 8px;
    }}
    .stCodeBlock code {{ color: #00ff88 !important; }}

    /* Legendas da Estratégia */
    .config-label {{
        color: #FFFFFF !important;
        font-weight: bold;
        font-size: 14px;
        margin-bottom: 5px;
        display: block;
    }}
    .instruction-text {{
        color: #00bcd4;
        font-size: 11px;
        font-style: italic;
    }}
    </style>
""", unsafe_allow_html=True)

if 'logado' not in st.session_state: st.session_state.logado = False
if 'meta_lucro' not in st.session_state: st.session_state.meta_lucro = 500.0
if 'lucro_atual' not in st.session_state: st.session_state.lucro_atual = 425.10

if not st.session_state.logado:
    # TELA DE LOGIN (MANTIDA)
    _, center, _ = st.columns([1, 1, 1])
    with center:
        st.markdown(f'<div style="text-align:center; margin-top:50px;"><img src="data:image/png;base64,{logo_base64}" width="180"></div>', unsafe_allow_html=True)
        with st.form("auth"):
            u = st.text_input("USUÁRIO")
            p = st.text_input("SENHA", type="password")
            if st.form_submit_button("ACESSAR SISTEMA"):
                if u == "admin" and p == "crow123":
                    st.session_state.logado = True
                    st.rerun()
else:
    # --- HEADER ---
    c1, c2, c3 = st.columns([1, 4, 1])
    with c1: st.image(f"data:image/png;base64,{logo_base64}", width=80)
    with c2: st.markdown("<h2 style='color:white; text-align:center;'>CROW TECH <span style='color:#00bcd4;'>PORTAL ELITE</span></h2>", unsafe_allow_html=True)
    with c3: 
        if st.button("SAIR"): 
            st.session_state.logado = False
            st.rerun()

    tab_dash, tab_strat, tab_api = st.tabs(["📊 DASHBOARD OPERACIONAL", "⚙️ CONFIGURAÇÃO DE SCRIPT", "🔐 CHAVES API"])

    with tab_dash:
        # Linha 1: Métricas e Progresso de Meta
        m1, m2, m3 = st.columns([1, 1, 2])
        with m1:
            st.markdown(f'<div class="product-card"><p class="metric-label">Banca Atual</p><p class="metric-value">$ 10.250,00</p></div>', unsafe_allow_html=True)
        with m2:
            st.markdown(f'<div class="product-card"><p class="metric-label">Lucro do Dia</p><p class="metric-value" style="color:#00ff88;">+ $ {st.session_state.lucro_atual}</p></div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            progresso = min(st.session_state.lucro_atual / st.session_state.meta_lucro, 1.0)
            st.markdown(f'<p class="metric-label">Meta Diária: $ {st.session_state.meta_lucro}</p>', unsafe_allow_html=True)
            st.progress(progresso)
            st.markdown(f'<p style="text-align:right; font-size:10px; color:#00bcd4;">{progresso*100:.1f}% da meta alcançada</p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        col_video, col_console = st.columns([2, 1])
        with col_video:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            st.markdown("<p class='metric-label'>Monitoramento: BTC/USDT (Velas de 1m)</p>", unsafe_allow_html=True)
            # Gráfico de Velas
            fig = go.Figure(data=[go.Candlestick(x=[1,2,3,4,5], open=[51,52,51,53,54], high=[53,54,52,55,56], low=[50,51,49,52,53], close=[52,51,53,54,55])])
            fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=300, margin=dict(l=0,r=0,t=0,b=0))
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col_console:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            st.markdown("<p class='metric-label'>Console de Operação</p>", unsafe_allow_html=True)
            st.code(f"[{datetime.now().strftime('%H:%M:%S')}]\nAnalysing Market...\nEMA 9/21: Bullish\nRSI: 58.2\nStatus: Scanning...", language="bash")
            st.button("🚀 INICIAR ENGINE", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    with tab_strat:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("### 🛠️ Ajuste Fino do Algoritmo")
        st.markdown("<p class='instruction-text'>As alterações abaixo afetam o comportamento do bot em tempo real.</p>", unsafe_allow_html=True)
        
        c_a, c_b = st.columns(2)
        with c_a:
            st.markdown('<span class="config-label">Gatilho RSI (Compra)</span>', unsafe_allow_html=True)
            st.markdown('<p class="instruction-text">Define o ponto de sobrevenda para entrada.</p>', unsafe_allow_html=True)
            st.slider("RSI Low", 10, 45, 30, label_visibility="collapsed")
            
            st.markdown('<br><span class="config-label">Stop Loss (%)</span>', unsafe_allow_html=True)
            st.markdown('<p class="instruction-text">Limite máximo de perda por operação.</p>', unsafe_allow_html=True)
            st.number_input("SL", 0.5, 5.0, 1.5, label_visibility="collapsed")

        with c_b:
            st.markdown('<span class="config-label">Meta de Lucro Diária ($)</span>', unsafe_allow_html=True)
            st.markdown('<p class="instruction-text">O bot parará ao atingir este valor.</p>', unsafe_allow_html=True)
            st.session_state.meta_lucro = st.number_input("Meta", 10.0, 5000.0, float(st.session_state.meta_lucro), label_visibility="collapsed")

            st.markdown('<br><span class="config-label">Timeframe</span>', unsafe_allow_html=True)
            st.markdown('<p class="instruction-text">Intervalo das velas para análise técnica.</p>', unsafe_allow_html=True)
            st.selectbox("TF", ["1m", "5m", "15m", "1h"], label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab_api:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("### 🔐 Conexão com Corretora")
        st.info("As chaves são enviadas via túnel criptografado diretamente para o núcleo do script.")
        st.text_input("API KEY", type="password", placeholder="Insira sua chave pública")
        st.text_input("SECRET KEY", type="password", placeholder="Insira sua chave privada")
        st.button("VINCULAR CONTA")
        st.markdown('</div>', unsafe_allow_html=True)
