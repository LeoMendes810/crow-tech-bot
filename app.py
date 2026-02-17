import streamlit as st
import base64

# 1. Configuração da página (Deve ser a primeira linha)
st.set_page_config(page_title="Crow Tech Elite", layout="wide")

# Função para converter imagem local para Base64 (Evita erro de carregamento no CSS)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Tenta carregar a marca d'água, se falhar, mantém apenas o fundo escuro
try:
    bin_str = get_base64('assets/corvo_bg.png')
    bg_img = f"url(data:image/png;base64,{bin_str})"
except:
    bg_img = "none"

if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- CSS DE ALTA PRECISÃO (FORÇANDO CENTRALIZAÇÃO) ---
st.markdown(f"""
    <style>
    /* Remover lixo do Streamlit */
    header, footer, .stDeployButton {{ visibility: hidden !important; }}
    
    /* MARCA D'ÁGUA CENTRALIZADA NO FUNDO */
    .stApp {{
        background-color: #0e1117;
        background-image: linear-gradient(rgba(14, 17, 23, 0.9), rgba(14, 17, 23, 0.9)), {bg_img};
        background-size: 50% !important;
        background-repeat: no-repeat !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}

    /* CENTRALIZAÇÃO TOTAL DO CONTEÚDO */
    .main-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 80vh;
        width: 100%;
    }}

    /* ESTILO DOS INPUTS E BOTÃO */
    .stTextInput input {{
        background-color: #161b22 !important;
        color: white !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
        text-align: center;
    }}
    
    label {{
        color: white !important;
        font-weight: bold !important;
        width: 100%;
        text-align: center;
    }}

    /* BOTÃO ENTRAR (SEM FUNDO, MENOR) */
    .stButton > button {{
        background-color: transparent !important;
        color: #0ea5e9 !important;
        border: 1px solid #0ea5e9 !important;
        padding: 5px 40px !important;
        border-radius: 5px !important;
        margin: 0 auto;
        display: block;
    }}
    
    .slogan-style {{
        color: #8b949e;
        font-style: italic;
        margin-top: -20px;
        margin-bottom: 30px;
        text-align: center;
    }}
    </style>
""", unsafe_allow_html=True)

def mostrar_tela_login():
    # Container invisível para centralizar tudo
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2: # Usa a coluna do meio para centralizar no monitor
        st.image("assets/logo.png", width=350)
        st.markdown('<p class="slogan-style">Inteligência em cada movimento</p>', unsafe_allow_html=True)
        
        # Inputs centralizados
        user = st.text_input("USUÁRIO", key="login_u")
        password = st.text_input("SENHA", type="password", key="login_p")
        
        st.write("") # Espaçamento
        
        if st.button("ENTRAR"):
            if user == "admin" and password == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Credenciais inválidas.")

    st.markdown('</div>', unsafe_allow_html=True)

# Lógica Principal
if not st.session_state.logado:
    mostrar_tela_login()
else:
    st.success("Logado! Clique no botão para sair se quiser testar a tela novamente.")
    if st.button("Sair"):
        st.session_state.logado = False
        st.rerun()
