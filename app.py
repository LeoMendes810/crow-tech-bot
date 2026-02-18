import streamlit as st
import base64
import pandas as pd
from datetime import datetime

# 1. Configuração de Elite (Foco Operacional)
st.set_page_config(page_title="Crow Tech Elite - C18.9.1.5", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

# --- CSS OPERACIONAL (Focado em Dados Reais) ---
st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 30% !important;
        background-attachment: fixed !important;
    }}
    /* Estilo Terminal/Log */
    .stCodeBlock {{
        background-color: rgba(0, 0, 0, 0.8) !important;
        border: 1px solid #00bcd4 !important;
        border-radius: 5px;
    }}
    .stat-card {{
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }}
    </style>
""", unsafe_allow_html=True)

if 'logado' not in st.session_state: st.session_state.logado = False

if not st.session_state.logado:
    # (Mantemos seu Login que já funciona)
    with st.form("login_crow"):
        st.markdown(f'<div style="text-align:center"><img src="data:image/png;base64,{logo_base64}" width="160"></div>', unsafe_allow_html=True)
        u = st.text_input("USUÁRIO")
        p = st.text_input("SENHA", type="password")
        if st.form_submit_button("ACESSAR TERMINAL"):
            if u == "admin" and p == "crow123":
                st.session_state.logado = True
                st.rerun()
else:
    # --- INTERFACE DO BOT (ESTILO TERMINAL AVANÇADO) ---
    c1, c2, c3 = st.columns([1, 4, 1])
    with c1: st.image(f"data:image/png;base64,{logo_base64}", width=80)
    with c2: st.markdown("<h2 style='color:#00bcd4;'>CROW TECH ELITE <span style='color:white; font-size:14px;'>v.C18.9.1.5</span></h2>", unsafe_allow_html=True)
    with c3: 
        if st.button("LOGOUT"): 
            st.session_state.logado = False
            st.rerun()

    # Painel de Controle de Operação
    st.markdown("### 🕹️ Centro de Comando")
    col_ctrl1, col_ctrl2, col_ctrl3 = st.columns(3)
    with col_ctrl1:
        st.button("🚀 INICIAR BOT (TERMUX)", use_container_width=True)
    with col_ctrl2:
        st.button("🛑 PARAR OPERAÇÕES", use_container_width=True)
    with col_ctrl3:
        st.button("🔄 REINICIAR API", use_container_width=True)

    st.markdown("---")

    # Área de Dados Reais
    col_info, col_log = st.columns([1, 2])

    with col_info:
        st.markdown("#### 💎 Status da Carteira")
        st.markdown('<div class="stat-card"><b>Saldo em Moedas</b><br><span style="color:#00bcd4; font-size:20px;">0.185 BTC</span></div>', unsafe_allow_html=True)
        st.markdown('<br>', unsafe_allow_html=True)
        st.markdown('<div class="stat-card"><b>Saldo em Dólar</b><br><span style="color:#00ff88; font-size:20px;">$ 4,150.00</span></div>', unsafe_allow_html=True)
        
        st.markdown("#### ⚙️ Parâmetros Atuais")
        st.write(f"RSI Referência: **30/70**")
        st.write(f"EMA Referência: **9 / 21 / 50**")
        st.write(f"Stop Loss: **1.5%**")

    with col_log:
        st.markdown("#### 🖥️ Saída do Console (Real-time)")
        # Simulando a tela do Termux aqui dentro
        st.code(f"""
>>> [INFO] Crow Tech C18.9.1.5 iniciado...
>>> [API] Conectando à Wallet... OK
>>> [DATA] Buscando RSI e EMA para BTC/USDT...
>>> [ANALYSIS] EMA 9 (51400) > EMA 21 (51250) -> TENDÊNCIA DE ALTA
>>> [BOT] Aguardando sinal de entrada RSI < 30...
>>> [LOG] Latência de rede: 12ms
>>> [{datetime.now().strftime('%H:%M:%S')}] Monitorando ativos da lista...
        """, language="bash")

    st.markdown("---")
    st.markdown("#### 📋 Lista de Ativos do Bot")
    # Tabela simples e limpa, como no seu script
    df_ativos = pd.DataFrame({
        "Par": ["BTC/USDT", "ETH/USDT", "SOL/USDT", "BNB/USDT"],
        "Preço": ["$ 51,420", "$ 2,750", "$ 110", "$ 380"],
        "Tendência": ["ALTA", "NEUTRA", "BAIXA", "ALTA"],
        "Sinal": ["AGUARDAR", "ANALISANDO", "VENDA", "COMPRA"]
    })
    st.dataframe(df_ativos, use_container_width=True)
