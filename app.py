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

# --- CSS DEFINITIVO: FOCO NA IMAGEM DE REFERÊNCIA ---
st.markdown(f"""
    <style>
    /* Reset total do Streamlit */
    header, footer, .stDeployButton {{ visibility: hidden !important; }}
    [data-testid="stHeader"] {{ background: rgba(0,0,0,0) !important; }}

    /* FUNDO: Dark profundo com a marca d'água centralizada */
    .stApp {{
        background-color: #0b0e14 !important;
        background-image: linear-gradient(rgba(11, 14, 20, 0.88), rgba(11, 14, 20, 0.88)), {bg_css} !important;
        background-size: 55% !important;
        background-repeat: no-repeat !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}

    /* O QUADRADO DE LOGIN (Glassmorphism Centralizado) */
    .glass-card {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 40px;
        width: 400px;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6);
        z-index: 9999;
    }}

    /* ÍCONE DE USUÁRIO (Igual à imagem) */
    .user-avatar {{
        width: 70px;
        height: 70px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 50%;
        margin: 0 auto 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}

    /* TÍTULO LOGIN */
    .login-header {{
        color: white;
        font-size: 22px;
        font-weight: 500;
        letter-spacing: 2px;
        margin-bottom: 30px;
    }}

    /* INPUTS (Apenas linha inferior, igual à referência) */
    .stTextInput input {{
        background-color: transparent !important;
        color: white !important;
        border: none !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 0px !important;
        padding: 10px 5px !important;
        font-size: 15px !important;
        margin-bottom: 15px !important;
    }}
    .stTextInput input:focus {{
        border-bottom: 2px solid #00bcd4 !important;
        box-shadow: none !important;
    }}

    /* BOTÃO LOGIN (Ciano Neon Centralizado) */
    .stButton > button {{
        background-color: #00bcd4 !important;
        color: #000000 !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        width: 120px !important;
        margin: 20px auto 0 !important;
        display: block !important;
        border-radius: 5px !important;
        border: none !important;
        box-shadow: 0 5px 15px rgba(0, 188, 212, 0.4) !important;
    }}

    /* LINKS DISCRETOS */
    .footer-text {{
        margin-top: 20px;
        font-size: 11px;
        color: rgba(255, 255, 255, 0.4);
        display: flex;
        justify-content: space-between;
    }}

    /* Remover labels padrão do Streamlit para usar os placeholders como a imagem */
    label {{ display: none !important; }}
    [data-testid="stForm"] {{ border: none !important; padding: 0 !important; }}
    </style>
""", unsafe_allow_html=True)

def mostrar_login():
    # Início do Card
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    # Elementos do Topo
    st.markdown("""
        <div class="user-avatar">
            <img src="https://img.icons8.com/ios-filled/50/ffffff/user-male-circle.png" width="40"/>
        </div>
        <div class="login-header">SIGN IN</div>
    """, unsafe_allow_html=True)

    with st.form("form_crow"):
        # Inputs sem label (usando placeholder igual à imagem)
        u = st.text_input("USUÁRIO", placeholder="Username")
        p = st.text_input("SENHA", type="password", placeholder="Password")
        
        # Link de "Lembrar" e "Esqueci"
        st.markdown("""
            <div class="footer-text">
                <span>☐ Remember me</span>
                <span>Forgot password?</span>
            </div>
        """, unsafe_allow_html=True)
        
        # Botão centralizado
        if st.form_submit_button("LOGIN"):
            if u == "admin" and p == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Credenciais inválidas")

    # Link final
    st.markdown("<p style='font-size: 10px; color: rgba(255,255,255,0.3); margin-top: 20px;'>Don't have an account? Register now</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Fluxo do App
if not st.session_state.logado:
    mostrar_login()
else:
    st.success("Logado! Bem-vindo ao Crow Tech Dashboard.")
    if st.button("Logout"):
        st.session_state.logado = False
        st.rerun()
