import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import streamlit.components.v1 as components
import os

# --- CONFIGURAÇÃO DA PÁGINA (ESCONDER MENU PADRÃO E FORÇAR DARK) ---
st.set_page_config(page_title="Crow Tech Elite", layout="wide", initial_sidebar_state="expanded")

# --- CSS DEFINITIVO: CONTRASTE, EXTERMÍNIO DO BRANCO E TOPO LIMPO ---
st.markdown("""
    <style>
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp { background-color: #0e1117; color: white; }
    
    /* Matar fundo branco de submenus, inputs e multiselect */
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div, .stMultiSelect div {
        background-color: #1c2128 !important;
        color: white !important;
        border: 1px solid #30363d !important;
    }
    
    /* Estilização da Tela de Login */
    .login-container {
        background-color: #161b22;
        padding: 40px;
        border-radius: 15px;
        border: 1px solid #30363d;
        text-align: center;
        max-width: 450px;
        margin: auto;
    }

    /* Labels e Textos Claros */
    label, p, span { color: #ffffff !important; font-weight: 500; }
    .titulo-main { font-size: 3.5rem !important; font-weight: 800; color: white; line-height: 1; }
    </style>
""", unsafe_allow_html=True)

# --- CONTROLE DE SESSÃO ---
if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- 1. TELA DE LOGIN (ACRESCENTADA) ---
def tela_login():
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.image("https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/logo.png", width=120)
        st.markdown("<h2 style='color: #0ea5e9;'>Crow Tech Elite</h2>", unsafe_allow_html=True)
        with st.form("login_form"):
            user = st.text_input("Usuário")
            password = st.text_input("Senha", type="password")
            if st.form_submit_button("ACESSAR DASHBOARD", use_container_width=True):
                if user == "admin" and password == "crow123":
                    st.session_state.logado = True
                    st.rerun()
                else: st.error("Acesso Negado.")
        
        c_l1, c_l2 = st.columns(2)
        with c_l1: st.button("Cadastrar", key="cad", use_container_width=True)
        with c_l2: st.button("Recuperar Senha", key="rec", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- 2. DASHBOARD (ESTRUTURA ORIGINAL RESTAURADA + ACRÉSCIMOS) ---
def dashboard():
    # --- SIDEBAR ORIGINAL ---
    with st.sidebar:
        st.image("https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/logo.png", width=100)
        st.markdown("### ⚡ COMANDO CENTRAL")
        with st.expander("🔄 GESTÃO DE PARES", expanded=True):
            lista_pares = ['SOL/USDT', 'BTC/USDT', 'ETH/USDT', 'XRP/USDT', 'DOGE/USDT', 'LINK/USDT']
            selecionados = st.multiselect("Pares Ativos:", lista_pares, default=['SOL/USDT', 'BTC/USDT', 'ETH/USDT', 'XRP/USDT'])
        
        with st.expander("💰 FINANCEIRO"):
            st.metric("Saldo Atual", "$ 15.94")
            st.button("Sincronizar Carteira", use_container_width=True)
        
        st.divider()
        if st.button("LOGOUT (SAIR)"):
            st.session_state.logado = False
            st.rerun()

    # --- CABEÇALHO ---
    st.markdown("<h1 class='titulo-main'>CROW <span style='color:#0ea5e9;'>TECH</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-style: italic; color: #8b949e;'>Seu estilo em jogo</p>", unsafe_allow_html=True)

    # --- MÉTRICAS E GRÁFICO DE ROSCA (RESTAURADOS) ---
    col_m1, col_m2, col_m3, col_m4 = st.columns([1,1,1,1.5])
    with col_m1: st.metric("SALDO", "$ 15.94", delta="Real")
    with col_m2: st.metric("LUCRO HOJE", "+1.20%", delta="0.80% Alvo")
    with col_m3: st.metric("STATUS", "SNIPER ON", delta="C18.9.1.5")
    
    with col_m4:
        # Gráfico de Rosca (Performance da Carteira)
        fig = go.Figure(data=[go.Pie(labels=['Lucro', 'Banca', 'Em Ordem'], 
                             values=[1.2, 14.74, 0], hole=.6,
                             marker=dict(colors=['#0ea5e9', '#1c2128', '#30363d']))])
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), height=150, showlegend=False, paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # --- BARRA DE GRÁFICOS EM TEMPO REAL (ACRESCENTADA) ---
    st.subheader("📡 Terminal Gráfico")
    tabs_pares = [p.replace("/", "") for p in selecionados]
    escolha_abas = st.tabs(selecionados)

    for i, aba in enumerate(escolha_abas):
        with aba:
            col_chart, col_radar = st.columns([2.5, 1])
            with col_chart:
                # Iframe TradingView
                tv_url = f"https://s.tradingview.com/widgetembed/?symbol=BITGET%3A{tabs_pares[i]}&interval=5&theme=dark"
                components.html(f'<iframe src="{tv_url}" width="100%" height="450" frameborder="0"></iframe>', height=450)
            
            with col_radar:
                # Radar de Ativos (Lista de Moedas que você pediu para manter)
                st.markdown("**Radar Crow Sniper**")
                df_radar = pd.DataFrame({
                    "Ativo": selecionados,
                    "RSI": [42.2, 50.2, 46.0, 67.1, 52.0, 48.0][:len(selecionados)],
                    "Tendência": ["BAIXA", "BAIXA", "BAIXA", "ALTA", "ESTÁVEL", "BAIXA"][:len(selecionados)]
                })
                st.table(df_radar)
                st.button(f"Ativar Sniper {selecionados[i]}", use_container_width=True)

# --- LÓGICA DE NAVEGAÇÃO ---
if not st.session_state.logado:
    tela_login()
else:
    dashboard()
