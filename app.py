import streamlit as st
import base64
from datetime import datetime

# 1. Configuração da página (Mantida do seu Login.txt)
st.set_page_config(page_title="Crow Tech Elite", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

# --- ESTADO DE LOGIN ---
if 'logado' not in st.session_state:
    st.session_state.logado = False
if 'meta_diaria' not in st.session_state:
    st.session_state.meta_diaria = 100.0

# --- TELA DE LOGIN (INTEGRAÇÃO FIEL DO SEU LOGIN.TXT) ---
if not st.session_state.logado:
    st.markdown(f"""
        <style>
        header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
        .stApp {{
            background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
            background-size: 50% !important;
            background-attachment: fixed !important;
        }}
        [data-testid="stForm"] {{
            position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
            width: 360px; background: rgba(255, 255, 255, 0.95) !important;
            border-radius: 20px; padding: 30px !important; box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        }}
        .stTextInput input {{ background-color: transparent !important; color: black !important; border: none !important; border-bottom: 1px solid rgba(0,0,0,0.2) !important; }}
        .link-text {{ color: #008b8b; font-size: 11px; cursor: pointer; font-weight: bold; }}
        div.stButton > button {{ background-color: #000000 !important; color: white !important; border-radius: 10px !important; width: 100%; }}
        </style>
    """, unsafe_allow_html=True)

    with st.form("login_form"):
        st.markdown(f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{logo_base64}" width="160">
                <p style="color: #000; font-size: 9px; letter-spacing: 2px; font-weight: 900; margin-top: -10px;">CROW TECH ELITE</p>
            </div>
        """, unsafe_allow_html=True)
        
        usuario = st.text_input("USUÁRIO", placeholder="Username")
        senha = st.text_input("SENHA", type="password", placeholder="Password")
        st.markdown('<div style="display: flex; justify-content: flex-end; margin-top: -15px;"><span class="link-text">Esqueceu a senha?</span></div>', unsafe_allow_html=True)
        
        if st.form_submit_button("ACESSAR SISTEMA"):
            if usuario == "admin" and senha == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Acesso negado")

# --- DASHBOARD (INTEGRAÇÃO FIEL DO SEU DASHBOARD.TXT) ---
else:
    st.markdown(f"""
        <style>
        header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
        .stApp {{
            background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
            background-size: 20% !important;
        }}
        .product-card {{ background: rgba(10, 15, 20, 0.8) !important; border: 1px solid rgba(0, 188, 212, 0.3); border-radius: 12px; padding: 20px; margin-bottom: 15px; color: white; }}
        .header-box {{ text-align: right; }}
        .main-title {{ color: white; font-size: 32px; font-weight: 900; margin: 0; }}
        .sub-title {{ color: #00bcd4; font-size: 14px; font-weight: bold; margin: 0; }}
        .slogan {{ color: rgba(255,255,255,0.4); font-size: 11px; font-style: italic; }}
        /* Ajuste para remover fundo branco do console e inputs no dashboard */
        .stCodeBlock, div[data-testid="stCodeBlock"] pre {{ background-color: #000 !important; border: 1px solid #00bcd4; }}
        div[data-testid="stNumberInput"] input, div[data-testid="stTextInput"] input {{ background-color: #000 !important; color: white !important; }}
        </style>
    """, unsafe_allow_html=True)

    # Header Crow Tech
    c1, c2 = st.columns([1, 3])
    with c1: st.image(f"data:image/png;base64,{logo_base64}", width=100)
    with c2:
        st.markdown(f"""<div class="header-box">
            <p class="main-title">CROW TECH</p>
            <p class="sub-title">PORTAL ELITE</p>
            <p class="slogan">Inteligência em cada movimento</p>
        </div>""", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📊 DASHBOARD", "⚙️ CONFIGURAÇÃO", "🔐 API"])

    with tab1:
        col_a, col_b, col_c = st.columns([1, 1, 2])
        col_a.markdown('<div class="product-card"><small>BANCA TOTAL</small><br><b>$ 10.250,00</b></div>', unsafe_allow_html=True)
        col_b.markdown('<div class="product-card"><small>LUCRO HOJE</small><br><b style="color:#00ff88;">+ $ 42,50</b></div>', unsafe_allow_html=True)
        with col_c:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            st.markdown(f"<small style='color:#00bcd4; font-weight:bold;'>META DIÁRIA: $ {st.session_state.meta_diaria}</small>", unsafe_allow_html=True)
            st.progress(0.42)
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.components.v1.html("""<div style="height:400px;"><script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <script type="text/javascript">new TradingView.widget({"width": "100%", "height": 400, "symbol": "BINANCE:BTCUSDT", "theme": "dark", "style": "1"});</script></div>""", height=400)
        st.markdown('</div>', unsafe_allow_html=True)

        st.code(f">>> [SISTEMA] Crow Tech Online\n>>> [ESTRATÉGIA] EMA 20 Ativa\n>>> [{datetime.now().strftime('%H:%M:%S')}] Monitorando sinais...")
        
        if st.button("SAIR"):
            st.session_state.logado = False
            st.rerun()

    with tab2:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.session_state.meta_diaria = st.number_input("Meta de Lucro Diário ($)", value=float(st.session_state.meta_diaria))
        st.text_input("Configuração", value="EMA 20 (Nativa)", disabled=True)
        st.markdown('</div>', unsafe_allow_html=True)
