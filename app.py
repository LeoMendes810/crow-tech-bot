import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import streamlit.components.v1 as components
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Crow Tech Elite", layout="wide", initial_sidebar_state="expanded")

# --- CSS INTEGRADO: LOGO NO FUNDO, TÍTULOS E EXTERMÍNIO DO BRANCO ---
st.markdown("""
    <style>
    /* 1. Logo ao Fundo (Restaurado) */
    .stApp {
        background-color: #0e1117;
        background-image: linear-gradient(rgba(14, 17, 23, 0.85), rgba(14, 17, 23, 0.85)), 
                          url("https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/logo.png");
        background-attachment: fixed;
        background-size: 35%; background-repeat: no-repeat; background-position: center;
        color: white;
    }

    /* 2. Matar fundos brancos em submenus e inputs (Sidebar e Main) */
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div, .stMultiSelect div {
        background-color: #1c2128 !important;
        color: white !important;
        border: 1px solid #30363d !important;
    }
    
    /* 3. Títulos, Rótulos e Legendas Visíveis */
    h1, h2, h3, p, span, label { color: white !important; }
    .stMetric label { color: #8b949e !important; font-size: 1rem !important; }
    
    /* 4. Esconder apenas a barra superior 'Manage App' sem quebrar o layout */
    header { background: rgba(0,0,0,0) !important; }
    [data-testid="stHeader"] { background-color: rgba(0,0,0,0) !important; }

    /* Login Container */
    .login-box {
        background-color: #161b22;
        padding: 40px;
        border-radius: 15px;
        border: 1px solid #30363d;
        margin: auto;
        max-width: 450px;
    }
    </style>
""", unsafe_allow_html=True)

# --- CONTROLE DE ACESSO ---
if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- TELA DE LOGIN (ACRESCENTADA) ---
def tela_login():
    _, col2, _ = st.columns([1, 1.5, 1])
    with col2:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.image("https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/logo.png", width=120)
        st.markdown("<h2 style='text-align: center;'>Acesso Crow Tech</h2>", unsafe_allow_html=True)
        with st.form("login"):
            u = st.text_input("Usuário")
            p = st.text_input("Senha", type="password")
            if st.form_submit_button("ENTRAR NO SISTEMA", use_container_width=True):
                if u == "admin" and p == "crow123":
                    st.session_state.logado = True
                    st.rerun()
                else: st.error("Incorreto.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARD COMPLETO (RESTAURADO) ---
def dashboard():
    # --- MENU LATERAL (RESTAURADO) ---
    with st.sidebar:
        st.image("https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/logo.png", width=100)
        st.markdown("### 🖥️ PAINEL DE CONTROLE")
        
        with st.expander("🔄 GESTÃO DE PARES", expanded=True):
            lista = ['SOL/USDT', 'BTC/USDT', 'ETH/USDT', 'XRP/USDT', 'DOGE/USDT', 'LINK/USDT']
            selecionados = st.multiselect("Selecione (Min. 4):", lista, default=['SOL/USDT', 'BTC/USDT', 'ETH/USDT', 'XRP/USDT'])
        
        with st.expander("💰 FINANCEIRO"):
            st.write("Saldo: $ 15.94")
            st.button("Sacar Lucro", use_container_width=True)

        st.divider()
        if st.button("SAIR (LOGOUT)"):
            st.session_state.logado = False
            st.rerun()

    # --- CORPO DO DASHBOARD ---
    st.markdown("<h1>CROW <span style='color:#0ea5e9;'>TECH</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-style: italic; margin-top: -20px;'>Seu estilo em jogo</p>", unsafe_allow_html=True)

    # Métricas com Rótulos
    c1, c2, c3, c4 = st.columns([1,1,1,1.5])
    with c1: st.metric("SALDO", "$ 15.94", delta="Real")
    with c2: st.metric("LUCRO HOJE", "+1.20%", delta="0.80% Alvo")
    with c3: st.metric("STATUS", "SNIPER ON", delta="C18.9.1.5")
    
    with c4:
        # Gráfico de Rosca com Legendas (Restaurado)
        fig = go.Figure(data=[go.Pie(labels=['Lucro', 'Banca', 'Ordem'], 
                             values=[1.2, 14.74, 0], hole=.6,
                             marker=dict(colors=['#0ea5e9', '#1c2128', '#30363d']))])
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), height=130, showlegend=True, 
                          legend=dict(font=dict(color="white")), paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # --- TERMINAL GRÁFICO E RADAR ---
    st.markdown("### 📡 Terminal de Operações")
    escolha = st.tabs(selecionados)

    for i, aba in enumerate(escolha):
        with aba:
            col_g, col_r = st.columns([2.5, 1.2])
            par_limpo = selecionados[i].replace("/", "")
            
            with col_g:
                # Gráfico Real TradingView
                tv = f"https://s.tradingview.com/widgetembed/?symbol=BITGET%3A{par_limpo}&interval=5&theme=dark"
                components.html(f'<iframe src="{tv}" width="100%" height="450" frameborder="0"></iframe>', height=450)
            
            with col_r:
                # Radar Sniper (A Lista de Moedas)
                st.markdown(f"**Análise {selecionados[i]}**")
                radar_df = pd.DataFrame({
                    "Ativo": selecionados,
                    "RSI": [42.2, 50.2, 46.0, 67.1, 48.5, 51.0][:len(selecionados)],
                    "Trend": ["BAIXA", "BAIXA", "BAIXA", "ALTA", "BAIXA", "ALTA"][:len(selecionados)]
                })
                st.table(radar_df)
                st.button(f"Ativar Sniper {par_limpo}", use_container_width=True)

# Navegação
if not st.session_state.logado:
    tela_login()
else:
    dashboard()
