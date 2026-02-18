import streamlit as st
import base64
from datetime import datetime

# ======================================================
# CONFIGURAÇÃO DA PÁGINA
# ======================================================
st.set_page_config(page_title="Crow Tech Elite Portal", layout="wide")

# ======================================================
# FUNÇÃO PARA CARREGAR IMAGENS
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

if "rsi_val" not in st.session_state:
    st.session_state.rsi_val = 30

# ======================================================
# CSS GLOBAL (SEM f-string)
# ======================================================
st.markdown("""
<style>
header, footer, .stDeployButton, [data-testid="stHeader"] {
    visibility: hidden !important;
}

.stApp {
    background: #0b1016;
}

.product-card {
    background: rgba(10,15,20,0.9);
    border: 1px solid rgba(0,188,212,0.35);
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 12px;
    box-shadow: 0 0 25px rgba(0,188,212,0.18);
}

.config-label {
    color: #00bcd4;
    font-weight: bold;
    font-size: 14px;
}

.instruction-text {
    color: white;
    font-size: 12px;
    opacity: 0.8;
}

.stTextInput input {
    background: rgba(255,255,255,0.85) !important;
    color: #000 !important;
    font-weight: bold;
    border: none !important;
    border-bottom: 2px solid #00bcd4 !important;
}

.stButton > button {
    background: rgba(0,188,212,0.18) !important;
    color: #eaffff !important;
    font-weight: 800 !important;
    height: 46px;
    border: 1px solid rgba(0,188,212,0.6) !important;
    border-radius: 10px !important;
    box-shadow: 0 0 15px rgba(0,188,212,0.35);
}

.stButton > button:hover {
    background: rgba(0,188,212,0.35) !important;
    box-shadow: 0 0 22px rgba(0,188,212,0.7);
}
</style>
""", unsafe_allow_html=True)

# ======================================================
# LOGIN
# ======================================================
if not st.session_state.logado:

    st.markdown("""
    <style>
    [data-testid="stForm"] {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 360px;
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(25px);
        border-radius: 22px;
        padding: 28px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.6);
    }
    </style>
    """, unsafe_allow_html=True)

    with st.form("login"):
        st.markdown(
            f"<div style='text-align:center'><img src='data:image/png;base64,{logo_base64}' width='150'></div>",
            unsafe_allow_html=True
        )

        usuario = st.text_input("Usuário", placeholder="Digite seu usuário")
        senha = st.text_input("Senha", type="password", placeholder="Digite sua senha")

        st.markdown(
            "<div style='text-align:right;font-size:11px;color:#9adfe6;'>Esqueci a senha</div>",
            unsafe_allow_html=True
        )

        entrar = st.form_submit_button("ENTRAR")

        st.markdown(
            "<div style='text-align:center;font-size:11px;color:#00bcd4;margin-top:12px;'>Não tem conta? Cadastre-se</div>",
            unsafe_allow_html=True
        )

        if entrar:
            if usuario == "admin" and senha == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Usuário ou senha inválidos")

# ======================================================
# DASHBOARD
# ======================================================
else:
    # HEADER
    h1, h2, h3 = st.columns([1, 4, 1])

    with h1:
        st.image(f"data:image/png;base64,{logo_base64}", width=60)

    with h2:
        st.markdown(
            "<h2 style='text-align:center;color:white;'>CROW TECH <span style='color:#00bcd4;'>PORTAL ELITE</span></h2>",
            unsafe_allow_html=True
        )

    with h3:
        if st.button("SAIR"):
            st.session_state.logado = False
            st.rerun()

    # TABS
    tab1, tab2, tab3 = st.tabs(
    ["📊 DASHBOARD", "⚙️ CONFIGURAÇÃO SCRIPT", "🔐 API CONNECTION"]
)

# ================= TAB 1 =================
with tab1:
    st.markdown("<div class='product-card'>", unsafe_allow_html=True)
    st.markdown("### 📊 Dashboard")
    st.info("Dashboard ativo. (conteúdo mantido)")

    st.markdown("</div>", unsafe_allow_html=True)

# ================= TAB 2 =================
with tab2:
    st.markdown("<div class='product-card'>", unsafe_allow_html=True)
    st.markdown("## ⚙️ Estratégia do Robô (Spot)")

    st.markdown("### 📈 Filtro de Tendência")
    st.number_input("EMA (períodos)", value=20, disabled=True)

    st.divider()

    st.markdown("### 📉 Timing de Entrada (RSI)")
    c1, c2 = st.columns(2)
    with c1:
        st.number_input("RSI mínimo", value=35, disabled=True)
    with c2:
        st.number_input("RSI máximo", value=50, disabled=True)

    st.divider()

    st.markdown("### 🔊 Confirmação por Volume")
    st.number_input("Volume mínimo (× média)", value=1.10, disabled=True)

    st.divider()

    st.markdown("### 💰 Gestão de Capital")
    st.number_input("Percentual do saldo por trade (%)", value=85, disabled=True)

    st.divider()

    st.markdown("### 🛡️ Proteções da Operação")
    c3, c4 = st.columns(2)
    with c3:
        st.number_input("Break-even (%)", value=0.80, disabled=True)
        st.number_input("Stop máximo (%)", value=-2.5, disabled=True)
    with c4:
        st.number_input("Alvo mínimo (%)", value=1.30, disabled=True)
        st.number_input("Recuo do topo (%)", value=0.30, disabled=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ================= TAB 3 =================
with tab3:
    st.markdown("<div class='product-card'>", unsafe_allow_html=True)
    st.info("Configuração de API será feita aqui.")
    st.markdown("</div>", unsafe_allow_html=True)
