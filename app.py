import streamlit as st

# 1. Configuração da página - MANTÉM O LAYOUT WIDE
st.set_page_config(page_title="Crow Tech Elite", layout="wide")

if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- CSS DEFINITIVO: TRAVANDO O LAYOUT ---
st.markdown("""
    <style>
    header { visibility: hidden; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0) !important; }
    
    /* MARCA D'ÁGUA: Só o corvo centralizado ao fundo */
    .stApp {
        background-color: #0e1117;
        background-image: linear-gradient(rgba(14, 17, 23, 0.8), rgba(14, 17, 23, 0.8)), 
                          url("app/static/assets/corvo_bg.png");
        background-size: 55%; 
        background-repeat: no-repeat; 
        background-position: center;
    }

    /* CONTAINER DE LOGIN: Fixado na esquerda para não sumir */
    .login-wrapper {
        max-width: 400px;
        margin-left: 5%;
        margin-top: 3%;
    }

    /* SLOGAN: Ajustado conforme a imagem do Termux */
    .slogan-text {
        color: #8b949e;
        font-style: italic;
        font-size: 1.1rem;
        margin-top: -15px;
        margin-bottom: 30px;
    }

    /* BOTÃO ENTRAR: Estilo 'Outlined' (sem fundo) */
    .stButton > button {
        background-color: transparent !important;
        color: #0ea5e9 !important;
        border: 1px solid #0ea5e9 !important;
        padding: 5px 25px !important;
        width: auto !important;
    }
    
    /* Esconder o quadrado cinza do form original */
    [data-testid="stForm"] { border: none !important; padding: 0 !important; }
    
    /* Labels Brancos */
    label { color: white !important; font-weight: bold !important; }
    </style>
""", unsafe_allow_html=True)

def mostrar_tela_login():
    # Colunas para garantir que o conteúdo fique na esquerda e o fundo livre
    col_login, col_espaco = st.columns([1, 1.5])
    
    with col_login:
        st.markdown('<div class="login-wrapper">', unsafe_allow_html=True)
        
        # LOGO PRINCIPAL (Com nome)
        st.image("assets/logo.png", width=300)
        
        # SLOGAN (Correto da imagem do Termux)
        st.markdown('<p class="slogan-text">Inteligência em cada movimento</p>', unsafe_allow_html=True)

        # INPUTS
        usuario = st.text_input("USUÁRIO", key="user_login")
        senha = st.text_input("SENHA", type="password", key="pass_login")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # BOTÃO ACESSAR
        if st.button("ENTRAR"):
            if usuario == "admin" and senha == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Acesso Negado")
        
        st.markdown('</div>', unsafe_allow_html=True)

# Lógica
if not st.session_state.logado:
    mostrar_tela_login()
else:
    st.write("# Dashboard Ativo")
