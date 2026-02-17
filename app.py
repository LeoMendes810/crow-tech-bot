import streamlit as st
import base64

# 1. Configuração da página
st.set_page_config(page_title="Crow Tech Elite", layout="wide")

# Função para converter imagem para Base64 (Garante que a marca d'água apareça)
def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return None

bg_base64 = get_base64('assets/corvo_bg.png')
bg_css = f"url(data:image/png;base64,{bg_base64})" if bg_base64 else "none"

if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- CSS DARK TOTAL E CENTRALIZAÇÃO ---
st.markdown(f"""
    <style>
    /* Remover tudo do Streamlit */
    header, footer, .stDeployButton {{ visibility: hidden !important; }}
    
    /* Fundo Dark com Marca d'água Centralizada */
    .stApp {{
        background-color: #0e1117;
        background-image: linear-gradient(rgba(14, 17, 23, 0.9), rgba(14, 17, 23, 0.9)), {bg_css};
        background-size: 55% !important;
        background-repeat: no-repeat !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}

    /* Container de Login Centralizado */
    .main-login {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 70vh;
        width: 100%;
        text-align: center;
    }}

    /* Estilo dos Inputs (Dark e sem brilho excessivo) */
    .stTextInput > div > div > input {{
        background-color: #161b22 !important;
        color: white !important;
        border: 1px solid #30363d !important;
        border-radius: 4px !important;
        text-align: center !important;
        width: 300px !important;
    }}
    
    label {{
        color: white !important;
        font-weight: bold !important;
        display: block;
        text-align: center;
        width: 100%;
    }}

    /* Botão de Acesso (Simples e Dark) */
    .stButton > button {{
        background-color: transparent !important;
        color: #ffffff !important;
        border: 1px solid #30363d !important;
        padding: 5px 40px !important;
        margin-top: 10px;
    }}
    
    /* Remover o quadrado do form do Streamlit */
    [data-testid="stForm"] {{ border: none !important; padding: 0 !important; }}
    </style>
""", unsafe_allow_html=True)

def tela_login():
    # Centralização via Container
    st.markdown('<div class="main-login">', unsafe_allow_html=True)
    
    # Logo Centralizado
    st.image("assets/logo.png", width=300)
    
    # Espaço simples para os campos
    with st.form("login_centralizado"):
        user = st.text_input("USUÁRIO")
        password = st.text_input("SENHA", type="password")
        
        # Botão Centralizado
        submit = st.form_submit_button("ACESSAR")
        
        if submit:
            if user == "admin" and password == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Dados incorretos")

    st.markdown('</div>', unsafe_allow_html=True)

# Lógica
if not st.session_state.logado:
    tela_login()
else:
    st.write("# Dashboard Crow Tech")
    if st.button("Sair"):
        st.session_state.logado = False
        st.rerun()
