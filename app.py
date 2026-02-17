import streamlit as st
import base64

# Configuração da página
st.set_page_config(page_title="Crow Tech Elite", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

# Preparando as imagens
bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- CSS RADICAL (FORÇA TUDO PARA DENTRO DA CAIXA) ---
st.markdown(f"""
    <style>
    /* Esconde o lixo do Streamlit */
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    
    /* Fundo Dark */
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 50% !important;
    }}

    /* O CONTAINER "BLINDADO" */
    .glass-wrapper {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 400px;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 40px;
        z-index: 9999;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0,0,0,0.7);
    }}

    /* Força os inputs do Streamlit a ficarem invisíveis na página mas ativos no código */
    .stTextInput, .stButton, .stForm {{
        position: absolute;
        opacity: 0;
        z-index: -1;
    }}

    /* CSS para os campos visuais dentro do container */
    .visual-input {{
        background: transparent;
        border: none;
        border-bottom: 1px solid rgba(255,255,255,0.3);
        width: 100%;
        color: white;
        padding: 10px 0;
        margin-top: 20px;
        outline: none;
    }}

    .visual-button {{
        background: #00bcd4;
        color: black;
        border: none;
        padding: 12px;
        width: 140px;
        border-radius: 5px;
        font-weight: bold;
        margin-top: 30px;
        cursor: pointer;
        box-shadow: 0 0 15px rgba(0,188,212,0.4);
    }}
    </style>
""", unsafe_allow_html=True)

if not st.session_state.logado:
    # A estrutura HTML que você vê (Idêntica à imagem)
    st.markdown(f"""
        <div class="glass-wrapper">
            <div style="width: 70px; height: 70px; background: rgba(255,255,255,0.1); border-radius: 50%; margin: 0 auto 15px; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(255,255,255,0.2);">
                <img src="https://img.icons8.com/ios-filled/50/ffffff/user-male-circle.png" width="40"/>
            </div>
            <img src="data:image/png;base64,{logo_base64}" width="200">
            <p style="color: rgba(255,255,255,0.5); font-size: 11px; margin-top: 5px;">CROW TECH ELITE</p>
            
            <div style="text-align: left; margin-top: 20px;">
                <label style="color: rgba(255,255,255,0.4); font-size: 10px;">USERNAME</label>
                <div class="visual-input">Username</div>
                <label style="color: rgba(255,255,255,0.4); font-size: 10px; margin-top: 20px; display: block;">PASSWORD</label>
                <div class="visual-input">••••••••</div>
            </div>

            <div style="display: flex; justify-content: space-between; margin-top: 15px; font-size: 11px; color: rgba(255,255,255,0.3);">
                <span>Lembrar-me</span>
                <span>Esqueceu a senha?</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # O Form "Invisível" que faz o login funcionar de verdade
    with st.form("form_real"):
        u = st.text_input("U")
        p = st.text_input("P", type="password")
        if st.form_submit_button("LOGIN"):
            if u == "admin" and p == "crow123":
                st.session_state.logado = True
                st.rerun()

else:
    st.write("### Sistema Ativado")
    if st.button("Sair"):
        st.session_state.logado = False
        st.rerun()
