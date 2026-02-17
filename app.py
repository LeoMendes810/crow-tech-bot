import streamlit as st
import base64

# 1. Configuração da página
st.set_page_config(page_title="Crow Tech Elite", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return None

# Carregamento da Marca d'água (Corvo ao fundo)
bg_base64 = get_base64('assets/corvo_bg.png')
bg_css = f"url(data:image/png;base64,{bg_base64})" if bg_base64 else "none"

if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- CSS DEFINITIVO: CROW TECH GLASSMORPHISM ---
st.markdown(f"""
    <style>
    /* Reset de interface */
    header, footer, .stDeployButton {{ visibility: hidden !important; }}
    [data-testid="stHeader"] {{ background: rgba(0,0,0,0) !important; }}

    /* FUNDO: Dark com Corvo centralizado */
    .stApp {{
        background-color: #0b0e14 !important;
        background-image: linear-gradient(rgba(11, 14, 20, 0.85), rgba(11, 14, 20, 0.85)), {bg_css} !important;
        background-size: 60% !important;
        background-repeat: no-repeat !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}

    /* QUADRADO DE LOGIN (GLASS) */
    .glass-container {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 40px;
        width: 420px;
        text-align: center;
        box-shadow: 0 0 40px rgba(0, 0, 0, 0.5), 0 0 20px rgba(0, 188, 212, 0.1);
        z-index: 1000;
    }}

    /* AVATAR CIRCULAR NO TOPO */
    .user-icon {{
        width: 80px;
        height: 80px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 50%;
        margin: 0 auto 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}

    /* INPUTS MINIMALISTAS */
    .stTextInput input {{
        background-color: transparent !important;
        color: white !important;
        border: none !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 0px !important;
        padding: 10px 5px !important;
        font-size: 15px !important;
        text-align: left !important;
    }}
    .stTextInput input:focus {{
        border-bottom: 2px solid #00bcd4 !important;
        box-shadow: none !important;
    }}

    /* BOTÃO LOGIN NEON */
    .stButton > button {{
        background-color: #00bcd4 !important;
        color: #000 !important;
        font-weight: bold !important;
        width: 100% !important;
        border: none !important;
        padding: 10px !important;
        border-radius: 5px !important;
        margin-top: 25px !important;
        box-shadow: 0 0 15px rgba(0, 188, 212, 0.5) !important;
    }}

    /* TEXTOS E LINKS */
    .label-text {{ color: rgba(255, 255, 255, 0.5); font-size: 0.8rem; text-align: left; }}
    .footer-links {{ margin-top: 15px; color: rgba(255, 255, 255, 0.4); font-size: 0.8rem; display: flex; justify-content: space-between; }}
    
    [data-testid="stForm"] {{ border: none !important; padding: 0 !important; }}
    </style>
""", unsafe_allow_html=True)

def mostrar_tela_login():
    # Estrutura do Card de Vidro
    st.markdown(f"""
        <div class="glass-container">
            <div class="user-icon">
                <img src="https://img.icons8.com/ios-filled/50/ffffff/user-male-circle.png" width="40"/>
            </div>
            <img src="https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/logo.png" width="220">
            <p style='color: #8b949e; font-style: italic; font-size: 12px;'>Inteligência em cada movimento</p>
            <br>
    """, unsafe_allow_html=True)

    with st.form("login_form"):
        u = st.text_input("USUÁRIO", placeholder="Seu usuário")
        p = st.text_input("SENHA", type="password", placeholder="••••••••")
        
        # Links rápidos dentro do card
        st.markdown("""
            <div class="footer-links">
                <span>Lembrar-me</span>
                <span style="cursor:pointer">Esqueceu a senha?</span>
            </div>
        """, unsafe_allow_html=True)
        
        if st.form_submit_button("LOGIN
