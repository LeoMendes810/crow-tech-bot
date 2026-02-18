import streamlit as st
import base64
from datetime import datetime

# ======================================================
# CONFIGURAÇÃO DA PÁGINA
# ======================================================
st.set_page_config(page_title="Crow Tech Elite", layout="wide")

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
# SESSION STATE (MEMÓRIA DO SISTEMA)
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
st.markdown("""
<style>
header, footer, .stDeployButton, [data-testid="stHeader"] {
    visibility: hidden !important;
}

.stApp {
    background: #0b1016;
}

.card {
    background: rgba(10,15,20,0.85);
    border: 1px solid rgba(0,188,212,0.35);
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0 0 25px rgba(0,188,212,0.2);
}

.stTextInput input {
    background: rgba(255,255,255,0.85) !important;
    color: #000000 !important;
    font-weight: bold;
    border: none !important;
    border-bottom: 2px solid #00bcd4 !important;
}

.stButton > button {
    background: rgba(0,188,212,0.18) !important;
    color: #eaffff !important;
    font-weight: 800 !important;
    width: 100% !important;
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

        st.markdown("""
        <div style="text-align:right; font-size:11px; color:#9adfe6; cursor:pointer;">
            Esqueci a senha
        </div>
        """, unsafe_allow_html=True)

        entrar = st.form_submit_button("ENTRAR")

        st.markdown("""
        <div style="text-align:center; font-size:11px; color:#00bcd4; cursor:pointer; margin-top:12px;">
            Não tem conta? Cadastre-se
        </div>
        """, unsafe_allow_html=True)

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
    col1, col2, col3 = st.columns([1,4,1])

    with col1:
        st.image(f"data:image/png;base64,{logo_base64}", width=60)

    with col2:
        st.markdown(
            "<h2 style='text-align:center;color:white'>CROW TECH <span style='color:#00bcd4'>DASHBOARD</span></h2>",
            unsafe_allow_html=True
        )

    with col3:
        if st.button("SAIR"):
            st.session_state.logado = False
            st.rerun()

    # TABS
    tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "⚙️ Configurações", "🔐 API"])

    # ================= TAB 1 =================
    with tab1:
        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown("<div class='card'>💰 <b>Banca</b><br>$ 10.250</div>", unsafe_allow_html=True)

        with c2:
            st.markdown(
                f"<div class='card'>📈 <b>Lucro Hoje</b><br><span style='color:#00ff88'>+ ${st.session_state.lucro_acumulado}</span></div>",
                unsafe_allow_html=True
            )

        with c3:
            pct = min(st.session_state.lucro_acumulado / st.session_state.meta_diaria, 1.0)
            st.markdown("<div class='card'><b>Meta Diária</b></div>", unsafe_allow_html=True)
            st.progress(pct)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 📟 Log do Robô")
        st.code(f"""
>>> API conectada
>>> Monitorando mercado
>>> {datetime.now().strftime('%H:%M:%S')}
        """, language="bash")
        st.button("🚀 LIGAR ROBÔ")
        st.markdown("</div>", unsafe_allow_html=True)

    # ================= TAB 2 =================
    with tab2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.slider("RSI", 10, 50, 30)
        st.number_input("Meta diária ($)", 10.0, 5000.0, st.session_state.meta_diaria)
        st.markdown("</div>", unsafe_allow_html=True)

    # ================= TAB 3 =================
    with tab3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.text_input("API KEY", type="password")
        st.text_input("SECRET KEY", type="password")
        st.button("TESTAR CONEXÃO")
        st.markdown("</div>", unsafe_allow_html=True)
