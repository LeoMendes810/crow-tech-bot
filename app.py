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

# --- CSS DE TRAVAMENTO PARA GITHUB CODESPACES ---
st.markdown(f"""
    <style>
    /* Esconde a barra superior do Streamlit */
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    
    /* Fundo Dark Fixo */
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 55% !important;
        background-attachment: fixed !important;
    }}

    /* CENTRALIZADOR DO QUADRADO */
    .main-box {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 380px;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 40px;
        text-align: center;
        box-shadow: 0 25px 50px rgba(0,0,0,0.5);
        z-index: 1000;
    }}

    /* Força os inputs para dentro da caixa */
    .stTextInput, .stButton {{
        width: 100% !important;
    }}

    /* Estilo do Input de Linha */
    input {{
        background: transparent !important;
        border: none !important;
        border-bottom: 1px solid rgba(255,255,255,0.3) !important;
        color: white !important;
        border-radius: 0 !important;
    }}
    
    /* Remove bordas extras do Streamlit */
    [data-testid="stVerticalBlock"] > div:first-child {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 2000;
        width: 300px;
    }}
    </style>
""", unsafe_allow_html=True)

# Estrutura Visual do Card (Apenas o visual)
st.markdown(f"""
    <div class="main-box">
        <div style="width: 70px; height: 70px; background: rgba(255,255,255,0.1); border-radius: 50%; margin: 0 auto 15px; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(255,255,255,0.2);">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="white"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08s5.97 1.09 6 3.08c-1.29 1.94-3.5 3.22-6 3.22z"/></svg>
        </div>
        <img src="data:image/png;base64,{logo_base64}" width="200">
        <p style="color: #00bcd4; font-size: 10px; letter-spacing: 2px; margin-bottom: 40px; font-weight: bold;">CROW TECH ELITE</p>
    </div>
""", unsafe_allow_html=True)

# Funcionalidade Real (Digitável)
if 'logado' not in st.session_state:
    st.session_state.logado = False

if not st.session_state.logado:
    # Os inputs reais são posicionados por cima do design pelo CSS
    user = st.text_input("USUÁRIO", placeholder="Username", label_visibility="collapsed")
    password = st.text_input("SENHA", type="password", placeholder="Password", label_visibility="collapsed")
    
    if st.button("LOGIN"):
        if user == "admin" and password == "crow123":
            st.session_state.logado = True
            st.rerun()
        else:
            st.error("Credenciais Inválidas")
else:
    st.write("### Bem-vindo ao Sistema Crow Tech")
    if st.button("Sair"):
        st.session_state.logado = False
        st.rerun()
