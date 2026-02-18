import streamlit as st
import base64
import pandas as pd
import plotly.graph_objects as go

# 1. Configuração da página
st.set_page_config(page_title="Crow Tech Elite C18.9.1.5", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

# --- CSS LIMPO E ORGANIZADO ---
st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 30% !important;
        background-attachment: fixed !important;
    }}

    /* Estilo dos Containers de Vidro */
    .crow-card {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
    }}

    h3 {{
        color: #00bcd4 !important;
        font-size: 16px !important;
        letter-spacing: 1px;
        text-transform: uppercase;
    }}
    </style>
""", unsafe_allow_html=True)

# Lógica de Login (Travada como você pediu)
if 'logado' not in st.session_state:
    st.session_state.logado = False

if not st.session_state.logado:
    # (Mantendo o seu login que já funciona)
    with st.form("login_crow"):
        st.markdown(f'<div style="text-align:center"><img src="data:image/png;base64,{logo_base64}" width="160"></div>', unsafe_allow_html=True)
        u = st.text_input("USUÁRIO")
        p = st.text_input("SENHA", type="password")
        if st.form_submit_button("ACESSAR C18.9.1.5"):
            if u == "admin" and p == "crow123":
                st.session_state.logado = True
                st.rerun()
else:
    # --- DASHBOARD REDESENHADO ---
    
    # Barra Superior (Header)
    c1, c2, c3 = st.columns([1, 3, 1])
    with c1:
        st.image(f"data:image/png;base64,{logo_base64}", width=100)
    with c2:
        st.markdown("<h1 style='text-align:center; color:white; font-size:24px; margin-top:10px;'>PAINEL DE OPERAÇÕES <span style='color:#00bcd4;'>C18.9.1.5</span></h1>", unsafe_allow_html=True)
    with c3:
        if st.button("SAIR", use_container_width=True):
            st.session_state.logado = False
            st.rerun()

    st.markdown("---")

    # Linha 1: Resumo em 3 Blocos
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="crow-card"><h3>💰 Saldo Total</h3><h2 style="color:white;">$ 10.250,00</h2></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="crow-card"><h3>📈 Lucro Hoje</h3><h2 style="color:#00ff88;">+ $ 425,10</h2></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="crow-card"><h3>🤖 Status Bot</h3><h2 style="color:#00bcd4;">EXECUTANDO</h2></div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="crow-card"><h3>📡 Latência</h3><h2 style="color:white;">12ms</h2></div>', unsafe_allow_html=True)

    # Linha 2: O Principal (Gráfico e Ativos)
    col_grafico, col_ativos = st.columns([3, 1])

    with col_grafico:
        st.markdown('<div class="crow-card">', unsafe_allow_html=True)
        st.markdown("<h3>📈 Monitoramento em Tempo Real</h3>", unsafe_allow_html=True)
        
        # Gráfico de Linha Simples e Limpo (Preço + EMA)
        dados = pd.DataFrame({'Preço': [50, 52, 51, 53, 55, 54, 56, 58, 57, 59]})
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=dados['Preço'], mode='lines+markers', name='Preço', line=dict(color='#00bcd4', width=3)))
        fig.update_layout(
            template="plotly_dark", 
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            height=350,
            margin=dict(l=20, r=20, t=20, b=20)
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_ativos:
        st.markdown('<div class="crow-card">', unsafe_allow_html=True)
        st.markdown("<h3>📋 Lista de Ativos</h3>", unsafe_allow_html=True)
        st.write("**BTC/USDT** ● 🟢 Compra")
        st.write("**ETH/USDT** ● ⚪ Aguardar")
        st.write("**SOL/USDT** ● 🔴 Venda")
        st.write("**BNB/USDT** ● 🟢 Compra")
        st.markdown('</div>', unsafe_allow_html=True)

    # Linha 3: Rosca e Indicadores Técnicos
    col_rosca, col_rsi, col_ema = st.columns(3)

    with col_rosca:
        st.markdown('<div class="crow-card">', unsafe_allow_html=True)
        st.markdown("<h3>🍩 Alocação</h3>", unsafe_allow_html=True)
        fig_donut = go.Figure(data=[go.Pie(labels=['BTC', 'Altcoins', 'Cash'], values=[50, 30, 20], hole=.7)])
        fig_donut.update_layout(showlegend=False, height=150, margin=dict(t=0, b=0, l=0, r=0), paper_bgcolor='rgba(0,0,0,0)')
        fig_donut.update_traces(marker=dict(colors=['#00bcd4', '#004d4d', '#1a1a1a']))
        st.plotly_chart(fig_donut, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_rsi:
        st.markdown('<div class="crow-card">', unsafe_allow_html=True)
        st.markdown("<h3>📊 Indicador RSI</h3>", unsafe_allow_html=True)
        st.progress(65)
        st.write("RSI Atual: **65 (Neutro)**")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_ema:
        st.markdown('<div class="crow-card">', unsafe_allow_html=True)
        st.markdown("<h3>📉 Cruzamento EMA</h3>", unsafe_allow_html=True)
        st.write("EMA 20: **54.210**")
        st.write("EMA 50: **53.900**")
        st.write("Tendência: **ALTA**")
        st.markdown('</div>', unsafe_allow_html=True)
