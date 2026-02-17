import streamlit as st
import ccxt
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# Configuração da Página
st.set_page_config(page_title="Crow Tech Elite", layout="wide")
st_autorefresh(interval=30000, key="datarefresh") # Atualiza a cada 30 segundos

# Conexão com Bitget usando os Secrets que você salvou
try:
    exchange = ccxt.bitget({
        'apiKey': st.secrets["BITGET_API_KEY"],
        'secret': st.secrets["BITGET_SECRET"],
        'password': st.secrets["BITGET_PASSWORD"],
    })

    # Busca Saldo Real
    balance = exchange.fetch_balance()
    usdt_balance = balance['total'].get('USDT', 0)
    
    # Busca Preço e RSI (Exemplo Solana)
    bars = exchange.fetch_ohlcv('SOL/USDT', timeframe='1h', limit=50)
    df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'vol'])
    
    # Cálculo Simples de RSI
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs)).iloc[-1]
    
    status_bot = "🔥 Monitorando" if rsi > 30 else "🚀 OPORTUNIDADE"
    
except Exception as e:
    usdt_balance = 0.0
    rsi = 0.0
    status_bot = "⚠️ Erro de Conexão"
    st.error(f"Erro: Verifique suas chaves nos Secrets.")

# --- VISUAL CROW TECH ---
st.title("🐦‍⬛ CROW TECH")
st.markdown("*Inteligência em cada movimento*")
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Saldo Real (USDT)", f"$ {usdt_balance:.2f}")
    st.caption("Saldo direto da sua carteira Bitget")

with col2:
    meta = 20.0
    # Cálculo de progresso baseado em um lucro fictício ou real se preferir
    progresso = min(usdt_balance / 200, 1.0) # Exemplo: progresso baseado no saldo
    st.metric("Meta do Dia", f"$ {meta:.2f}", "Rumo aos $20")
    st.progress(0.45) # Aqui podemos ajustar para mostrar seu lucro do dia

with col3:
    st.metric("RSI Solana (1h)", f"{rsi:.2f}")
    st.write(f"Status: **{status_bot}**")

st.divider()
st.sidebar.image("https://raw.githubusercontent.com/LeoMendes810/crow-tech-bot/master/assets/logo.png", width=150) # Tenta puxar o logo se existir
st.sidebar.title("Configurações")
st.sidebar.write(f"Horário de parada: 23:00")
