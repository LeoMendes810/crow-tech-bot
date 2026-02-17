import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Crow Tech Elite", layout="wide")

if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- CSS PERSONALIZADO ---
st.markdown("""
    <style>
    /* Remover bordas de formulários e cabeçalhos */
    [data-testid="stForm"] { border: none !important; padding: 0 !important; }
    header { visibility: hidden; }
    
    /* 6. Logo Marca d'água (Só o Corvo, maior e centralizado) */
    .stApp {
        background-color: #0e1117;
        background-image: linear-gradient(rgba(14, 17, 23, 0.85), rgba(14, 17, 23, 0.85)), 
                          url("https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/corvo_bg.png");
        background-size: 50%; background-repeat: no-repeat; background-position: center;
    }

    /* Card de Login */
    .login-container {
        max-width: 400px;
        margin-left: 10%; /* Ajuste para o PC */
        margin-top: 5%;
        text-align: left;
    }

    /* 4. Botão Acessar (Menor, Sem Fundo, Estilo Link) */
    .stButton > button {
        background-color: transparent !important;
        color: #0ea5e9 !important;
        border: 1px solid #0ea5e9 !important;
        padding: 5px 20px !important;
        font-weight: bold !important;
        width: auto !important;
    }
    .stButton > button:hover {
        background-color: rgba(14, 165, 233, 0.1) !important;
        color: white !important;
    }

    /* Labels e Inputs */
    label { color: white !important; font-weight: bold !important; }
    div[data-baseweb="input"] { background-color: #161b22 !important; border: 1px solid #30363d !important; }
    input { color: white !important; }
    
    /* 3. Slogan Correto */
    .slogan { color: #8b949e; font-style: italic; font-size: 1.1rem; margin-top: -10px; margin-bottom: 30px; }
    </style>
""", unsafe_allow_html=True)

def mostrar_tela_login():
    col1, col2 = st.columns([1, 1]) # Divide a tela para o logo ficar na esquerda
    
    with col1:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        
        # 5. Logo Principal (Esquerda e Maior)
        st.image("assets/logo.png", width=250)
        
        # 3. Slogan sem ponto de interrogação
        st.markdown('<p class="slogan">Seu estilo em jogo</p>', unsafe_allow_html=True)

        # Campos de Login (Sem o quadrado do Form)
        usuario = st.text_input("USUÁRIO", key="user")
        senha = st.text_input("SENHA", type="password", key="pass")
        
        # 4. Botão Menor e Sem Fundo
        if st.button("ACESSAR"):
            if usuario == "admin" and senha == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Credenciais inválidas.")

        st.markdown("<br>", unsafe_allow_html=True)
        
        # Links de Cadastro/Senha
        c1, c2 = st.columns([1, 1])
        with c1:
            if st.button("Criar conta", key="cad"): pass
        with c2:
            if st.button("Perdi a senha", key="p_pass"): pass
            
        st.markdown('</div>', unsafe_allow_html=True)

# Lógica
if not st.session_state.logado:
    mostrar_tela_login()
else:
    st.write("Logado!")
