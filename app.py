import streamlit as st
import os

# 1. Configuração da página (DEVE ser a primeira linha)
st.set_page_config(page_title="Crow Tech Elite", layout="wide")

# 2. Inicialização do estado de login
if 'logado' not in st.session_state:
    st.session_state.logado = False

# 3. CSS SEGURO (Sem ocultar o corpo da página)
st.markdown("""
    <style>
    /* Fundo escuro e imagem de fundo */
    .stApp {
        background-color: #0e1117;
        background-image: linear-gradient(rgba(14, 17, 23, 0.8), rgba(14, 17, 23, 0.8)), 
                          url("https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/logo.png");
        background-size: 40%; background-repeat: no-repeat; background-position: center;
    }

    /* Card de Login Centralizado */
    .login-box {
        background-color: #161b22;
        padding: 50px;
        border-radius: 20px;
        border: 1px solid #30363d;
        text-align: center;
        max-width: 500px;
        margin: 100px auto; /* Centraliza verticalmente no PC */
        box-shadow: 0px 4px 20px rgba(0,0,0,0.5);
    }

    /* Labels Brancos e Fortes */
    label { color: #ffffff !important; font-size: 1.2rem !important; font-weight: bold; }
    
    /* Inputs Escuros com borda azul */
    div[data-baseweb="input"] {
        background-color: #0d1117 !important;
        border: 1px solid #0ea5e9 !important;
    }
    input { color: white !important; }
    </style>
""", unsafe_allow_html=True)

# --- FUNÇÃO DA TELA INICIAL ---
def mostrar_tela_login():
    # Usamos colunas para centralizar o card no monitor
    _, col_centro, _ = st.columns([1, 1.5, 1])
    
    with col_centro:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        
        # Logo
        st.image("https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/logo.png", width=150)
        
        st.markdown("<h1 style='color: white;'>ENTRAR</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color: #8b949e;'>Seu estilo em jogo</p>", unsafe_allow_html=True)

        # Formulário
        with st.form("login_crow"):
            usuario = st.text_input("USUÁRIO")
            senha = st.text_input("SENHA", type="password")
            
            botao = st.form_submit_button("ACESSAR SISTEMA", use_container_width=True)
            
            if botao:
                if usuario == "admin" and senha == "crow123":
                    st.session_state.logado = True
                    st.rerun()
                else:
                    st.error("Credenciais inválidas.")

        # Links estilo Rede Social
        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Criar conta", use_container_width=True):
                st.info("Falar com suporte.")
        with c2:
            if st.button("Perdi a senha", use_container_width=True):
                st.warning("Recuperação ativa.")
        
        st.markdown('</div>', unsafe_allow_html=True)

# --- LÓGICA PRINCIPAL ---
if not st.session_state.logado:
    mostrar_tela_login()
else:
    st.write("# Dashboard Crow Tech")
    st.write("Parabéns, você entrou! Agora podemos construir o resto aqui.")
    if st.button("Sair"):
        st.session_state.logado = False
        st.rerun()
