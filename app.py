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

# Carregar imagens (Certifique-se que estão na pasta assets)
bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

# --- CSS DEFINITIVO E SIMPLIFICADO ---
st.markdown(f"""
    <style>
    /* Remove a sujeira do Streamlit */
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    
    /* Fundo Dark com o Corvo */
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 50% !important;
        background-attachment: fixed !important;
    }}

    /* CENTRALIZAÇÃO DO FORMULÁRIO (A CAIXA DE VIDRO) */
    [data-testid="stForm"] {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 380px;
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 20px;
        padding: 30px !important;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
        z-index: 9999;
    }}

    /* Estilo dos inputs (Linha branca) */
    .stTextInput input {{
        background-color: transparent !important;
        color: white !important;
        border: none !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 0px !important;
        padding: 5px 0px !important;
    }}

    /* Botão Neon */
    .stButton > button {{
        background-color: #00bcd4 !important;
        color: black !important;
        font-weight: bold !important;
        width: 100% !important;
        border: none !important;
        box-shadow: 0 0 15px rgba(0, 188, 212, 0.4) !important;
        margin-top: 20px;
    }}

    /* Ajuste de textos */
    label {{ color: rgba(255, 255, 255, 0.5) !important; font-size: 10px !important; }}
    </style>
""", unsafe_allow_html=True)

# Lógica de Login
if 'logado' not in st.session_state:
    st.session_state.logado = False

if not st.session_state.logado:
    # Tudo dentro deste 'with' ficará preso dentro da caixa de vidro
    with st.form("login_crow"):
        # Ícone e Logo simulados dentro do form
        st.markdown(f"""
            <div style="text-align: center;">
                <div style="width: 60px; height: 60px; background: rgba(255,255,255,0.1); border-radius: 50%; margin: 0 auto 10px; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(255,255,255,0.2);">
                    <img src="https://img.icons8.com/ios-filled/50/ffffff/user-male-circle.png" width="35"/>
                </div>
                <img src="data:image/png;base64,{logo_base64}" width="180">
                <p style="color: #00bcd4; font-size: 10px; letter-spacing: 2px; font-weight: bold; margin-bottom: 20px;">CROW TECH ELITE</p>
            </div>
        """, unsafe_allow_html=True)

        # Inputs Reais (Onde você vai digitar)
        usuario = st.text_input("USUÁRIO", placeholder="Username")
        senha = st.text_input("SENHA", type="password", placeholder="Password")
        
        st.markdown('<p style="color: rgba(255,255,255,0.3); font-size: 10px; text-align: center;">Esqueceu a senha?</p>', unsafe_allow_html=True)
        
        # Botão de Login
        enviar = st.form_submit_button("LOGIN")

        if enviar:
            if usuario == "admin" and senha == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Erro no acesso")
else:
    st.success("Logado na Crow Tech!")
    if st.button("Sair"):
        st.session_state.logado = False
        st.rerun()
