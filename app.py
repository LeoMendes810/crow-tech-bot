import streamlit as st
import base64
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 1. Configurações de Elite
st.set_page_config(page_title="Crow Tech Elite C18.9.1.5", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

# --- CSS DASHBOARD (C18.9.1.5) ---
st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 40% !important;
        background-attachment: fixed !important;
    }}

    /* Estilização dos Cards de Dados */
    .metric-card {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
    }}
    
    .stTabs [data-baseweb="tab-list"] {{
        gap: 24px;
        background-color: transparent;
    }}

    .stTabs [data-baseweb="tab"] {{
        height: 50px;
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 10px 10px 0px 0px;
        color: white;
        font-weight: bold;
    }}
    </style>
""", unsafe_allow_html=True)

# Lógica de Sessão
if 'logado' not in st.session_state: st.session_state.logado = False

# --- TELA DE LOGIN (ESTÁTICA E SALVA) ---
if not st.session_state.logado:
    # (O código de login que travamos anteriormente vai aqui...)
    # Por brevidade, vou focar no Dashboard, mas mantenha sua função de login ativa
    with st.form("login_crow"):
        st.markdown(f'<div style="text-align:center"><img src="data:image/png;base64,{logo_base64}" width="160"></div>', unsafe_allow_html=True)
        u = st.text_input("USUÁRIO")
        p = st.text_input("SENHA", type="password")
        if st.form_submit_button("ACESSAR C18.9.1.5"):
            if u == "admin" and p == "crow123":
                st.session_state.logado = True
                st.rerun()

# --- INTERFACE DO BOT (SURPRESA C18.9.1.5) ---
else:
    # Header do Sistema
    col_logo, col_v, col_status = st.columns([1, 4, 1])
    with col_logo:
        st.image(f"data:image/png;base64,{logo_base64}", width=120)
    with col_v:
        st.markdown(f"<h2 style='color:#00bcd4; margin-top:10px;'>SISTEMA CROW TECH <span style='color:white; font-size:14px;'>v.C18.9.1.5</span></h2>", unsafe_allow_html=True)
    with col_status:
        if st.button("🔴 DESCONECTAR"):
            st.session_state.logado = False
            st.rerun()

    st.markdown("---")

    # Layout Principal: 3 Colunas
    col1, col2, col3 = st.columns([1.5, 3, 1.5])

    # --- COLUNA 1: ATIVOS E PERFORMANCE ---
    with col1:
        st.markdown("### 📊 Ativos em Monitoramento")
        ativos = pd.DataFrame({
            'Par': ['BTC/USDT', 'ETH/USDT', 'SOL/USDT', 'BNB/USDT'],
            'Sinal': ['COMPRA', 'AGUARDAR', 'VENDA', 'COMPRA'],
            'Força': ['88%', '45%', '92%', '76%']
        })
        st.table(ativos)

        st.markdown("### 🍩 Alocação de Carteira")
        # Gráfico de Rosca (Donut)
        fig_donut = go.Figure(data=[go.Pie(labels=['BTC', 'ETH', 'SOL', 'Stable'], 
                             values=[4500, 2500, 1500, 1500], hole=.6)])
        fig_donut.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0), 
                                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig_donut.update_traces(marker=dict(colors=['#00bcd4', '#004d4d', '#008b8b', '#1a1a1a']))
        st.plotly_chart(fig_donut, use_container_width=True)

    # --- COLUNA 2: GRÁFICO AO VIVO E INDICADORES ---
    with col2:
        st.markdown("### 📈 Gráfico em Tempo Real (RSI / EMA)")
        
        # Gerando dados fictícios para o gráfico
        df = pd.DataFrame({
            'Date': pd.date_range(start='2026-01-01', periods=100, freq='H'),
            'Close': np.random.normal(50000, 1500, 100).cumsum()
        })
        df['EMA_20'] = df['Close'].ewm(span=20).mean()
        df['EMA_50'] = df['Close'].ewm(span=50).mean()

        fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03, row_heights=[0.7, 0.3])
        
        # Velas/Linha de Preço e EMAs
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], name='Preço', line=dict(color='#00bcd4', width=2)), row=1, col=1)
        fig.add_trace(go.Scatter(x=df['Date'], y=df['EMA_20'], name='EMA 20', line=dict(color='white', width=1, dash='dot')), row=1, col=1)
        
        # RSI Simulado
        fig.add_trace(go.Bar(x=df['Date'], y=np.random.randint(30, 70, 100), name='RSI', marker_color='#004d4d'), row=2, col=1)
        
        fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
                          margin=dict(t=20, b=20), height=500, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    # --- COLUNA 3: LOGS E OPERAÇÕES ---
    with col3:
        st.markdown("### 🛡️ Operações Recentes")
        for i in range(5):
            st.info(f"🟢 BUY Order: {np.random.choice(['BTC', 'SOL'])} | Profit: +{np.random.uniform(1,5):.2f}%")
        
        st.markdown("### ⚙️ Parâmetros C18")
        st.slider("Agressividade do RSI", 0, 100, 70)
        st.checkbox("Trailing Stop Ativo", value=True)
        st.button("⚡ EXECUÇÃO FORÇADA", use_container_width=True)

    # Rodapé Técnico
    st.markdown(f"""
        <div style="text-align: center; color: rgba(255,255,255,0.2); font-size: 10px; margin-top: 50px;">
            SISTEMA CROW TECH ELITE // ENCRYPTED CONNECTION // LATENCY: 14ms // {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}
        </div>
    """, unsafe_allow_html=True)
