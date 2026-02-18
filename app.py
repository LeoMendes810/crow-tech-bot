import streamlit as st
import base64
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# 1. Configurações Globais
st.set_page_config(page_title="Crow Tech Elite Portal", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

# --- CSS DE ELITE (REMOÇÃO DE BRANCO E AJUSTE DE SLOGAN) ---
st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 18% !important;
        background-attachment: fixed !important;
        color: white !important;
    }}
    
    /* Cards Pretos Translúcidos */
    .product-card {{
        background: rgba(0, 0, 0, 0.85) !important;
        border: 1px solid rgba(0, 188, 212, 0.4);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    }}

    /* Botões Customizados */
    div.stButton > button {{
        background-color: #00bcd4 !important;
        color: #000000 !important;
        border: none !important;
        font-weight: 900 !important;
        text-transform: uppercase;
    }}
    
    /* Botão Sair (Vermelho Dark) */
    div.stButton > button[kind="secondary"] {{
        background-color: rgba(255, 75, 75, 0.2) !important;
        color: #ff4b4b !important;
        border: 1px solid #ff4b4b !important;
    }}

    /* Console Estilo Matrix */
    .stCodeBlock, div[data-testid="stCodeBlock"], div[data-testid="stCodeBlock"] > pre {{
        background-color: #000000 !important;
        border: 1px solid #00bcd4 !important;
    }}
    code {{ color: #00ff88 !important; background-color: transparent !important; }}

    /* Texto de Meta Reforçado */
    .meta-label {{
        color: #00bcd4 !important;
        font-weight: 900 !important;
        font-size: 14px;
        text-transform: uppercase;
        margin-bottom: 5px;
        display: block;
    }}

    /* Header e Slogan Justificado à Direita */
    .header-box {{ text-align: right; padding-right: 10px; }}
    .main-title {{ color: white; font-size: 38px; font-weight: 900; line-height: 1; margin: 0; }}
    .sub-title {{ color: #00bcd4; font-size: 16px; font-weight: bold; margin: 0; letter-spacing: 2px; }}
    .slogan {{ color: rgba(255,255,255,0.6); font-size: 12px; font-style: italic; margin-top: 5px; letter-spacing: 1px; }}

    /* Estilização de Labels */
    .config-label {{ color: #00bcd4 !important; font-weight: 800; font-size: 16px; }}
    .instruction-text {{ color: #FFFFFF !important; font-size: 12px; opacity: 0.85; }}
    </style>
""", unsafe_allow_html=True)

if 'logado' not in st.session_state: st.session_state.logado = False
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 100.0
if 'lucro_acumulado' not in st.session_state: st.session_state.lucro_acumulado = 42.50

if not st.session_state.logado:
    # TELA DE LOGIN AXIO / CROW TECH
    _, col2, _ = st.columns([1, 1, 1])
    with col2:
        st.markdown(f'<div style="text-align:center; margin-top:100px;"><img src="data:image/png;base64,{logo_base64}" width="160"></div>', unsafe_allow_html=True)
        with st.form("login"):
            u = st.text_input("USUÁRIO")
            p = st.text_input("SENHA", type="password")
            if st.form_submit_button("VALIDAR ACESSO ELITE"):
                if u == "admin" and p == "crow123":
                    st.session_state.logado = True
                    st.rerun()
else:
    # --- CABEÇALHO REVISADO ---
    c1, c2 = st.columns([1, 3])
    with c1: 
        st.image(f"data:image/png;base64,{logo_base64}", width=110)
    with c2:
        st.markdown(f"""
            <div class="header-box">
                <p class="main-title">CROW TECH</p>
                <p class="sub-title">PORTAL ELITE</p>
                <p class="slogan">Inteligência em cada movimento</p>
            </div>
        """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📊 DASHBOARD", "⚙️ CONFIGURAÇÃO DO SCRIPT", "🔐 CONEXÃO API"])

    with tab1:
        # Métricas Principais
        col_a, col_b, col_c = st.columns([1, 1, 2])
        with col_a:
            st.markdown('<div class="product-card"><small style="color:rgba(255,255,255,0.5)">BANCA TOTAL (USDT)</small><br><span style="font-size:26px; font-weight:bold;">$ 10.250,00</span></div>', unsafe_allow_html=True)
        with col_b:
            st.markdown(f'<div class="product-card"><small style="color:rgba(255,255,255,0.5)">LUCRO LÍQUIDO</small><br><span style="color:#00ff88; font-size:26px; font-weight:bold;">+ $ {st.session_state.lucro_acumulado}</span></div>', unsafe_allow_html=True)
        with col_c:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            pct = min(st.session_state.lucro_acumulado / st.session_state.meta_diaria, 1.0)
            st.markdown(f"<span class='meta-label'>Meta Diária: $ {st.session_state.meta_diaria}</span>", unsafe_allow_html=True)
            st.progress(pct)
            st.markdown(f"<p style='text-align:right; font-size:12px; color:#00bcd4; font-weight:bold; margin-top:5px;'>{pct*100:.1f}% DO OBJETIVO</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # Gráfico Binance Style
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.components.v1.html("""
            <div class="tradingview-widget-container">
                <div id="tradingview_crow"></div>
                <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
                <script type="text/javascript">
                new TradingView.widget({
                  "width": "100%", "height": 450, "symbol": "BINANCE:BTCUSDT",
                  "interval": "1", "timezone": "Etc/UTC", "theme": "dark", "style": "1", "toolbar_bg": "rgba(0,0,0,0)"
                });
                </script>
            </div>
        """, height=450)
        st.markdown('</div>', unsafe_allow_html=True)

        # Log do Robô
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.code(f"""
>>> [CROW TECH] Conexão Cloud estabelecida.
>>> [STRATEGY] Operando via EMA 20 | RSI Target: {st.session_state.get('rsi_val', 30)}
>>> [ANALYSIS] Tendência identificada. Aguardando ponto de entrada...
>>> [{datetime.now().strftime('%H:%M
