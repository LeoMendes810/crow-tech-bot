import streamlit as st
import base64

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
# SESSION STATE
# ======================================================
if "logado" not in st.session_state:
    st.session_state.logado = False

# ======================================================
# CSS – VISUAL DA TELA DE LOGIN
# ======================================================
st.markdown(f"""
<style>
header, footer, .stDeployButton, [data-testid="stHeader"] {{
    visibility: hidden !important;
}}

.stApp {{
    background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center;
    background-size: 45%;
    background-attachment: fixed;
}}

[data-testid="stForm"] {{
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
}}

.stTextInput input {{
    background: rgba(255,255,255,0.85) !important;
    color: #000000 !important;
    font-weight: bold;
    border: none !important;
    border-bottom: 2px solid #00bcd4 !important;
    border-radius: 6px;
}}

.stButton > button {{
    background: rgba(0,188,212,0.18) !important;
    color: #eaffff !important;
    font-weight: 800 !important;
    width: 100% !important;
    height: 46px;
    border: 1px solid rgba(0,188,212,0.6) !important;
    border-radius: 10px !important;
    box-shadow: 0 0 15px rgba(0,188,212,0.35);
    backdrop-filter: blur(10px);
    transition: all 0.25s ease;
}

.stButton > button:hover {{
    background: rgba(0,188,212,0.35) !important;
    box-shadow: 0 0 22px rgba(0,188,212,0.7);
    transform: translateY(-1px);
}}
</style>
""", unsafe_allow_html=True)

# ======================================================
# LOGIN
# ======================================================
if not st.session_state.logado:

    with st.form("login"):
        st.markdown(f"""
        <div style="text-align:center; margin-bottom:14px;">
            <img src="data:image/png;base64,{logo_base64}" width="150">
            <p style="
                color:#9adfe6;
                font-size:10px;
                letter-spacing:2px;
                font-weight:900;
                margin-top:-6px;
            ">
                CROW TECH ELITE
            </p>
        </div>
        """, unsafe_allow_html=True)

        usuario = st.text_input("Usuário", placeholder="Digite seu usuário")
        senha = st.text_input("Senha", type="password", placeholder="Digite sua senha")

        # ESQUECI A SENHA
        st.markdown("""
        <div style="display:flex; justify-content:flex-end; margin-top:-12px;">
            <span style="
                color:#9adfe6;
                font-size:11px;
                cursor:pointer;
                text-decoration:underline;
            ">
                Esqueci a senha
            </span>
        </div>
        """, unsafe_allow_html=True)

        entrar = st.form_submit_button("ENTRAR")

        # CADASTRE-SE
        st.markdown("""
        <div style="text-align:center; margin-top:18px;">
            <span style="color:rgba(255,255,255,0.6); font-size:11px;">
                Não tem conta?
            </span>
            <span style="
                color:#00bcd4;
                font-size:11px;
                font-weight:700;
                cursor:pointer;
                margin-left:4px;
            ">
                Cadastre-se
            </span>
        </div>
        """, unsafe_allow_html=True)

        if entrar:
            if usuario == "admin" and senha == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Usuário ou senha inválidos")

else:
    st.success("Login realizado com sucesso")
