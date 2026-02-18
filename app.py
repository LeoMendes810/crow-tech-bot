import streamlit as st
import base64

# 1. Configuração da página
st.set_page_config(page_title="Crow Tech Elite", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

# Carregar imagens
bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

# --- CSS REFINADO: FOCO NO DETALHE ---
st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 50% !important;
        background-attachment: fixed !important;
    }}

    /* CAIXA DE VIDRO */
    [data-testid="stForm"] {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 360px;
        background: rgba(255, 255, 255, 0.12) !important;
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 20px;
        padding: 20px 35px 35px 35px !important; /* Ajuste no padding superior */
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
        z-index: 9999;
    }}

    /* INPUTS COM LETRA PRETA E VISÍVEL */
    .stTextInput input {{
        background-color: rgba(255, 255, 255, 0.7) !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        border: none !important;
        border-bottom: 2px solid #00bcd4 !important;
        border-radius: 5px !important;
        padding: 8px !important;
        font-weight: bold !important;
    }}

    /* BOTÃO ACESSAR */
    .stButton > button {{
        background-color: #00bcd4 !important;
        color: black !important;
        font-weight: 800 !important;
        width: 100% !important;
        border: none !important;
        box-shadow: 0 0 15px rgba(0, 188, 212, 0.4) !important;
        margin-top: 10px;
        height: 45px;
        text-transform: uppercase;
    }}

    label {{ 
        color: #000000 !important; 
        font-size: 10px !important; 
        font-weight: 900 !important;
        margin-bottom: -5px !important;
    }}

    /* LINKS INFERIORES */
    .link-text {{
        color: #000000;
        font-size: 11px;
        text-decoration: none;
        font-weight: bold;
        cursor: pointer;
    }}
    </style>
""", unsafe_allow_html=True)

if 'logado' not in st.session_state:
    st.session_state.logado = False

if not st.session_state.logado:
    with st.form("login_crow"):
        # LOGO MAIS PARA CIMA (Removido o ícone de silhueta)
        st.markdown(f"""
            <div style="text-align: center; margin-bottom: 10px;">
                <img src="data:image/png;base64,{logo_base64}" width="160">
                <p style="color: #000000; font-size: 9px; letter-spacing: 2px; font-weight: 900; margin-top: -10px;">CROW TECH ELITE</p>
            </div>
        """, unsafe_allow_html=True)

        usuario = st.text_input("USUÁRIO", placeholder="Username")
        senha = st.text_input("SENHA", type="password", placeholder="Password")
        
        # LINHA DE ESQUECI A SENHA
        st.markdown(f"""
            <div style="display: flex; justify-content: flex-end; margin-top: -15px; margin-bottom: 10px;">
                <span class="link-text">Esqueceu a senha?</span>
            </div>
        """, unsafe_allow_html=True)
        
        enviar = st.form_submit_button("ACESSAR SISTEMA")

        # LINHA DE CADASTRO
        st.markdown(f"""
            <div style="text-align: center; margin-top: 20px;">
                <span style="color: rgba(0,0,0,0.6); font-size: 11px;">Não tem conta? </span>
                <span class="link-text" style="color: #004d4d;">Cadastre-se aqui</span>
            </div>
        """, unsafe_allow_html=True)

        if enviar:
            if usuario == "admin" and senha == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Credenciais incorretas")
else:
    st.title("🦅 Crow Tech Dashboard")
    if st.button("Sair"):
        st.session_state.logado = False
        st.rerun()
