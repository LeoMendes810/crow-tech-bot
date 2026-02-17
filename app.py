import streamlit as st
import base64

# 1. Configuração da página
st.set_page_config(page_title="Crow Tech Elite", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None

# Carregamento das imagens
bg_base64 = get_base64('assets/corvo_bg.png')
bg_css = f"url(data:image/png;base64,{bg_base64})" if bg_base64 else "none"

if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- CSS PARA CENTRALIZAÇÃO E GLASSMORPHISM ---
st.markdown(f"""
    <style>
    /* Esconder menus do Streamlit */
    header, footer, .stDeployButton {{ visibility: hidden !important; }}
    [data-testid="stHeader"] {{ background: rgba(0,0,0,0) !important; }}

    /* FUNDO: Dark com Corvo centralizado e fixo */
    .stApp {{
        background-color: #0b1016 !important;
        background-image: linear-gradient(rgba(11, 16, 22, 0.85), rgba(11, 16, 22, 0.85)), {bg_css} !important;
        background-size: 55% !important;
        background-repeat: no-repeat !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}

    /* O QUADRADO DE VIDRO (Centralizado na tela) */
    .login-card {{
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
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
        z-index: 1000;
    }}

    /* ÍCONE DE USUÁRIO (AVATAR CIRCULAR) */
    .avatar-icon {{
        width: 70px;
        height: 70px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 50%;
        margin: 0 auto 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}

    /* INPUTS (LINHA BRANCA MINIMALISTA) */
    .stTextInput input {{
        background-color: transparent !important;
        color: white !important;
        border: none !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 0px !important;
        padding: 10px 5px !important;
        font-size: 14px !important;
        text-align: left !important;
    }}
    .stTextInput input:focus {{
        border-bottom: 2px solid #00bcd4 !important;
        box-shadow: none !important;
    }}

    /* BOTÃO LOGIN (CIANO NEON) */
    .stButton > button {{
        background-color: #00bcd4 !important;
        color: #000 !important;
        font-weight: bold !important;
        width: 120px !important;
        border: none !important;
        padding: 8px !important;
        border-radius: 5px !important;
        margin-top: 25px !important;
        box-shadow: 0 0 15px rgba(0, 188, 212, 0.4) !important;
    }}

    /* LABELS E TEXTOS */
    label {{ color: rgba(255, 255, 255, 0.5) !important; font-size: 10px !important; text-align: left !important; display: block; }}
    .footer-links {{ margin-top: 15px; display: flex; justify-content: space-between; font-size: 11px; color: rgba(255, 255, 255, 0.4); }}
    
    [data-testid="stForm"] {{ border: none !important; padding: 0 !important; }}
    </style>
""", unsafe_allow_html=True)

def mostrar_login():
    # Criação do Card via HTML/CSS
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    
    # Avatar e Logo (Dentro do card)
    st.markdown("""
        <div class="avatar-icon">
            <img src="https://img.icons8.com/ios-filled/50/ffffff/user-male-circle.png" width="40"/>
        </div>
    """, unsafe_allow_html=True)
    st.image("assets/logo.png", width=220)
    
    # Formulário de Login
    with st.form("form_login"):
        user = st.text_input("USUÁRIO", placeholder="Username")
        password = st.text_input("SENHA", type="password", placeholder="Password")
        
        st.markdown("""
            <div class="footer-links">
                <span>☐ Lembrar-me</span>
                <span>Esqueceu a senha?</span>
            </div>
        """, unsafe_allow_html=True)
        
        # Botão centralizado
        col_btn_l, col_btn_c, col_btn_r = st.columns([1,1.2,1])
        with col_btn_c:
            btn_acesso = st.form_submit_button("LOGIN")
        
        if btn_acesso:
            if user == "admin" and password == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Credenciais inválidas")

    # Rodapé do Card
    st.markdown("<p style='font-size: 10px; color: rgba(255,255,255,0.3); margin-top: 20px;'>Não tem uma conta? Registre-se agora</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Lógica principal
if not st.session_state.logado:
    mostrar_login()
else:
    st.title("Crow Tech - Dashboard")
    if st.button("Sair"):
        st.session_state.logado = False
        st.rerun()
