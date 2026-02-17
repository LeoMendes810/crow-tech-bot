import streamlit as st
import ccxt
import pandas as pd
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh
import os

# CONFIGURAÇÃO DE PÁGINA (Barra lateral agora inicia ABERTA)
st.set_page_config(page_title="Crow Tech Elite", layout="wide", initial_sidebar_state="expanded")
st_autorefresh(interval=30000, key="datarefresh")

# --- ESTILO CROW TECH ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        background-image: linear-gradient(rgba(14, 17, 23, 0.92), rgba(14, 17, 23, 0.92)), 
                          url("https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/logo.png");
        background-attachment: fixed;
        background-size: 50%;
        background-repeat: no-repeat;
        background-position: center;
    }
    [data-testid="stSidebar"] { background-color: #1c2128 !important; border-right: 1px solid #30363d; }
    [data-testid="stMetric"] { background-color: rgba(28, 33, 40, 0.95) !important; border-radius: 15px; padding: 25px !important; }
    .titulo-main { font-size: 4.5rem !important; font-weight: 800; margin-bottom: -10px; line-height: 1; color: white; }
    .slogan-main { font-size: 1.8rem !important; color: #8b949e !important; font-style: italic; margin-top: 0; }
    h1, h2, h3, p, span, label { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: O MENU QUE VOCÊ PROCURAVA ---
with st.sidebar:
    st.image("assets/logo.png", width=120)
    st.markdown("## 📟 Terminal Crow Tech")
    
    # SEÇÃO 1: GESTÃO DE PARES (Mínimo 6, inicia com os 4 fixos)
    with st.expander("🔄 Gestão de Pares", expanded=True):
        lista_20 = [
            'SOL/USDT', 'BTC/USDT', 'ETH/USDT', 'XRP/USDT', 'DOGE/USDT', 'TRX/USDT',
            'ADA/USDT', 'MATIC/USDT', 'DOT/USDT', 'LINK/USDT', 'AVAX/USDT', 'SHIB/USDT',
            'LTC/USDT', 'BCH/USDT', 'UNI/USDT', 'NEAR/USDT', 'APT/USDT', 'ARB/USDT',
            'TIA/USDT', 'OP/USDT'
        ]
        # Aqui garantimos que os 4 originais já vêm selecionados por defeito
        selecionados = st.multiselect(
            "Selecione os ativos ativos:",
            lista_20,
            default=['SOL/USDT', 'BTC/USDT', 'ETH/USDT', 'XRP/USDT']
        )
        
        if len(selecionados) < 4:
            st.warning("⚠️ Os 4 pares base devem estar ativos para estabilidade.")
        else:
            st.success(f"✅ {len(selecionados)} pares monitorizados.")

    # SEÇÃO 2: FINANCEIRO
    with st.expander("💰 Financeiro"):
        st.button("➕ Adicionar Fundos (Depósito)")
        st.button("➖ Retirar Fundos (Saque)")
        st.caption("Carteira Destino: Não configurada.")

    # SEÇÃO 3: CONFIGURAÇÕES / SEGURANÇA
    with st.expander("⚙️ Configurações"):
        st.subheader("Segurança")
        st.text_input("E-mail para Alertas")
        st.text_input("Alterar Chave de Acesso", type="password")
        st.button("Salvar Preferências")

    st.divider()
    st.caption("Crow Tech Bot v3.3 | Modo Sniper")

# --- CABEÇALHO ---
col_l, col_t = st.columns([1, 5])
with col_l:
    if os.path.exists("assets/logo.png"): st.image("assets/logo.png", width=150)
with col_t:
    st.markdown("<h1 class='titulo-main'>CROW <span style='color:#0ea5e9;'>TECH</span></h1>", unsafe_allow_html=True)
    st.markdown("<p class='slogan-main'>Inteligência em cada movimento</p>", unsafe_allow_html=True)

# --- CORPO DO DASHBOARD ---
st.write("")
m1, m2, m3 = st.columns(3)
with m1: st.metric("SALDO BITGET", "$ 185.50")
with m2: st.metric("RESULTADO", "$ 5.20", delta="Win")
with m3: st.metric("STATUS", "REAL MODE", delta="OPERANDO")

st.divider()
c_radar, c_perf = st.columns([1.6, 1.4])

with c_radar:
    st.subheader("📡 Radar de Ativos")
    if selecionados:
        # Simulação rápida dos dados dos pares escolhidos
        df = pd.DataFrame({
            "Ativo": [p.split('/')[0] for p in selecionados],
            "Preço": ["$ ---" for _ in selecionados],
            "Var 24h": ["---" for _ in selecionados]
        })
        st.table(df)
    else:
        st.info("Utilize o menu lateral para selecionar os pares.")

with c_perf:
    st.subheader("🎯 Performance")
    fig = go.Figure(go.Pie(labels=['Wins', 'Losses'], values=[85, 15], hole=.6, marker_colors=['#00ff00', '#ff4b4b']))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='white', height=350, showlegend=True,
                      legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5, font=dict(size=14, color="white")))
    st.plotly_chart(fig, use_container_width=True)
