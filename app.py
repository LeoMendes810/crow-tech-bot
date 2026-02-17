import streamlit as st
import base64

# 1. Configuração da página (Primeira linha sempre)
st.set_page_config(page_title="Crow Tech Elite", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return None

# Carregando as imagens da sua pasta assets
logo_main = "assets/logo.png"
corvo_bg = get_base64('assets/corvo_bg.png')
bg_img = f"url(data:image/png;base64,{corvo_bg})" if corvo_bg else "none"

if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- CSS DEFINITIVO: DARK GLASSMORPHISM ---
st.markdown(f"""
    <style>
    /* Remover cabeçalhos e menus do Streamlit */
    header, footer, .stDeployButton {{ visibility: hidden !important; }}
    [data-testid="stHeader"] {{ background: rgba(0,0,0,0) !important; }}

    /* Fundo Dark com Marca d'água Grande e Centralizada */
    .stApp {{
        background-color: #0b0e14 !important;
        background-image: linear-gradient(rgba(11, 14, 20, 0.8), rgba(11, 14, 20, 0.8)), {bg_img} !important;
        background-size: 65% !important;
        background-repeat: no-repeat !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}

    /* Container de Vidro (O Quadrado Transparente) */
    .glass-card {{
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 50px;
        max-width: 450px;
        margin: auto;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
        text-align: center;
    }}

    /* Inputs Estilizados */
    .stTextInput input {{
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 10px !important;
        height: 45px !important;
        text-align: center !important;
    }}

    /* Labels */
    label {{
        color: rgba(255, 255, 255, 0.8) !important;
        font-weight: bold !important;
        letter-spacing: 1px;
    }}

    /* Botão de Login (Ciano Neon) */
    .stButton > button {{
        background-color: #00bcd4 !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 10px 0 !important;
        font-weight: bold !important;
        font-size: 1rem !important;
        width: 100% !important;
        box-shadow: 0 0 15px rgba(0, 188, 212, 0.4) !important;
        transition: 0.3s !important;
    }}
    .stButton > button:hover {{
        transform: scale(1.02);
        box-shadow: 0 0 25px rgba(0, 188, 212, 0.7) !important;
    }}

    /* Links de rodapé */
    .footer-link button {{
        background: none !important;
        border: none !important;
        color: rgba(255, 255, 255, 0.5) !important;
        font-size: 0.8rem !important;
        text-decoration: underline !important;
    }}

    /* Remover borda do Form */
    [data-testid="stForm"] {{ border: none !important; padding: 0 !important; }}
    </style>
""", unsafe_allow_html=True)

def mostrar_tela_login():
    # Centralização vertical
    st.write("<br><br><br>", unsafe_allow_html=True)
    
    # O Quadrado de Vidro
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    # Logo Principal dentro do quadrado
    st.image(logo_main, width=280)
    st.write("<br>", unsafe_allow_html=True)

    with st.form("login_crow"):
        user = st.text_input("USUÁRIO", placeholder="Seu usuário...")
        password = st.text_input("SENHA", type="password", placeholder="••••••••")
        
        st.write("<br>", unsafe_allow_html=True)
        
        if st.form_submit_button("LOGIN"):
            if user == "admin" and password == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Acesso negado")

    # Links inferiores
    col_l1, col_l2 = st.columns(2)
    with col_l1:
        st.markdown('<div class="footer-link">', unsafe_allow_html=True)
        if st.button("Criar conta"): pass
        st.markdown('</div>', unsafe_allow_html=True)
    with col_l2:
        st.markdown('<div class="footer-link">', unsafe_allow_html=True)
        if st.button("Esqueceu a senha?"): pass
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Navegação
if not st.session_state.logado:
    mostrar_tela_login()
else:
    st.success("Logado com sucesso!")
    if st.button("SAIR"):
        st.session_state.logado = False
        st.rerun()
