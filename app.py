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

# Carregamento de imagens da pasta assets
bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- CSS PARA TORNAR OS CAMPOS REAIS E INTEGRADOS AO DESIGN ---
st.markdown(f"""
    <style>
    /* Esconder menus padrão */
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    
    /* Fundo Dark com o Corvo centralizado */
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 55% !important;
        background-attachment: fixed !important;
    }}

    /* CONTAINER CENTRAL (O QUADRADO DE VIDRO) */
    .login-box {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 380px;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        box-shadow: 0 25px 50px rgba(0,0,0,0.5);
        z-index: 1000;
    }}

    /* Estilização dos Inputs reais do Streamlit para ficarem minimalistas */
    .stTextInput > div > div > input {{
        background-color: transparent !important;
        color: white !important;
        border: none !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 0px !important;
        padding: 10px 0px !important;
        font-size: 14px !important;
    }}
    
    .stTextInput > div > div > input:focus {{
        border-bottom: 2px solid #00bcd4 !important;
        box-shadow: none !important;
    }}

    /* Botão de Login */
    .stButton > button {{
        background-color: #00bcd4 !important;
        color: black !important;
        font-weight: bold !important;
        width: 100% !important;
        border: none !important;
        padding: 12px !important;
        border-radius: 5px !important;
        margin-top: 20px !important;
        box-shadow: 0 0 15px rgba(0, 188, 212, 0.4) !important;
    }}
    
    /* Labels discretas */
    label {{
        color: rgba(255, 255, 255, 0.5) !important;
        font-size: 10px !important;
        text-transform: uppercase;
        margin-bottom: -15px !important;
    }}

    /* Remove bordas do formulário */
    [data-testid="stForm"] {{ border: none !important; padding: 0 !important; }}
    </style>
""", unsafe_allow_html=True)

def tela_login():
    # Criação da estrutura visual do card
    with st.container():
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        
        # Avatar de usuário (Círculo no topo)
        st.markdown("""
            <div style="width: 70px; height: 70px; background: rgba(255,255,255,0.1); border-radius: 50%; margin: 0 auto 15px; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(255,255,255,0.2);">
                <svg width="40" height="40" viewBox="0 0 24 24" fill="white"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08s5.97 1.09 6 3.08c-1.29 1.94-3.5 3.22-6 3.22z"/></svg>
            </div>
        """, unsafe_allow_html=True)
        
        # Logo Crow Tech
        st.image(f"data:image/png;base64,{logo_base64}", width=200)
        st.markdown('<p style="color: #00bcd4; font-size: 10px; letter-spacing: 2px; margin-bottom: 20px; font-weight: bold;">CROW TECH ELITE</p>', unsafe_allow_html=True)

        # Formulário Real de Login
        with st.form("login_crow"):
            usuario = st.text_input("Username")
            senha = st.text_input("Password", type="password")
            
            st.markdown("""
                <div style="display: flex; justify-content: space-between; margin-top: 10px; font-size: 11px; color: rgba(255,255,255,0.4);">
                    <span>☐ Lembrar-me</span>
                    <span>Esqueceu a senha?</span>
                </div>
            """, unsafe_allow_html=True)
            
            submit = st.form_submit_button("LOGIN")
            
            if submit:
                if usuario == "admin" and senha == "crow123":
                    st.session_state.logado = True
                    st.rerun()
                else:
                    st.error("Usuário ou senha incorretos")

        st.markdown('<p style="color: rgba(255,255,255,0.3); font-size: 10px; margin-top: 20px;">Não tem uma conta? Registre-se agora</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Lógica principal de navegação
if not st.session_state.logado:
    tela_login()
else:
    st.success("Bem-vindo ao Dashboard Crow Tech Elite!")
    if st.button("Logout"):
        st.session_state.logado = False
        st.rerun()
