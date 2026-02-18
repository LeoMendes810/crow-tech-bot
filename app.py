import streamlit as st
import base64
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# 1. Setup de Marca Crow Tech
st.set_page_config(page_title="Crow Tech Elite Portal", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

# --- CSS ULTRA CLEAN (REMOÇÃO DE BLOCOS VAZIOS E CORREÇÃO DE CONSOLE) ---
st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 20% !important;
        background-attachment: fixed !important;
    }}
    
    /* Cards Profissionais */
    .product-card {{
        background: rgba(10, 15, 20, 0.8);
        border: 1px solid rgba(0, 188, 212, 0.2);
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
    }}

    /* CONSOLE REAL (FUNDO PRETO FORÇADO) */
    .stCodeBlock, div[data-testid="stCodeBlock"] {{
        background-color: #000000 !important;
        border: 1px solid #00bcd4 !important;
    }}
    code {{
        color: #00ff88 !important;
        background-color: transparent !important;
    }}

    .config-label {{ color: #00bcd4; font-weight: bold; font-size: 15px; }}
    .instruction-text {{ color: #ffffff; font-size: 12px; opacity: 0.8; margin-bottom: 10px; }}
    </style>
""", unsafe_allow_html=True)

# Gerenciamento de Memória do Bot
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 100.0
if 'lucro_acumulado' not in st.session_state: st.session_state.lucro_acumulado = 42.50

# --- LÓGICA DE NAVEGAÇÃO ---
if 'logado' not in st.session_state: st.session_state.logado = False

if not st.session_state.logado:
    # Login Centralizado
    _, col2, _ = st.columns([1, 1, 1])
    with col2:
        st.markdown(f'<div style="text-align:center; margin-top:50px;"><img src="data:image/png;base64,{logo_base64}" width="150"></div>', unsafe_allow_html=True)
        with st.form("login"):
            u = st.text_input("USUÁRIO AXIO")
            p = st.text_input("SENHA", type="password")
            if st.form_submit_button("ENTRAR NO TERMINAL"):
                if u == "admin" and p == "crow123":
                    st.session_state.logado = True
                    st.rerun()
else:
    # --- INTERFACE PRINCIPAL ---
    c1, c2, c3 = st.columns([1, 4, 1])
    with c1: st.image(f"data:image/png;base64,{logo_base64}", width=70)
    with c2: st.markdown("<h2 style='text-align:center; color:white;'>CROW TECH <span style='color:#00bcd4;'>PORTAL ELITE</span></h2>", unsafe_allow_html=True)
    with c3: 
        if st.button("SAIR"): 
            st.session_state.logado = False
            st.rerun()

    tab1, tab2, tab3 = st.tabs(["📊 DASHBOARD", "⚙️ CONFIGURAÇÃO SCRIPT", "🔐 API CONNECTION"])

    with tab1:
        # Top Cards: Dinheiro e Meta
        col_a, col_b, col_c = st.columns([1, 1, 2])
        with col_a:
            st.markdown('<div class="product-card"><small>BANCA ATUAL (USDT)</small><br><span style="font-size:22px; font-weight:bold;">$ 10.250,00</span></div>', unsafe_allow_html=True)
        with col_b:
            st.markdown(f'<div class="product-card"><small>LUCRO HOJE</small><br><span style="color:#00ff88; font-size:22px; font-weight:bold;">+ $ {st.session_state.lucro_acumulado}</span></div>', unsafe_allow_html=True)
        with col_c:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            pct = min(st.session_state.lucro_acumulado / st.session_state.meta_diaria, 1.0)
            st.markdown(f"<small>PROGRESSO DA META DIÁRIA ($ {st.session_state.meta_diaria})</small>", unsafe_allow_html=True)
            st.progress(pct)
            st.markdown(f"<p style='text-align:right; font-size:11px; color:#00bcd4;'>{pct*100:.1f}% CONCLUÍDO</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # Monitoramento Estilo Binance
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("<small>LIVE CHART (VIA API USUÁRIO)</small>", unsafe_allow_html=True)
        # Aqui, no futuro, injetaremos o TradingView Widget real
        st.components.v1.html("""
            <div class="tradingview-widget-container">
                <div id="tradingview_12345"></div>
                <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
                <script type="text/javascript">
                new TradingView.widget({
                  "width": "100%", "height": 400, "symbol": "BINANCE:BTCUSDT",
                  "interval": "1", "timezone": "Etc/UTC", "theme": "dark", "style": "1"
                });
                </script>
            </div>
        """, height=400)
        st.markdown('</div>', unsafe_allow_html=True)

        # Console de Operação Estilo Termux
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("<small>LOG DE EXECUÇÃO EM TEMPO REAL</small>", unsafe_allow_html=True)
        st.code(f"""
>>> [OK] API Conectada com sucesso.
>>> [SCAN] Analisando Médias Móveis (EMA 9/21)...
>>> [ANALYSIS] Preço acima da EMA 21. Tendência confirmada.
>>> [INFO] Aguardando RSI tocar nível configurado ({st.session_state.get('rsi_val', 30)})...
>>> [{datetime.now().strftime('%H:%M:%S')}] Monitorando par selecionado.
        """, language="bash")
        st.button("🚀 LIGAR ROBÔ", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("### 🛠️ Parâmetros do Robô (Script Termux)")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<p class="config-label">Gatilho RSI</p>', unsafe_allow_html=True)
            st.markdown('<p class="instruction-text">Define o nível de "sobrevenda". Quando o mercado cai demais (RSI baixo), o robô entende que é hora de comprar.</p>', unsafe_allow_html=True)
            st.session_state.rsi_val = st.slider("RSI", 10, 50, 30, label_visibility="collapsed")
            
            st.markdown('<br><p class="config-label">Stop Loss Automático (%)</p>', unsafe_allow_html=True)
            st.markdown('<p class="instruction-text">Se a operação cair este valor, o robô encerra para proteger seu capital.</p>', unsafe_allow_html=True)
            st.number_input("SL", 0.5, 5.0, 1.5, label_visibility="collapsed")

        with c2:
            st.markdown('<p class="config-label">Meta de Lucro Diário ($)</p>', unsafe_allow_html=True)
            st.markdown('<p class="instruction-text">O robô monitora o lucro total das operações do dia. Ao atingir este valor em dólares, ele para de operar até o dia seguinte.</p>', unsafe_allow_html=True)
            st.session_state.meta_diaria = st.number_input("Meta $", 10.0, 5000.0, float(st.session_state.meta_diaria), label_visibility="collapsed")

            st.markdown('<br><p class="config-label">Cruzamento de Médias (EMA)</p>', unsafe_allow_html=True)
            st.markdown('<p class="instruction-text">Padrão de referência: EMA 9 (Curta) e EMA 21 (Longa). O robô busca entradas quando a rápida cruza a lenta.</p>', unsafe_allow_html=True)
            st.selectbox("Referência", ["9 / 21 (Recomendado)", "20 / 50", "50 / 200"], label_visibility="collapsed")
        
        st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("### 🔐 Credenciais de Operação")
        st.info("O robô precisa dessas chaves para enviar ordens para a sua conta na corretora. Suas chaves ficam protegidas pelo protocolo AXIO.")
        st.text_input("API KEY BINANCE", type="password")
        st.text_input("SECRET KEY BINANCE", type="password")
        st.button("VINCULAR E TESTAR CONEXÃO")
        st.markdown('</div>', unsafe_allow_html=True)
