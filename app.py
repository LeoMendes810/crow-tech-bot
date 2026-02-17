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

# Carregamento das imagens
bg_base64 = get_base64('assets/corvo_bg.png')
bg_css = f"url(data:image/png;base64,{bg_base64})" if bg_base64 else "none"

if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- CSS PROFISSIONAL: LOGIN À ESQUERDA + FUNDO ESTÁTICO ---
st.markdown(f"""
    <style>
    /* 1. FUNDO: Marca d'água sempre no centro, sem se mover */
    .stApp {{
        background-color: #0e1117 !important;
        background-image: linear-gradient(rgba(14, 17, 23, 0.85), rgba(14, 17, 23, 0.85)), {bg_css} !important;
        background-size: 50% !important;
        background-repeat: no-repeat !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}

    /* 2. REMOVER RUÍDOS */
    header, footer {{ visibility: hidden !important; }}
    [data-testid="stHeader"] {{ background: rgba(0,0,0,0) !important; }}

    /* 3. AREA DE LOGIN: Fixa na Esquerda */
    .login-sidebar {{
        margin-left: 5%;
        margin-top: 50px;
        max-width: 380px;
    }}

    /* 4. LABELS E INPUTS */
    label {{ color: white !important; font-weight: bold !important; font-size: 0.9rem !important; }}
    .stTextInput input {{
        background-color: #161b22 !important;
        color: white !important;
        border: 1px solid #30363d !important;
        border-radius: 5px !important;
    }}

    /* 5. BOTÃO ENTRAR: Sem fundo, borda ciano */
    .stButton > button {{
        background-color: transparent !important;
        color: #0ea5e9 !important;
        border: 1px solid #0ea5e9 !important;
        padding: 5px 30px !important;
        border-radius: 4px !important;
        width: auto !important;
    }}

    /* 6. LINKS DE APOIO: Estilo discreto */
    .support-links {{
        margin-top: 25px;
        font-size: 0.85rem;
    }}
    
    .slogan-box {{
        color: #8b949e;
        font-style: italic;
        margin-top: -15px;
        margin-bottom: 35px;
    }}
    </style>
""", unsafe_allow_html=True)

def mostrar_tela_login():
    # Grid: Coluna 1 (Login) | Coluna 2 (Espaço para a marca d'água aparecer)
    col_login, col_vazia = st.columns([1, 1.5])
    
    with col_login:
        st.markdown('<div class="login-sidebar">', unsafe_allow_html=True)
        
        # LOGO PRINCIPAL
        st.image("assets/logo.png", width=300)
        st.markdown('<p class="slogan-box">Inteligência em cada movimento</p>', unsafe_allow_html=True)

        # INPUTS
        u = st.text_input("USUÁRIO", key="usr")
        p = st.text_input("SENHA", type="password", key="pwd")
        
        st.write("")
        
        # BOTAO ENTRAR
        if st.button("ENTRAR"):
            if u == "admin" and p == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Credenciais inválidas.")

        # LINKS DE APOIO (CRIAR CONTA / ESQUECEU)
        st.markdown('<div class="support-links">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Criar conta", key="create"):
                st.info("Contate o administrador.")
        with c2:
            if st.button("Esqueceu a senha?", key="forgot"):
                st.warning("Sistema de recuperação externo.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# LÓGICA
if not st.session_state.logado:
    mostrar_tela_login()
else:
    st.markdown("# DASHBOARD ATIVO")
    if st.button("SAIR"):
        st.session_state.logado = False
        st.rerun()
