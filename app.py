import streamlit as st
import base64

st.set_page_config(page_title="Crow Tech Elite", layout="wide")

def get_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

bg_base64 = get_base64("assets/corvo_bg.png")
logo_base64 = get_base64("assets/logo.png")

if "logado" not in st.session_state:
    st.session_state.logado = False

# CSS (SEM f-string)
st.markdown("""
<style>
header, footer, .stDeployButton, [data-testid="stHeader"] {
    visibility: hidden !important;
}

.stApp {
    background: #0b1016;
}

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
</style>
""", unsafe_allow_html=True)

# LOGIN
if not st.session_state.logado:
    with st.form("login"):
        st.markdown(
            f"<div style='text-align:center'><img src='data:image/png;base64,{logo_base64}' width='150'></div>",
            unsafe_allow_html=True
        )

        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")

        st.markdown("""
        <div style="text-align:right; font-size:11px; color:#9adfe6; cursor:pointer;">
            Esqueci a senha
        </div>
        """, unsafe_allow_html=True)

        entrar = st.form_submit_button("ENTRAR")

        st.markdown("""
        <div style="text-align:center; font-size:11px; color:#00bcd4; cursor:pointer; margin-top:10px;">
            Cadastre-se
        </div>
        """, unsafe_allow_html=True)

        if entrar:
            if usuario == "admin" and senha == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Usuário ou senha inválidos")
else:
    # ===========================
    # DASHBOARD SIMPLES (TESTE)
    # ===========================
    st.markdown("""
    <style>
    .dashboard-box {
        background: rgba(10,15,20,0.85);
        border: 1px solid rgba(0,188,212,0.4);
        border-radius: 14px;
        padding: 25px;
        box-shadow: 0 0 25px rgba(0,188,212,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

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

    st.markdown("<div class='dashboard-box'>", unsafe_allow_html=True)
    st.success("🚀 Dashboard carregado com sucesso!")
    st.write("Aqui entra todo o conteúdo do seu sistema.")
    st.markdown("</div>", unsafe_allow_html=True)
