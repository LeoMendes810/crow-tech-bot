import streamlit as st

# 1. Configuração da página (Deve ser a primeira linha)
st.set_page_config(page_title="Crow Tech Elite", layout="wide")

if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- CSS PERSONALIZADO ---
st.markdown("""
    <style>
    /* Remover cabeçalho padrão e barra branca */
    header { visibility: hidden; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0) !important; }
    
    /* 1. Remover o quadrado circulado (Borda do Form) */
    [data-testid="stForm"] { border: none !important; padding: 0 !important; }

    /* 6. Logo secundário Marca d'água (Só o corvo, maior e centralizado) */
    .stApp {
        background-color: #0e1117;
        background-image: linear-gradient(rgba(14, 17, 23, 0.88), rgba(14, 17, 23, 0.88)), 
                          url("https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/corvo_bg.png");
        background-size: 60%; background-repeat: no-repeat; background-position: center;
    }

    /* Posicionamento do container de login na esquerda */
    .login-container {
        max-width: 450px;
        margin-left: 8%; 
        margin-top: 5%;
        text-align: left;
    }

    /* 3. Slogan correto e estilizado */
    .slogan { 
        color: #8b949e; 
        font-style: italic; 
        font-size: 1.2rem; 
        margin-top: -15px; 
        margin-bottom: 40px; 
        font-weight: 400;
    }

    /* Labels dos campos em branco puro */
    label { color: #ffffff !important; font-weight: bold !important; font-size: 1rem !important; }

    /* 4. Botão ACESSAR (Menor, sem fundo, estilo borda) */
    .stButton > button {
        background-color: transparent !important;
        color: #0ea5e9 !important;
        border: 1px solid #0ea5e9 !important;
        border-radius: 5px !important;
        padding: 5px 30px !important;
        font-size: 0.9rem !important;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: rgba(14, 165, 233, 0.1) !important;
        border-color: #ffffff !important;
        color: #ffffff !important;
    }

    /* Estilo dos campos de texto */
    div[data-baseweb="input"] { background-color: #161b22 !important; border: 1px solid #30363d !important; border-radius: 8px; }
    input { color: #ffffff !important; }

    /* Links de rodapé discretos */
    .footer-links button {
        background: none !important;
        border: none !important;
        padding: 0 !important;
        color: #57606a !important;
        text-decoration: none !important;
        font-size: 0.85rem !important;
    }
    </style>
""", unsafe_allow_html=True)

def mostrar_tela_login():
    # Divisão para o conteúdo ficar na esquerda
    col_content, col_empty = st.columns([1, 1.2])
    
    with col_content:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        
        # 5. Logo Principal (Esquerda e Maior)
        st.image("https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/logo.png", width=320)
        
        # 3. Slogan corrigido
        st.markdown('<p class="slogan">Inteligência em cada movimento</p>', unsafe_allow_html=True)

        # 2. Removido a frase "Entrar" (Iniciando campos direto)
        usuario = st.text_input("USUÁRIO", key="input_user")
        senha = st.text_input("SENHA", type="password", key="input_pass")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # 4. Botão menor e customizado
        if st.button("ENTRAR"):
            if usuario == "admin" and senha == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Credenciais incorretas.")

        # Links de apoio
        st.markdown("<br><br>", unsafe_allow_html=True)
        c1, c2 = st.columns([1, 1])
        with c1:
            if st.button("Criar conta", key="link_cad"): pass
        with c2:
            if st.button("Esqueci a senha", key="link_pass"): pass
            
        st.markdown('</div>', unsafe_allow_html=True)

# Lógica de Navegação
if not st.session_state.logado:
    mostrar_tela_login()
else:
    # Quando logar, ele limpa a tela e mostra o Dashboard
    st.write("### Bem-vindo ao Dashboard Crow Tech")
    if st.button("Sair"):
        st.session_state.logado = False
        st.rerun()
