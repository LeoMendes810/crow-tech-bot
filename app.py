import streamlit as st
import base64
from datetime import datetime

# ======================================================
# CONFIGURAÇÃO DA PÁGINA
# ======================================================
st.set_page_config(page_title="Crow Tech Elite Portal", layout="wide")

# ======================================================
# FUNÇÕES UTILITÁRIAS
# ======================================================
def get_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

bg_base64 = get_base64("assets/corvo_bg.png")
logo_base64 = get_base64("assets/logo.png")

# ======================================================
# SESSION STATE
# ======================================================
if "logado" not in st.session_state:
    st.session_state.logado = False

if "meta_diaria" not in st.session_state:
    st.session_state.meta_diaria = 100.0

if "lucro_acumulado" not in st.session_state:
    st.session_state.lucro_acumulado = 42.50

# ======================================================
# CSS GLOBAL
# ======================================================
def css_global():
    st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{
        visibility: hidden !important;
    }}

    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center;
        background-size: 30%;
        background-attachment: fixed;
    }}

    .product-card {{
        background: rgba(10,15,20,0.8);
        border: 1px solid rgba(0,188,212,0.25);
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 12px;
    }}

    .config-label {{
        color: #00bcd4;
        font-weight: bold;
        font-size: 14px;
    }}

    .instruction-text {{
        color: white;
        font-size: 12px;
        opacity: 0.8;
    }}

    .stCodeBlock {{
        background-color: #000 !important;
        border: 1px solid #00bcd4 !important;
    }}

    code {{
        color: #00ff88 !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# ======================================================
# LOGIN
# ======================================================
def render_login():
    css_global()

    st.markdown(f"""
    <style>
    [data-testid="stForm"] {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 360px;
        background: rgba(255,255,255,0.12);
        backdrop-filter: blur(25px);
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.6);
    }}

    .stTextInput input {{
        background: rgba(255,255,255,0.75);
        color: black !important;
        font-weight: bold;
        border-bottom: 2px solid #00bcd4;
    }}

    .stButton > button {{
        background: #00bcd4;
        color: black;
        font-weight: 900;
        width: 100%;
        height: 45px;
        margin-top: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

    with st.form("login"):
        st.markdown(
            f"<div style='text-align:center'><img src='data:image/png;base64,{logo_base64}' width='150'></div>",
            unsafe_allow_html=True
        )

        user = st.text_input("USUÁRIO")
        pwd = st.text_input("SENHA", type="password")

        if st.form_submit_button("ACESSAR SISTEMA"):
            if user == "admin" and pwd == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Credenciais inválidas")

# ======================================================
# DASHBOARD
# ======================================================
def render_dashboard():
    css_global()

    # HEADER
    c1, c2, c3 = st.columns([1,4,1])
    with c1:
        st.image(f"data:image/png;base64,{logo_base64}", width=70)
    with c2:
        st.markdown(
            "<h2 style='text-align:center;color:white'>CROW TECH <span style='color:#00bcd4'>PORTAL ELITE</span></h2>",
            unsafe_allow_html=True
        )
    with c3:
        if st.button("SAIR"):
            st.session_state.logado = False
            st.rerun()

    tab1, tab2, tab3 = st.tabs(["📊 DASHBOARD", "⚙️ CONFIGURAÇÕES", "🔐 API"])

    # ================= TAB 1 =================
    with tab1:
        col1, col2, col3 = st.columns([1,1,2])

        with col1:
            st.markdown(
                "<div class='product-card'><small>BANCA</small><br><b>$10.250</b></div>",
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"<div class='product-card'><small>LUCRO HOJE</small><br><span style='color:#00ff88'>+ ${st.session_state.lucro_acumulado}</span></div>",
                unsafe_allow_html=True
            )

        with col3:
            pct = min(st.session_state.lucro_acumulado / st.session_state.meta_diaria, 1.0)
            st.markdown("<div class='product-card'>", unsafe_allow_html=True)
            st.markdown(f"<small>META DIÁRIA (${st.session_state.meta_diaria})</small>", unsafe_allow_html=True)
            st.progress(pct)
            st.markdown(f"<small>{pct*100:.1f}% concluído</small>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='product-card'>", unsafe_allow_html=True)
        st.markdown("<small>LOG DE EXECUÇÃO</small>", unsafe_allow_html=True)
        st.code(f"""
>>> API conectada
>>> Analisando EMA 9 / 21
>>> RSI aguardando nível configurado
>>> [{datetime.now().strftime('%H:%M:%S')}] Monitorando mercado
        """, language="bash")
        st.button("🚀 LIGAR ROBÔ", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ================= TAB 2 =================
    with tab2:
        st.markdown("<div class='product-card'>", unsafe_allow_html=True)

        st.markdown("<p class='config-label'>RSI</p>", unsafe_allow_html=True)
        st.session_state.rsi_val = st.slider("RSI", 10, 50, 30)

        st.markdown("<p class='config-label'>Meta Diária ($)</p>", unsafe_allow_html=True)
        st.session_state.meta_diaria = st.number_input(
            "Meta", 10.0, 5000.0, st.session_state.meta_diaria
        )

        st.markdown("</div>", unsafe_allow_html=True)

    # ================= TAB 3 =================
    with tab3:
        st.markdown("<div class='product-card'>", unsafe_allow_html=True)
        st.text_input("API KEY", type="password")
        st.text_input("SECRET KEY", type="password")
        st.button("TESTAR CONEXÃO")
        st.markdown("</div>", unsafe_allow_html=True)

# ======================================================
# RENDER
# ======================================================
if st.session_state.logado:
    render_dashboard()
else:
    render_login()
