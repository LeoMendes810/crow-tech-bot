import streamlit as st
import base64

# 1. Configuração da página (Deve ser a primeira linha)
st.set_page_config(page_title="Crow Tech Elite", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return None

# Carregamento da Marca d'água
bg_base64 = get_base64('assets/corvo_bg.png')
bg_css = f"url(data:image/png;base64,{bg_base64})" if bg_base64 else "none"

if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- CSS DE ALTA PERFORMANCE (IDÊNTICO À REFERÊNCIA) ---
st.markdown(f"""
    <style>
    /* Remover lixo visual do Streamlit */
    header, footer, .stDeployButton {{ visibility: hidden !important; }}
    [data-testid="stHeader"] {{ background: rgba(0,0,0,0) !important; }}

    /* FUNDO: Dark com Marca d'água centralizada e fixa */
    .stApp {{
        background-color: #0b0e14 !important;
        background-image: linear-gradient(rgba(11, 14, 20, 0.8), rgba(11, 14, 20, 0.8)), {bg_css} !important;
        background-size: 60% !important;
        background-repeat: no-repeat !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}

    /* CONTAINER CENTRAL (O QUADRADO TRANSPARENTE) */
    .glass-container {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 60px 40px;
        width: 400px;
        text-align: center;
        z-index: 999;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5);
    }}

    /* LOGO E TEXTO DENTRO DO CARD */
    .logo-img {{ margin-bottom: 20px; }}
    .login-title {{
        color: white;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 30px;
        letter-spacing: 2px;
    }}

    /* INPUTS (Linhagem limpa igual à referência) */
    .stTextInput input {{
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: white !important;
        border: none !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 0px !important;
        padding: 10px 5px !important;
        font-size: 16px !important;
        margin-bottom: 20px !important;
    }}
    .stTextInput input:focus {{
        border-bottom: 2px solid #00bcd4 !important;
    }}

    /* BOTÃO LOGIN (Ciano Neon) */
    .stButton > button {{
        background-color: #00bcd4 !important;
        color: black !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        width: 100% !important;
        border-radius: 8px !important;
        padding: 12px !important;
        border: none !important;
        margin-top: 20px !important;
        box-shadow: 0 10px 20px rgba(0, 188, 212, 0.3) !important;
    }}

    /* LINKS DE RODAPÉ */
    .footer-links {{
        margin-top: 25px;
        display: flex;
        justify-content: space-between;
        font-size: 12px;
        color: rgba(255, 255, 255, 0.5);
    }}
    
    label {{ color: rgba(255, 255, 255, 0.6) !important; text-align: left !important; display: block; }}
    
    /* Remove bordas do Form */
    [data-testid="stForm"] {{ border: none !important; padding: 0 !important; }}
    </style>
""", unsafe_allow_html=True)

def mostrar_tela_login():
    # Estrutura HTML do Card de Vidro
    st.markdown("""
        <div class="glass-container">
    """, unsafe_allow_html=True)
    
    # 1. Logo dentro do Card
    st.image("assets/logo.png", width=200)
    st.markdown('<div class="login-title">LOGIN</div>', unsafe_allow_html=True)

    # 2. Formulário
    with st.form("login_form"):
        u = st.text_input("USUÁRIO", placeholder="Ex: admin")
        p = st.text_input("SENHA", type="password", placeholder="••••••••")
        
        if st.form_submit_button("ACESSAR SISTEMA"):
            if u == "admin" and p == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Credenciais inválidas")

    # 3. Rodapé do Card
    st.markdown("""
        <div class="footer-links">
            <span>Criar conta</span>
            <span>Esqueceu a senha?</span>
        </div>
        </div>
    """, unsafe_allow_html=True)

# Lógica principal
if not st.session_state.logado:
    mostrar_tela_login()
else:
    st.title("Dashboard Crow Tech")
    if st.button("Sair"):
        st.session_state.logado = False
        st.rerun()
