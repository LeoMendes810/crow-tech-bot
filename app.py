import streamlit as st
import base64

# 1. Configuração da página (Must be first)
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

# --- CSS DE NÍVEL PREMIUM ---
st.markdown(f"""
    <style>
    /* 1. Limpeza total de interface */
    header, footer, .stDeployButton {{ visibility: hidden !important; }}
    [data-testid="stHeader"] {{ background: rgba(0,0,0,0) !important; }}

    /* 2. Fundo com Marca d'água Ajustada (Fixo e Elegante) */
    .stApp {{
        background-color: #0b0e14 !important;
        background-image: linear-gradient(rgba(11, 14, 20, 0.93), rgba(11, 14, 20, 0.93)), {bg_css} !important;
        background-size: 45% !important;
        background-repeat: no-repeat !important;
        background-position: 70% center !important; /* Move o corvo um pouco para a direita */
        background-attachment: fixed !important;
    }}

    /* 3. Container de Login Estilo Painel */
    .login-panel {{
        background: rgba(22, 27, 34, 0.5);
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 12px;
        border: 1px solid rgba(48, 54, 61, 0.8);
        max-width: 420px;
        margin-left: 8%;
        margin-top: 5vh;
        box-shadow: 20px 0 50px rgba(0,0,0,0.3);
    }}

    /* 4. Labels e Inputs com contraste profissional */
    label {{ 
        color: #8b949e !important; 
        font-size: 0.8rem !important; 
        letter-spacing: 1px; 
        text-transform: uppercase;
        margin-bottom: 8px !important;
    }}
    
    .stTextInput input {{
        background-color: #0d1117 !important;
        color: #ffffff !important;
        border: 1px solid #30363d !important;
        border-radius: 6px !important;
        padding: 12px !important;
        font-size: 1rem !important;
    }}
    .stTextInput input:focus {{
        border-color: #0ea5e9 !important;
        box-shadow: 0 0 0 1px #0ea5e9 !important;
    }}

    /* 5. Botão de Acesso - O Coração do Layout */
    .stButton > button {{
        background-color: transparent !important;
        color: #0ea5e9 !important;
        border: 1px solid #0ea5e9 !important;
        padding: 10px 40px !important;
        font-size: 0.9rem !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        margin-top: 10px;
    }}
    .stButton > button:hover {{
        background-color: #0ea5e9 !important;
        color: #000000 !important;
        box-shadow: 0 0 15px rgba(14, 165, 233, 0.4);
    }}

    /* 6. Slogan e Links */
    .slogan-txt {{
        color: #57606a;
        font-style: italic;
        font-size: 0.95rem;
        margin-bottom: 35px;
    }}
    
    .link-footer {{
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid #30363d;
        display: flex;
        justify-content: space-between;
    }}
    
    /* Ajuste de botões secundários */
    .sec-btn button {{
        border: none !important;
        background: none !important;
        color: #57606a !important;
        font-size: 0.8rem !important;
        text-decoration: none !important;
    }}
    .sec-btn button:hover {{ color: #0ea5e9 !important; }}
    </style>
""", unsafe_allow_html=True)

def mostrar_tela_login():
    # Coluna 1: O Painel de Controle | Coluna 2: Espaço para a Marca d'água
    c_login, c_void = st.columns([1, 1.8])
    
    with c_login:
        st.markdown('<div class="login-panel">', unsafe_allow_html=True)
        
        # Logo Principal
        st.image("assets/logo.png", width=280)
        st.markdown('<p class="slogan-txt">Inteligência em cada movimento</p>', unsafe_allow_html=True)

        # Inputs
        u = st.text_input("Usuário", key="u_key", placeholder="Digite seu usuário")
        p = st.text_input("Senha", type="password", key="p_key", placeholder="••••••••")
        
        st.write("")
        
        # Ação Principal
        if st.button("Acessar"):
            if u == "admin" and p == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Credenciais inválidas.")

        # Links de Apoio
        st.markdown('<div class="link-footer">', unsafe_allow_html=True)
        cf1, cf2 = st.columns(2)
        with cf1:
            st.markdown('<div class="sec-btn">', unsafe_allow_html=True)
            if st.button("Criar conta", key="c_ac"): pass
            st.markdown('</div>', unsafe_allow_html=True)
        with cf2:
            st.markdown('<div class="sec-btn">', unsafe_allow_html=True)
            if st.button("Perdeu a senha?", key="f_pw"): pass
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# Lógica
if not st.session_state.logado:
    mostrar_tela_login()
else:
    st.markdown("### Dashboard Ativado")
    if st.button("Sair"):
        st.session_state.logado = False
        st.rerun()
