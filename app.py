import streamlit as st
import base64
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# 1. Setup de Marca
st.set_page_config(page_title="Crow Tech Elite Portal", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

# --- CSS PRECISÃO CIRÚRGICA (FIM DOS FUNDOS BRANCOS) ---
st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 20% !important;
        background-attachment: fixed !important;
        color: white !important;
    }}
    
    /* Cards e Containers */
    .product-card {{
        background: rgba(0, 0, 0, 0.7) !important;
        border: 1px solid rgba(0, 188, 212, 0.3);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    }}

    /* REMOÇÃO TOTAL DE FUNDO BRANCO EM BOTÕES E CAMPOS */
    div.stButton > button {{
        background-color: #00bcd4 !important;
        color: #000000 !important;
        border: none !important;
        font-weight: bold !important;
    }}
    
    /* Logout/Sair específico */
    .stButton button[kind="secondary"] {{
        background-color: rgba(255, 75, 75, 0.8) !important;
        color: white !important;
    }}

    /* CONSOLE PRETO ABSOLUTO */
    .stCodeBlock, div[data-testid="stCodeBlock"], div[data-testid="stCodeBlock"] > pre {{
        background-color: #000000 !important;
        border: 1px solid #00bcd4 !important;
    }}
    code {{ color: #00ff88 !important; background-color: transparent !important; }}

    /* LEGENDA DA META REFORÇADA */
    .meta-label {{
        color: #00bcd4 !important;
        font-weight: 900 !important;
        text-shadow: 1px 1px 2px #000;
        font-size: 13px;
        text-transform: uppercase;
    }}

    /* AJUSTE TÍTULO E SLOGAN */
    .header-box {{ text-align: right; margin-top: -20px; }}
    .main-title {{ color: white; font-size: 32px; font-weight: 900; margin-bottom: 0px; }}
    .sub-title {{ color: #00bcd4; font-size: 14px; font-weight: bold; margin-top: -10px; }}
    .slogan {{ color: rgba(255,255,255,0.4); font-size: 11px; font-style: italic; }}

    /* Labels de Configuração */
    .config-label {{ color: #00bcd4 !important; font-weight: bold; font-size: 16px; }}
    .instruction-text {{ color: #FFFFFF !important; font-size: 12px; opacity: 0.9; }}
    </style>
""", unsafe_allow_html=True)

if 'logado' not in st.session_state: st.session_state.logado = False
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 100.0
if 'lucro_acumulado' not in st.session_state: st.session_state.lucro_acumulado = 42.50

if not st.session_state.logado:
    # Login Centralizado
    _, col2, _ = st.columns([1, 1, 1])
    with col2:
        st.markdown(f'<div style="text-align:center; margin-top:100px;"><img src="data:image/png;base64,{logo_base64}" width="150"></div>', unsafe_allow_html=True)
        with st.form("login"):
            u = st.text_input("USUÁRIO")
            p = st.text_input("SENHA", type="password")
            if st.form_submit_button("LOGIN ELITE"):
                if u == "admin" and p == "crow123":
                    st.session_state.logado = True
                    st.rerun()
else:
    # --- HEADER DINÂMICO ---
    c1, c2 = st.columns([1, 3])
    with c1: 
        st.image(f"data:image/png;base64,{logo_base64}", width=100)
    with c2:
        st.markdown(f"""
            <div class="header-box">
                <p class="main-title">CROW TECH</p>
                <p class="sub-title">PORTAL ELITE</p>
                <p class="slogan">Seu estilo em jogo</p>
            </div>
        """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📊 DASHBOARD", "⚙️ CONFIGURAÇÃO SCRIPT", "🔐 CONEXÃO API"])

    with tab1:
        # Top Cards
        col_a, col_b, col_c = st.columns([1, 1, 2])
        with col_a:
            st.markdown('<div class="product-card"><small>BANCA TOTAL (USDT)</small><br><span style="font-size:24px; font-weight:bold; color:white;">$ 10.250,00</span></div>', unsafe_allow_html=True)
        with col_b:
            st.markdown(f'<div class="product-card"><small>LUCRO REALIZADO</small><br><span style="color:#00ff88; font-size:24px; font-weight:bold;">+ $ {st.session_state.lucro_acumulado}</span></div>', unsafe_allow_html=True)
        with col_c:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            pct = min(st.session_state.lucro_acumulado / st.session_state.meta_diaria, 1.0)
            st.markdown(f"<span class='meta-label'>Meta Diária: $ {st.session_state.meta_diaria}</span>", unsafe_allow_html=True)
            st.progress(pct)
            st.markdown(f"<p style='text-align:right; font-size:12px; color:#00bcd4; font-weight:bold;'>{pct*100:.1f}% CONCLUÍDO</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # Live Chat Binance (TradingView)
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

        # Console Log
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.code(f"""
>>> [SISTEMA] Conectado ao Núcleo Crow Tech...
>>> [ESTRATÉGIA] EMA 20 Ativa | RSI: {st.session_state.get('rsi_val', 30)}
>>> [ANALYSIS] Aguardando cruzamento de confirmação...
>>> [{datetime.now().strftime('%H:%M:%S')}] Operação em modo automático.
        """, language="bash")
        
        c_btn1, c_btn2 = st.columns([4, 1])
        with c_btn1: st.button("🚀 INICIAR OPERAÇÕES", use_container_width=True)
        with c_btn2: 
            if st.button("SAIR", use_container_width=True):
                st.session_state.logado = False
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("### 🛠️ Parâmetros do Algoritmo")
        
        ca, cb = st.columns(2)
        with ca:
            st.markdown('<p class="config-label">Gatilho RSI</p>', unsafe_allow_html=True)
            st.markdown('<p class="instruction-text">Define o ponto de entrada. O robô buscará oportunidades abaixo deste nível.</p>', unsafe_allow_html=True)
            st.session_state.rsi_val = st.slider("RSI", 10, 50, 30, label_visibility="collapsed")
            
            st.markdown('<br><p class="config-label">Proteção de Capital (Stop Loss %)</p>', unsafe_allow_html=True)
            st.markdown('<p class="instruction-text">Percentual de segurança para encerramento forçado.</p>', unsafe_allow_html=True)
            st.number_input("SL", 0.5, 5.0, 1.5, label_visibility="collapsed")

        with cb:
            st.markdown('<p class="config-label">Objetivo de Lucro Diário ($)</p>', unsafe_allow_html=True)
            st.markdown('<p class="instruction-text">Valor total a ser alcançado no dia antes do desligamento automático.</p>', unsafe_allow_html=True)
            st.session_state.meta_diaria = st.number_input("Meta $", 10.0, 5000.0, float(st.session_state.meta_diaria), label_visibility="collapsed")

            st.markdown('<br><p class="config-label">Média Móvel (EMA)</p>', unsafe_allow_html=True)
            st.markdown('<p class="instruction-text">Referência fixa do script: EMA 20 (Tendência de Curto/Médio Prazo).</p>', unsafe_allow_html=True)
            st.text_input("EMA", value="EMA 20 (PADRÃO)", disabled=True, label_visibility="collapsed")
        
        st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("### 🔐 Credenciais de API")
        st.info("Insira suas chaves para que o sistema possa executar ordens em sua conta.")
        st.text_input("API KEY", type="password")
        st.text_input("SECRET KEY", type="password")
        st.button("CONECTAR CONTA")
        st.markdown('</div>', unsafe_allow_html=True)
