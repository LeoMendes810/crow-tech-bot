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

# Carregamento de imagens
bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- CSS GLOBAL (LIMPEZA DO STREAMLIT) ---
st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 55% !important;
        background-attachment: fixed !important;
    }}

    /* Esconde os inputs reais do Streamlit que ficam no fundo */
    .stTextInput, .stButton, [data-testid="stForm"] {{
        position: absolute;
        opacity: 0;
        pointer-events: none;
    }}
    </style>
""", unsafe_allow_html=True)

# --- FUNÇÃO DE LOGIN (HTML PURO PARA DESIGN IDENTICO) ---
def login_screen():
    # Design idêntico à imagem escolhida
    st.markdown(f"""
    <div style="
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 380px;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 40px;
        text-align: center;
        box-shadow: 0 25px 50px rgba(0,0,0,0.5);
        z-index: 9999;
        font-family: sans-serif;
    ">
        <div style="width: 70px; height: 70px; background: rgba(255,255,255,0.1); border-radius: 50%; margin: 0 auto 15px; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(255,255,255,0.2);">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="white"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08s5.97 1.09 6 3.08c-1.29 1.94-3.5 3.22-6 3.22z"/></svg>
        </div>
        
        <img src="data:image/png;base64,{logo_base64}" width="200" style="margin-bottom: 5px;">
        <p style="color: #00bcd4; font-size: 10px; letter-spacing: 2px; margin-bottom: 30px; font-weight: bold;">CROW TECH ELITE</p>

        <div style="text-align: left;">
            <p style="color: rgba(255,255,255,0.5); font-size: 11px; margin-bottom: 5px;">USERNAME</p>
            <div style="border-bottom: 1px solid rgba(255,255,255,0.3); padding: 5px 0; color: white; font-size: 14px; margin-bottom: 20px;">Use os campos abaixo para digitar</div>
            
            <p style="color: rgba(255,255,255,0.5); font-size: 11px; margin-bottom: 5px;">PASSWORD</p>
            <div style="border-bottom: 1px solid rgba(255,255,255,0.3); padding: 5px 0; color: white; font-size: 14px;">••••••••</div>
        </div>

        <div style="display: flex; justify-content: space-between; margin-top: 15px; font-size: 11px; color: rgba(255,255,255,0.4);">
            <span>☐ Lembrar-me</span>
            <span>Esqueceu a senha?</span>
        </div>

        <div style="margin-top: 30px; background: #00bcd4; color: black; padding: 10px; border-radius: 5px; font-weight: bold; cursor: pointer; box-shadow: 0 0 15px rgba(0,188,212,0.4);">
            CLIQUE EM ACESSAR ABAIXO
        </div>
        
        <p style="color: rgba(255,255,255,0.3); font-size: 10px; margin-top: 20px;">Don't have an account? Register now</p>
    </div>
    """, unsafe_allow_html=True)

    # Inputs Reais (Para o funcionamento do Python) - Eles aparecem discretos abaixo do card
    st.write("---") # Espaçador para não sobrepor
    with st.form("RealLogin"):
        u = st.text_input("Usuário")
        p = st.text_input("Senha", type="password")
        if st.form_submit_button("ACESSAR SISTEMA"):
            if u == "admin" and p == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Erro!")

# Fluxo principal
if not st.session_state.logado:
    login_screen()
else:
    st.title("Crow Tech - Dashboard Ativo")
    if st.button("Logout"):
        st.session_state.logado = False
        st.rerun()
