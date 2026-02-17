def tela_login():
    # CSS focado em entregar conteúdo e garantir contraste
    st.markdown("""
        <style>
        /* 1. Limpeza do topo sem esconder o corpo (Evita tela branca) */
        [data-testid="stHeader"] { background: rgba(0,0,0,0) !important; }
        footer {visibility: hidden;}
        
        /* 2. Fundo Escuro para toda a página */
        .stApp { background-color: #0e1117 !important; }

        /* 3. Centralização e Estilo do Card de Login */
        .login-card {
            background-color: #161b22;
            padding: 3rem;
            border-radius: 15px;
            border: 2px solid #30363d;
            text-align: center;
            margin-top: 10%;
        }

        /* 4. CONTRASTE: Títulos e Labels em Branco Puro */
        h1, h2, h3, p, span { color: #ffffff !important; }
        
        .stTextInput label {
            color: #ffffff !important; /* Branco forte para os nomes Usuário/Senha */
            font-size: 1.2rem !important;
            font-weight: 700 !important;
            text-transform: uppercase;
        }

        /* 5. Ajuste dos inputs para não ficarem apagados */
        div[data-baseweb="input"] {
            background-color: #1c2128 !important;
            border: 1px solid #0ea5e9 !important; /* Borda Ciano para destaque */
        }
        
        input { color: white !important; }

        /* 6. Botão de Links (Cadastro/Senha) */
        .stButton button {
            background-color: transparent;
            color: #0ea5e9 !important;
            border: none;
            text-decoration: underline;
        }
        </style>
    """, unsafe_allow_html=True)

    # Organização Visual
    _, col_login, _ = st.columns([1, 1.5, 1])
    
    with col_login:
        st.markdown('<div class="login-card">', unsafe_allow_html=True)
        
        # Logo da Crow Tech
        st.image("https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/logo.png", width=140)
        
        st.markdown("<h2 style='margin-bottom: 25px;'>ACESSO RESTRITO</h2>", unsafe_allow_html=True)
        
        with st.form("form_acesso"):
            # Campos com Labels em negrito e branco
            user = st.text_input("Usuário")
            password = st.text_input("Senha", type="password")
            
            # Botão Principal
            if st.form_submit_button("ENTRAR NO DASHBOARD", use_container_width=True):
                if user == "admin" and password == "crow123":
                    st.session_state.logado = True
                    st.rerun()
                else:
                    st.error("Credenciais Inválidas")
        
        # Links de Apoio estilo "Instagram/Facebook"
        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Criar Conta", key="btn_cad"):
                st.info("Entre em contato com o suporte AXIO/Crow Tech.")
        with c2:
            if st.button("Esqueci a Senha", key="btn_pass"):
                st.warning("Sistema de recuperação em manutenção.")
        
        st.markdown('</div>', unsafe_allow_html=True)
