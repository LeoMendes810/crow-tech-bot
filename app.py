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

# --- CSS PARA COR DA LETRA PRETA ---
st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 50% !important;
        background-attachment: fixed !important;
    }}

    [data-testid="stForm"] {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 380px;
        background: rgba(255, 255, 255, 0.15) !important; /* Aumentei um pouco a opacidade para o preto destacar */
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 20px;
        padding: 30px !important;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
        z-index: 9999;
    }}

    /* ALTERAÇÃO: TEXTO EM PRETO */
    .stTextInput input {{
        background-color: rgba(255, 255, 255, 0.5) !important; /* Fundo leve para o input */
        color: #000000 !important; /* PRETO */
        -webkit-text-fill-color: #000000 !important;
        border: none !important;
        border-bottom: 2px solid #00bcd4 !important;
        border-radius: 5px !important;
        padding: 10px !important;
        font-size: 16px !important;
        font-weight: bold !important;
    }}

    .stButton > button {{
        background-color: #00bcd4 !important;
        color: black !important;
        font-weight: bold !important;
        width: 100% !important;
        border: none !important;
        box-shadow: 0 0 15px rgba(0, 188, 212, 0.4) !important;
        margin-top: 20px;
        height: 45px;
    }}

    label {{ 
        color: #000000 !important; /* Label preta para combinar */
        font-size: 11px !important; 
        font-weight: bold;
    }}
    </style>
""", unsafe_allow_html=True)

if 'logado' not in st.session_state:
    st.session_state.logado = False

if not st.session_state.logado:
    with st.form("login_crow"):
        st.markdown(f"""
            <div style="text-align: center;">
                <div style="width: 65px; height: 65px; background: rgba(0,0,0,0.1); border-radius: 50%; margin: 0 auto 10px; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(0,0,0,0.1);">
                    <img src="https://img.icons8.com/ios-filled/50/000000/user-male-circle.png" width="35"/>
                </div>
                <img src="data:image/png;base64,{logo_base64}" width="180">
                <p style="color: #000000; font-size: 10px; letter-spacing: 2px; font-weight: bold; margin-bottom: 25px;">CROW TECH ELITE</p>
            </div>
        """, unsafe_allow_html=True)

        usuario = st.text_input("USUÁRIO", placeholder="Username")
        senha = st.text_input("SENHA", type="password", placeholder="Password")
        
        enviar = st.form_submit_button("ACESSAR SISTEMA")

        if enviar:
            if usuario == "admin" and senha == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Acesso Negado")
else:
    st.title("🦅 Crow Tech Dashboard")
    if st.button("Sair do Sistema"):
        st.session_state.logado = False
        st.rerun()
