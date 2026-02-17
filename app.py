import streamlit as st
import ccxt
import pandas as pd
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh

# Configuração da Página Elite
st.set_page_config(page_title="Crow Tech Dashboard", layout="wide", initial_sidebar_state="expanded")
st_autorefresh(interval=30000, key="datarefresh")

# Estilização Personalizada (Ciano, Branco e Tons de Cinza)
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #0e1117; border-right: 1px solid #0ea5e9; }
    .stMetric { background-color: #161b22; border-radius: 10px; padding: 15px; border: 1px solid #30363d; }
    .logo-text { font-size: 28px !important; font-weight: bold; color: #ffffff; margin-bottom: 0px; }
    .logo-tech { color: #0ea5e9; }
    .slogan { font-size: 14px; color: #8b949e; font-style: italic; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<p class="logo-text">CROW <span class="logo-tech">TECH</span></p>', unsafe_allow_html=True)
    st.markdown('<p class="slogan">Inteligência em cada movimento</p>', unsafe_allow_html=True)
    st.divider()
    st.toggle("Ligar Operações (OFF)", value=False, disabled=True, help="Operações bloqueadas para ajustes de design")
    st.write(f"⏰ Parada programada: **23:00**")
    st.divider()
    st.write("### Pares em Foco")
    st.info("SOL/USDT\n\nBTC/USDT")

# --- LÓGICA DE DADOS (BITGET) ---
try:
    exchange = ccxt.bitget({
        'apiKey': st.secrets["BITGET_API_KEY"],
        'secret': st.secrets["BITGET_SECRET"],
        'password': st.secrets["BITGET_PASSWORD"],
    })
    
    # Saldo Real
    bal = exchange.fetch_balance()
    saldo = bal['total'].get('USDT', 0)
    
    # Dados para Gráfico (SOL/USDT)
    bars = exchange.fetch_ohlcv('SOL/USDT', timeframe='1h', limit=30)
    df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'vol'])
    
    # Indicadores (RSI e AMA Simples)
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rsi = 100 - (100 / (1 + (gain / loss))).iloc[-1]
    ama = df['close'].rolling(window=10).mean().iloc[-1] # Média Adaptativa Simples para visual

except:
    saldo, rsi, ama = 185.50, 42.0, 141.50 # Fallback para design caso API falhe

# --- LAYOUT PRINCIPAL ---
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Saldo Real (USDT)", f"$ {saldo:.2f}", delta="Ativo", delta_color="normal")

with c2:
    meta = 20.0
    lucro_dia = 5.20 # Valor exemplo até integrarmos histórico
    cor_meta = "normal" if lucro_dia >= 0 else "inverse"
    st.metric("Meta do Dia ($20)", f"$ {lucro_dia:.2f}", delta=f"{((lucro_dia/meta)*100):.1f}%", delta_color=cor_meta)
    st.progress(min(lucro_dia/meta, 1.0))

with c3:
    status = "BUSCANDO" if rsi > 30 else "OPORTUNIDADE"
    st.metric("Status do Bot", status, delta=f"RSI: {rsi:.1f}")

st.divider()

# --- GRÁFICOS ---
col_graf, col_hist = st.columns([2, 1])

with col_graf:
    st.write("### Monitoramento SOL/USDT")
    fig = go.Figure(data=[go.Candlestick(x=pd.to_datetime(df['time'], unit='ms'),
                open=df['open'], high=df['high'],
                low=df['low'], close=df['close'],
                increasing_line_color='#0ea5e9', decreasing_line_color='#ff4b4b')])
    fig.update_layout(template="plotly_dark", height=400, margin=dict(l=20, r=20, t=20, b=20))
    st.plotly_chart(fig, use_container_width=True)
    st.write(f"**Indicadores:** RSI: `{rsi:.2f}` | AMA: `{ama:.2f}`")

with col_hist:
    st.write("### Histórico Acertos/Erros")
    # Gráfico de barras fictício para design
    hist_data = pd.DataFrame({'Trade': ['1', '2', '3', '4'], 'Resultado': [10, -5, 15, 8]})
    colors = ['#00ff00' if x > 0 else '#ff4b4b' for x in hist_data['Resultado']]
    fig_bar = go.Figure(data=[go.Bar(x=hist_data['Trade'], y=hist_data['Resultado'], marker_color=colors)])
    fig_bar.update_layout(template="plotly_dark", height=300)
    st.plotly_chart(fig_bar, use_container_width=True)

st.write("---")
st.caption("Crow Tech - Dashboard de Monitoramento Estratégico")
