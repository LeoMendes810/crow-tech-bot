import streamlit as st
import base64
import pandas as pd
from datetime import datetime

# 1. Configurações de Marca e Estilo
st.set_page_config(page_title="Crow Tech Elite Portal", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

# --- CSS DEFINITIVO (ZERO BRANCO / SLOGAN ALINHADO) ---
st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 18% !important;
        background-attachment: fixed !important;
        color: white !important;
    }}
    
    /* Remover fundos brancos de botões e campos de texto */
    div.stButton > button, div.stDownloadButton > button {{
        background-color: #00bcd4 !important;
        color: #000000 !important;
        border: none !important;
        font-weight: 900 !important;
    }}

    /* Estilo específico para o botão SAIR (Dark Red) */
    button[kind="secondary"] {{
        background-color: rgba(255, 75, 75, 0.2) !important;
        color: #ff4b4b !important;
        border: 1px solid #ff4b4b !important;
    }}

    /* Cards e Containers Dark */
    .product-card {{
        background: rgba(0, 0, 0, 0.85) !important;
        border: 1px solid rgba(0, 188, 212, 0.3);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    }}

    /* Console Preto Absoluto */
    .stCodeBlock, div[data-testid="stCodeBlock"], div[data-testid="stCodeBlock"] pre {{
        background-color: #000000 !important;
        border: 1px solid #00bcd4 !important;
    }}
    code {{ color: #00ff88 !important; }}

    /* Header e Slogan */
    .header-container {{ text-align: right; }}
    .main-title {{ color: white; font-size: 38px; font-weight: 900; margin-bottom: 0px; line-height: 1; }}
    .sub-title {{ color: #00bcd4; font-size: 18px; font-weight: bold; margin-top: 0px; }}
    .slogan {{ color: rgba(255,255,255,0.6); font-size: 13px; font-style: italic; margin-top: 5px; }}

    /* Meta Legenda Reforçada */
    .meta-text {{
        color: #00bcd4 !important;
        font-weight: 900 !important;
        font-size: 15px;
        text-transform: uppercase;
        text-shadow: 2px 2px 4px #000;
    }}
    </style>
""", unsafe_allow_html=True)

# Lógica de Sessão
if 'logado' not in st.session_state: st.session_state.logado = False
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 100.0
if 'lucro_total' not in st.session_state: st.session_state.lucro_total = 42.50

if not st.session_state.logado:
    # Login Central (Ajustado)
    _, col_login, _ = st.columns([1, 1, 1])
    with col_login:
        st.markdown(f'<div style="text-align:center; margin-top:100px;"><img src="data:image/png;base64,{logo_base64}" width="150"></div>', unsafe_allow_html=True)
        with st.form("login"):
            u = st.text_input("USUÁRIO")
            p = st.text_input("SENHA", type="password")
            if st.form_submit_button("VALIDAR ACESSO"):
                if u == "admin" and p == "crow123":
                    st.session_state.logado = True
                    st.rerun()
else:
    # --- CABEÇALHO PROFISSIONAL ---
    h_col1, h_col2 = st.columns([1, 3])
    with h_col1:
        st.image(f"data:image/png;base64,{logo_base64}", width=110)
    with h_col2:
        st.markdown(f"""
            <div class="header-container">
                <p class="main-title">CROW TECH</p>
                <p class="sub-title">PORTAL ELITE</p>
                <p class="slogan">Inteligência em cada movimento</p>
            </div>
        """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📊 DASHBOARD", "⚙️ CONFIGURAÇÃO SCRIPT", "🔐 CONEXÃO API"])

    with tab1:
        # Métricas e Meta
        m1, m2, m3 = st.columns([1, 1, 2])
        with m1:
            st.markdown('<div class="product-card"><small>SALDO EM CONTA</small><br><b>$ 10.250,00</b></div>', unsafe_allow_html=True)
        with m2:
            st.markdown(f'<div class="product-card"><small>LUCRO ACUMULADO</small><br><b style="color:#00ff88;">+ $ {st.session_state.lucro_total}</b></div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            pct = min(st.session_state.lucro_total / st.session_state.meta_diaria, 1.0)
            st.markdown(f"<span class='meta-text'>Meta Diária ($ {st.session_state.meta_diaria})</span>", unsafe_allow_html=True)
            st.progress(pct)
            st.markdown(f"<p style='text-align:right; font-size:12px;'>{pct*100:.1f}% da meta atingida</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # Monitoramento Binance Real
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.components.v1.html("""
            <div style="height:400px;">
                <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
                <script type="text/javascript">
                new TradingView.widget({
                  "width": "100%", "height": 400, "symbol": "BINANCE:BTCUSDT",
                  "interval": "1", "theme": "dark", "style": "1", "toolbar_bg": "rgba(0,0,0,0)"
                });
                </script>
            </div>
        """, height=400)
        st.markdown('</div>', unsafe_allow_html=True)

        # Console Log (CORREÇÃO DE FUNDO E ERRO DE SINTAXE)
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.code(f"""
>>> [SYS] Crow Tech Engine v.C18.9.1.5 Ativa
>>> [STATUS] Analisando Médias (EMA 20 Nativa)
>>> [LOG] {datetime.now().strftime('%H:%M:%S')} - Escaneando sinais de entrada...
>>> [INFO] Aguardando confirmação do gatilho RSI.
        """, language="bash")
        
        c_btn1, c_btn2 = st.columns([4, 1])
        with c_btn1: st.button("🚀 INICIAR OPERAÇÕES", use_container_width=True)
        with c_btn2: 
            if st.button("SAIR", use_container_width=True, kind="secondary"):
                st.session_state.logado = False
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("### 🛠️ Parâmetros da Inteligência")
        
        ca, cb = st.columns(2)
        with ca:
            st.markdown("<b style='color:#00bcd4;'>Gatilho RSI</b>", unsafe_allow_html=True)
            st.markdown("<small>Define o nível de força para entrada em operações de compra.</small>", unsafe_allow_html=True)
            st.slider("RSI", 10, 50, 30, label_visibility="collapsed")
            
            st.markdown("<br><b style='color:#00bcd4;'>Stop Loss (%)</b>", unsafe_allow_html=True)
            st.markdown("<small>Limite de segurança por operação.</small>", unsafe_allow_html=True)
            st.number_input("SL", 0.5, 5.0, 1.5, label_visibility="collapsed")

        with cb:
            st.markdown("<b style='color:#00bcd4;'>Meta de Lucro do Dia ($)</b>", unsafe_allow_html=True)
            st.markdown("<small>Ao atingir este lucro total, o bot para de operar até o dia seguinte.</small>", unsafe_allow_html=True)
            st.session_state.meta_diaria = st.number_input("Meta", 10.0, 5000.0, float(st.session_state.meta_diaria), label_visibility="collapsed")

            st.markdown("<br><b style='color:#00bcd4;'>Filtro de Tendência (EMA)</b>", unsafe_allow_html=True)
            st.markdown("<small>Configuração fixa do núcleo: Média Exponencial 20.</small>", unsafe_allow_html=True)
            st.text_input("EMA", value="EMA 20 (NATIVA DO SCRIPT)", disabled=True, label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("### 🔐 Integração com a Carteira")
        st.info("Insira suas chaves para que o Portal Elite execute as ordens diretamente na sua conta.")
        st.text_input("API KEY BINANCE", type="password")
        st.text_input("SECRET KEY BINANCE", type="password")
        st.button("CONECTAR E VALIDAR")
        st.markdown('</div>', unsafe_allow_html=True)
