def tela_login():
    # CSS específico para a Tela de Login (Alta visibilidade)
    st.markdown("""
        <style>
        /* Esconder tudo que for do Streamlit nesta tela */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Centralizar o formulário na tela */
        .main {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .login-card {
            background-color: #161b22;
            padding: 2.5rem;
            border-radius: 20px;
            border: 1px solid #30363d;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
            text-align: center;
        }

        /* Clarear os Labels dos campos */
        .stTextInput label {
            color: #ffffff !important;
            font-size: 1.1rem !important;
            font-weight: bold !important;
            margin-bottom: 10px;
        }

        /* Ajustar os botões de link */
        .link-buttons {
            margin-top: 15px;
            display: flex;
            justify-content: space-between;
        }
        
        /* Texto de boas vindas */
        .welcome-text {
            color: #8b949e;
            margin-bottom: 2rem;
            font-size: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Layout da tela de Login
    _, col_center, _ = st.columns([1, 1.2, 1])
    
    with col_center:
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        
        # Logo da Crow Tech
        st.image("https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/logo.png", width=130)
        
        st.markdown("<h1 style='color: white; margin-bottom: 5px;'>Entrar</h1>", unsafe_allow_html=True)
        st.markdown("<p class='welcome-text'>Seu estilo em jogo. Entre com suas credenciais.</p>", unsafe_allow_html=True)
        
        # Formulário de Login
        with st.form("login_form", clear_on_submit=False):
            usuario = st.text_input("USUÁRIO")
            senha = st.text_input("SENHA", type="password")
            
            # Botão de Acesso Estilizado
            botao_entrar = st.form_submit_button("ACESSAR DASHBOARD", use_container_width=True)
            
            if botao_entrar:
                if usuario == "admin" and senha == "crow123":
                    st.session_state.logado = True
                    st.success("Acesso autorizado! Carregando...")
                    st.rerun()
                else:
                    st.error("Usuário ou senha incorretos.")

        # Links de Suporte (Fora do form para não dar conflito)
        st.write("") 
        c_cad, c_pass = st.columns(2)
        with c_cad:
            if st.button("Criar Conta", use_container_width=True, key="cad"):
                st.toast("Redirecionando para cadastro...")
        with c_pass:
            if st.button("Esqueci Senha", use_container_width=True, key="pass"):
                st.toast("Iniciando recuperação via E-mail...")
        
        st.markdown('</div>', unsafe_allow_html=True)
