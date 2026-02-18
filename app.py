import streamlit as st
import base64
from datetime import datetime

# 1. SETUP DE MARCA E CONFIGURAÇÃO DE PÁGINA
st.set_page_config(page_title="Crow Tech Elite Portal", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

# --- CSS INTEGRADO: FUSÃO LOGIN (VIDRO) + DASHBOARD (DARK) ---
st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 25% !important;
        background-attachment: fixed !important;
        color: white !important;
    }}

    /* ESTILO DO LOGIN (VIDRO) */
    [data-testid="stForm"] {{
        background: rgba(255, 255, 255, 0.12) !important;
        backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 20px;
        padding: 30px !important;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
    }}

    /* INPUTS DO LOGIN (TEXTO VISÍVEL) */
    .stTextInput input {{
        background-color: rgba(255, 255, 255, 0.8) !important;
        color: #000000 !important;
        font-weight: bold !important;
        border-bottom: 2px solid #00bcd4 !important;
    }}
    
    label {{ color: white !important; font-weight: bold !important; }}

    /* CARDS DO DASHBOARD */
    .product-card {{
        background: rgba(10, 15, 20, 0.85) !important;
        border: 1px solid rgba(0, 188, 212, 0.2);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 10px;
    }}

    /* CONSOLE PRETO ABSOLUTO */
    .stCodeBlock, div[data-testid="stCodeBlock"], div[data-testid="stCodeBlock"] pre {{
        background-color: #000000 !important;
        border: 1px solid #00bcd4 !important;
    }}
    code {{ color: #00ff88 !important; }}

    /* BOTÕES CROW TECH */
    div.stButton > button {{
        background-color: #00bcd4 !important;
        color: black !important;
        font-weight: 800 !important;
        border: none !important;
        width: 100%;
        text-transform: uppercase;
    }}
    
    .header-right {{ text-align: right; }}
    .slogan-text {{ color: rgba(255,255,255,0.6); font-size: 14px; font-style: italic; }}
    </style>
""", unsafe_allow_html=True)

# Gerenciamento de Estado
if 'logado' not in st.session_state: st.session_state.logado = False
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 500.0
if 'lucro_hoje' not in st.session_state: st.session_state.lucro_hoje = 425.10

# --- LÓGICA DE NAVEGAÇÃO ---
if not st.session_state.logado:
    # Interface de Login (Baseada no Login.txt)
    _, col_cent, _ = st.columns([1, 1, 1])
    with col_cent:
        st.markdown(f'<div style="text-align: center; margin-bottom: 10px; margin-top: 50px;"><img src="data:image/png;base64,{logo_base64}" width="160"></div>', unsafe_allow_html=True)
        with st.form("login_crow"):
            st.markdown("<p style='text-align:center; color:white; font-size:10px; letter-spacing:2px;'>CROW TECH ELITE</p>", unsafe_allow_html=True)
            u = st.text_input("USUÁRIO", placeholder="Username")
            p = st.text_input("SENHA", type="password", placeholder="Password")
            if st.form_submit_button("ACESSAR SISTEMA"):
                if u == "admin" and p == "crow123":
                    st.session_state.logado = True
                    st.rerun()
                else:
                    st.error("Credenciais incorretas")

else:
    # --- DASHBOARD ELITE (Baseado no Dashboard.txt) ---
    c1, c2 = st.columns([1, 3])
    with c1: st.image(f"data:image/png;base64,{logo_base64}", width=100)
    with c2:
        st.markdown("""
            <div class="header-right">
                <h1 style="margin:0; color:white;">CROW TECH <span style="color:#00bcd4;">PORTAL ELITE</span></h1>
                <p class="slogan-text">Inteligência em cada movimento</p>
            </div>
        """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📊 DASHBOARD", "⚙️ CONFIGURAÇÃO", "🔐 API CONNECTION"])

    with tab1:
        col_m1, col_m2, col_m3 = st.columns([1, 1, 2])
        with col_m1:
            st.markdown('<div class="product-card"><small>BANCA ATUAL (USDT)</small><br><span style="font-size:22px; font-weight:bold;">$ 10.250,00</span></div>', unsafe_allow_html=True)
        with col_m2:
            st.markdown(f'<div class="product-card"><small>LUCRO HOJE</small><br><span style="color:#00ff88; font-size:22px; font-weight:bold;">+ $ {st.session_state.lucro_hoje}</span></div>', unsafe_allow_html=True)
        with col_m3:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            pct = min(st.session_state.lucro_hoje / st.session_state.meta_diaria, 1.0)
            st.markdown(f"<small>PROGRESSO DA META DIÁRIA ($ {st.session_state.meta_diaria})</small>", unsafe_allow_html=True)
            st.progress(pct)
            st.markdown(f"<p style='text-align:right; font-size:11px; color:#00bcd4; margin:0;'>{pct*100:.1f}% CONCLUÍDO</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # Gráfico e Console
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.components.v1.html("""
            <div style="height:350px;"><script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <script type="text/javascript">new TradingView.widget({"width": "100%", "height": 350, "symbol": "BINANCE:BTCUSDT", "theme": "dark", "style": "1"});</script></div>
        """, height=350)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.code(f">>> [OK] API Conectada com sucesso.\n>>> [ESTRATÉGIA] EMA 20 Ativa\n>>> [{datetime.now().strftime('%H:%M:%S')}] Monitorando sinais...", language="bash")
        
        c_exec, c_out = st.columns([4, 1])
        with c_exec:
            if st.button("🚀 INICIAR ENGINE"): st.toast("Algoritmo Crow Tech iniciado!")
        with c_out:
            if st.button("SAIR"):
                st.session_state.logado = False
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("### 🛠️ Ajuste Fino do Algoritmo")
        st.slider("Gatilho RSI", 10, 50, 30)
        st.number_input("Stop Loss (%)", value=1.50)
        st.session_state.meta_diaria = st.number_input("Meta de Lucro Diário ($)", value=float(st.session_state.meta_diaria))
        st.text_input("Média Móvel de Referência", value="EMA 20", disabled=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("### 🔐 Credenciais de Operação")
        st.text_input("API KEY BINANCE", type="password")
        st.text_input("SECRET KEY BINANCE", type="password")
        st.button("VINCULAR E TESTAR CONEXÃO")
        st.markdown('</div>', unsafe_allow_html=True)
