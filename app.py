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

# Carregamento das imagens da pasta assets
bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')
bg_css = f"url(data:image/png;base64,{bg_base64})" if bg_base64 else ""

if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- CSS DE PRECISÃO PARA REPRODUZIR A IMAGEM ---
st.markdown(f"""
    <style>
    /* Remover interface padrão */
    header, footer, .stDeployButton {{ visibility: hidden !important; }}
    [data-testid="stHeader"] {{ background: rgba(0,0,0,0) !important; }}

    /* FUNDO: Dark + Marca d'água */
    .stApp {{
        background-color: #0b1016 !important;
        background-image: linear-gradient(rgba(11, 16, 22, 0.85), rgba(11, 16, 22, 0.85)), {bg_css} !important;
        background-size: 65% !important;
        background-repeat: no-repeat !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}

    /* CONTAINER CENTRALIZADO (O QUADRADO) */
    .main-container {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 40px;
        width: 400px;
        text-align: center;
        box-shadow: 0 20px 60px rgba(0,0,0,0.5);
        z-index: 1000;
    }}

    /* ICONE DE USUARIO NO TOPO */
    .user-avatar {{
        width: 70px;
        height: 70px;
        background: rgba(255,255,255,0.1);
        border-radius: 50%;
        margin: 0 auto 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid rgba(255,255,255,0.2);
    }}

    /* INPUTS MINIMALISTAS (LINHAS) */
    .stTextInput input {{
        background-color: transparent !important;
        color: white !important;
        border: none !important;
        border-bottom: 1px solid rgba(255,255,255,0.3) !important;
        border-radius: 0px !important;
        padding: 10px 0px !important;
        font-size: 14px !important;
    }}
    .stTextInput input:focus {{
        border-bottom: 2px solid #00bcd4 !important;
        box-shadow: none !important;
    }}

    /* BOTÃO LOGIN (CIANO NEON) */
    .stButton > button {{
        background-color: #00bcd4 !important;
        color: black !important;
        font-weight: bold !important;
        width: 130px !important;
        border: none !important;
        padding: 8px !important;
        border-radius: 4px !important;
        margin-top: 25px !important;
        box-shadow: 0 0 15px rgba(0, 188, 212, 0.4) !important;
    }}

    /* TEXTOS AUXILIARES */
    label {{ color: rgba(255,255,255,0.5) !important; font-size: 11px !important; text-align: left !important; }}
    .footer-info {{
        display: flex;
        justify-content: space-between;
        margin-top: 15px;
        font-size: 11px;
        color: rgba(255,255,255,0.4);
    }}

    [data-testid="stForm"] {{ border: none !important; padding: 0 !important; }}
    </style>
""", unsafe_allow_html=True)

if not st.session_state.logado:
    # Renderização do Login
    st.markdown(f"""
        <div class="main-container">
            <div class="user-avatar">
                <img src="https://img.icons8.com/ios-filled/50/ffffff/user-male-circle.png" width="40"/>
            </div>
            <img src="data:image/png;base64,{get_base64('assets/logo.png')}" width="220">
            <p style='color: #8b949e; font-size: 12px; margin-top: 5px;'>Inteligência em cada movimento</p>
    """, unsafe_allow_html=True)

    with st.form("login_form"):
        u = st.text_input("USERNAME", placeholder="Usuário")
        p = st.text_input("PASSWORD", type="password", placeholder="Senha")
        
        st.markdown("""
            <div class="footer-info">
                <span>Lembrar-me</span>
                <span>Esqueceu a senha?</span>
            </div>
        """, unsafe_allow_html=True)
        
        # Centralizando o botão no form
        c1, c2, c3 = st.columns([1, 1.5, 1])
        with c2:
            submit = st.form_submit_button("LOGIN")
            
        if submit:
            if u == "admin" and p == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Credenciais Inválidas")

    st.markdown("""
            <p style='color: rgba(255,255,255,0.3); font-size: 10px; margin-top: 20px;'>Criar conta agora</p>
        </div>
    """, unsafe_allow_html=True)

else:
    st.write("### Área Logada Crow Tech")
    if st.button("Sair"):
        st.session_state.logado = False
        st.rerun()
