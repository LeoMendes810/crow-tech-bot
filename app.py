import streamlit as st
import ccxt
import pandas as pd
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh

# Configuração Crow Tech
st.set_page_config(page_title="Crow Tech Elite", layout="wide")
st_autorefresh(interval=30000, key="datarefresh")

# Cores e Estilo
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1c2128; border-radius: 10px; padding: 15px; border: 1px solid #30363d; color: white; }
    div[data-testid="stMetricValue"] { color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO COM LOGO ---
col_l, col_t = st.columns([1, 5])
with col_l:
    # Busca o logo na pasta Ativos que você criou
    st.image("Ativos/logo.png", width=120)
with col_t:
    st.markdown("# <span style='color:white'>CROW</span> <span style='color:#0ea5e9'>TECH</span>", unsafe_allow_html=True)
    st.markdown("*Inteligência em cada movimento*")

# --- LÓGICA DE DADOS ---
try:
    exchange = ccxt.bitget({
        'apiKey': st.secrets["BITGET_API_KEY"],
        'secret': st.secrets["BITGET_SECRET"],
        'password': st.secrets["BITGET_PASSWORD"],
    })
    bal = exchange.fetch_balance()
    saldo_real = bal['total'].get('USDT', 0)
    
    # Exemplo de monitoramento SOL/USDT
    bars = exchange.fetch_ohlcv('SOL/USDT', timeframe='1h', limit=50)
    df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'vol'])
    
    # Cálculos RSI e AMA
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
    rsi = 100 - (100 / (1 + (gain / loss))).iloc[-1]
    ama = df['close'].rolling(10).mean().iloc[-1]

except:
    saldo_real, rsi, ama = 15.94, 56.1, 142.0 # Fallback do seu print

# --- DASHBOARD ---
st.divider()
c1, c2, c3 = st.columns(3)

with c1:
    # Verde para positivo (acima de 0)
    st.metric("Saldo Real (USDT)", f"$ {saldo_real:.2f}", delta="Ativo", delta_color="normal")

with c2:
    meta = 20.0
    lucro = 5.20 # Exemplo
    # Lógica de cores: Verde se atingiu a meta, Vermelho se está abaixo
    cor_seta = "normal" if lucro >= meta else "inverse"
    st.metric("Meta do Dia ($20.00)", f"$ {lucro:.2f}", delta=f"{((lucro/meta)*100):.1f}%", delta_color=cor_seta)
    st.progress(min(lucro/meta, 1.0))

with c3:
    status = "BUSCANDO" if rsi > 30 else "OPORTUNIDADE"
    st.metric("Status do Bot", status, delta=f"RSI: {rsi:.1f}")

# --- GRÁFICOS ---
st.divider()
g1, g2 = st.columns([2, 1])

with g1:
    st.subheader("Monitoramento SOL/USDT")
    fig = go.Figure(data=[go.Candlestick(x=pd.to_datetime(df['time'], unit='ms'),
                open=df['open'], high=df['high'], low=df['low'], close=df['close'],
                increasing_line_color='#00ff00', decreasing_line_color='#ff0000')]) # Cores que você pediu
    fig.update_layout(template="plotly_dark", height=400)
    st.plotly_chart(fig, use_container_width=True)
    st.write(f"**Indicadores Ativos:** RSI: `{rsi:.1f}` | AMA: `{ama:.1f}`")

with g2:
    st.subheader("Histórico Acertos/Erros")
    # Gráfico de barras com cores condicionais
    res_dados = [12, -4, 8, 15] # Exemplo de trades
    cores_barras = ['#00ff00' if x > 0 else '#ff0000' for x in res_dados]
    fig_bar = go.Figure(go.Bar(y=res_dados, marker_color=cores_barras))
    fig_bar.update_layout(template="plotly_dark", height=300)
    st.plotly_chart(fig_bar, use_container_width=True)

st.sidebar.write("### Configurações")
st.sidebar.info("Robô em modo Visual. Próxima parada às 23:00.")
