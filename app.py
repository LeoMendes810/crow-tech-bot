import streamlit as st
import base64
from datetime import datetime

# 1. SETUP DE MARCA
st.set_page_config(page_title="Crow Tech Elite Portal", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

# --- CSS DEFINITIVO (RESTAURADO E ESTABILIZADO) ---
st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 20% !important;
        background-attachment: fixed !important;
        color: white !important;
    }}

    /* LOGIN CARD ORIGINAL */
    .login-card {{
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        margin-top: 50px;
    }}

    /* CARDS DO DASHBOARD */
    .product-card {{
        background: rgba(0, 0, 0, 0.8) !important;
        border: 1px solid rgba(0, 188, 212, 0.3);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 10px;
    }}

    /* CONSOLE PRETO ABSOLUTO (SEM FUNDO BRANCO) */
    .stCodeBlock, div[data-testid="stCodeBlock"], div[data-testid="stCodeBlock"] pre {{
        background-color: #000000 !important;
        border: 1px solid #00bcd4 !important;
    }}
    code {{ color: #00ff88 !important; background-color: transparent !important; }}

    /* CABEÇALHO E SLOGAN JUSTIFICADO À DIREITA */
    .header-box {{ text-align: right; }}
    .main-title {{ color: white; font-size: 36px; font-weight: 900; line-height: 1; margin: 0; }}
    .sub-title {{ color: #00bcd4; font-size: 16px; font-weight: bold; margin: 0; }}
    .slogan {{ color: rgba(255,255,255,0.6); font-size: 13px; font-style: italic; margin-top: 5px; }}

    /* META E BOTAO */
    .meta-text {{ color: #00bcd4; font-weight: 900; text-transform: uppercase; font-size: 14px; }}
    div.stButton > button {{
        background-color: #00bcd4 !important;
        color: black !important;
        font-weight: bold !important;
        border: none !important;
        width: 100%;
    }}
    
    /* INPUTS DARK */
    div[data-testid="stTextInput"] input, div[data-testid="stNumberInput"] input {{
        background-color: rgba(0, 0, 0, 0.6) !important;
        color: white !important;
        border: 1px solid rgba(0, 188, 212, 0.5) !important;
    }}
    </style>
""", unsafe_allow_html=True)

if 'logado' not in st.session_state: st.session_state.logado = False
if 'meta_val' not in st.session_state: st.session_state.meta_val = 500.0

# --- ESTRUTURA DE NAVEGAÇÃO ---
if not st.session_state.logado:
    # TELA DE LOGIN (CARD DE VIDRO)
    _, col_log, _ = st.columns([1, 1.2, 1])
    with col_log:
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        st.image(f"data:image/png;base64,{logo_base64}", width=130)
        st.markdown("<h2 style='margin-bottom:0;'>CROW TECH</h2><p style='color:#00bcd4; margin-top:0;'>PORTAL ELITE</p>", unsafe_allow_html=True)
        u = st.text_input("USUÁRIO", placeholder="Username")
        p = st.text_input("SENHA", type="password", placeholder="Password")
        if st.button("ACESSAR"):
            if u == "admin" and p == "crow123":
                st.session_state.logado = True
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
else:
    # --- HEADER ---
    c_logo, c_text = st.columns([1, 3])
    with c_logo: st.image(f"data:image/png;base64,{logo_base64}", width=100)
    with c_text:
        st.markdown(f"""
            <div class="header-box">
                <p class="main-title">CROW TECH</p>
                <p class="sub-title">PORTAL ELITE</p>
                <p class="slogan">Inteligência em cada movimento</p>
            </div>
        """, unsafe_allow_html=True)

    tab_dash, tab_conf, tab_api = st.tabs(["📊 DASHBOARD", "⚙️ CONFIGURAÇÃO", "🔐 API"])

    with tab_dash:
        # Métricas
        m1, m2, m3 = st.columns([1, 1, 2])
        with m1: st.markdown('<div class="product-card"><small>BANCA USDT</small><br><span style="font-size:22px; font-weight:bold;">$ 10.250,00</span></div>', unsafe_allow_html=True)
        with m2: st.markdown('<div class="product-card"><small>LUCRO HOJE</small><br><span style="font-size:22px; font-weight:bold; color:#00ff88;">+ $ 425,10</span></div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            st.markdown(f"<span class='meta-text'>Meta Diária: $ {st.session_state.meta_val}</span>", unsafe_allow_html=True)
            st.progress(0.85)
            st.markdown("<p style='text-align:right; font-size:11px; color:#00bcd4; margin:0;'>85% CONCLUÍDO</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # Gráfico e Console
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.components.v1.html("""
            <div style="height:400px;"><script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <script type="text/javascript">new TradingView.widget({"width": "100%", "height": 400, "symbol": "BINANCE:BTCUSDT", "theme": "dark", "style": "1"});</script></div>
        """, height=400)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.code(f">>> [SISTEMA] Crow Tech Online\n>>> [ESTRATEGIA] EMA 20 Ativa\n>>> [{datetime.now().strftime('%H:%M:%S')}] Escaneando sinais...", language="bash")
        c_b1, c_b2 = st.columns([4, 1])
        with c_b1: st.button("🚀 INICIAR ENGINE")
        with c_b2: 
            if st.button("SAIR"):
                st.session_state.logado = False
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with tab_conf:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("### 🛠️ Ajuste de Parâmetros")
        st.slider("Gatilho RSI", 10, 50, 30)
        st.number_input("Stop Loss (%)", value=1.5)
        st.session_state.meta_val = st.number_input("Meta de Lucro Diário ($)", value=st.session_state.meta_val)
        st.text_input("Configuração Nativa", value="EMA 20", disabled=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab_api:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("### 🔐 Conexão API")
        st.text_input("API KEY BINANCE", type="password")
        st.text_input("SECRET KEY", type="password")
        st.button("VINCULAR CONTA")
        st.markdown('</div>', unsafe_allow_html=True)
