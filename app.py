import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Crow Tech Elite", layout="wide", initial_sidebar_state="collapsed")

# --- SISTEMA DE LOGIN ---
if 'logado' not in st.session_state:
    st.session_state.logado = False

def tela_login():
    st.markdown("""
        <style>
        .login-box {
            background-color: #161b22;
            padding: 40px;
            border-radius: 15px;
            border: 1px solid #30363d;
            text-align: center;
            max-width: 400px;
            margin: auto;
        }
        .stApp { background-color: #0e1117; }
        </style>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("assets/logo.png", width=150)
        st.markdown("<h1 style='text-align: center;'>CROW TECH</h1>", unsafe_allow_html=True)
        with st.form("login"):
            usuario = st.text_input("Usuário")
            senha = st.text_input("Senha", type="password")
            entrar = st.form_submit_button("ACESSAR SISTEMA", use_container_width=True)
            
            if entrar:
                if usuario == "admin" and senha == "crow123": # Altere aqui
                    st.session_state.logado = True
                    st.rerun()
                else:
                    st.error("Credenciais inválidas")
        st.caption("Esqueceu a senha? Entre em contato com o suporte AXIO.")

# --- DASHBOARD PRINCIPAL ---
def dashboard():
    # CSS para matar fundos brancos e estilizar o dashboard
    st.markdown("""
        <style>
        /* Fundo dos campos de seleção e menus */
        div[data-baseweb="select"] > div, div[data-baseweb="input"] > div, .stMultiSelect div {
            background-color: #1c2128 !important;
            color: white !important;
            border: 1px solid #30363d !important;
        }
        .stApp { background-color: #0e1117; color: white; }
        [data-testid="stHeader"] { background: rgba(0,0,0,0); }
        .stTabs [data-baseweb="tab-list"] { background-color: #161b22; border-radius: 10px; padding: 5px; }
        </style>
    """, unsafe_allow_html=True)

    # --- BARRA SUPERIOR DE ATIVOS ---
    st.markdown("### 📊 Terminal de Operações")
    pares_disponiveis = ["SOLUSDT", "BTCUSDT", "ETHUSDT", "XRPUSDT", "DOGEUSDT"]
    escolha = st.tabs(pares_disponiveis) # Transforma os pares em abas superiores

    for i, aba in enumerate(escolha):
        with aba:
            par_atual = pares_disponiveis[i]
            
            # --- COLUNAS: GRÁFICO VS MÉTRICAS ---
            col_grafico, col_dados = st.columns([3, 1])
            
            with col_grafico:
                # Integração Real do TradingView
                embed_code = f"""
                <iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_76d4d&symbol=BITGET%3A{par_atual}&interval=5&hidesidetoolbar=1&symboledit=1&saveimage=1&toolbarbg=f1f3f6&studies=[]&theme=dark&style=1&timezone=Etc%2FUTC&studies_overrides=%7B%7D&overrides=%7B%7D&enabled_features=%5B%5D&disabled_features=%5B%5D&locale=br&utm_source=localhost&utm_medium=widget&utm_campaign=chart&utm_term=BITGET%3A{par_atual}" 
                width="100%" height="500" frameborder="0" allowfullscreen></iframe>
                """
                components.html(embed_code, height=500)

            with col_dados:
                st.metric("PREÇO ATUAL", "Analisando...", delta="RSI: --")
                st.markdown("---")
                st.write("**Gatilhos Sniper:**")
                st.caption("✅ EMA 20 Alinhada")
                st.caption("⏳ Aguardando Volatilidade")
                if st.button(f"FORÇAR ENTRADA {par_atual}", key=f"btn_{par_atual}"):
                    st.warning("Comando enviado ao Termux...")

    # Sidebar para Logout e Funções
    with st.sidebar:
        st.image("assets/logo.png", width=100)
        if st.button("SAIR (LOGOUT)"):
            st.session_state.logado = False
            st.rerun()

# --- LÓGICA DE NAVEGAÇÃO ---
if not st.session_state.logado:
    tela_login()
else:
    dashboard()
