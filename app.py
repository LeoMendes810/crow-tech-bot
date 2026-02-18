import streamlit as st
import base64
import pandas as pd
from datetime import datetime

# 1. Configurações de Marca Crow Tech
st.set_page_config(page_title="Crow Tech Elite Portal", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

# --- CSS ELITE (REMOÇÃO TOTAL DE FUNDO BRANCO E AJUSTES VISUAIS) ---
st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 18% !important;
        background-attachment: fixed !important;
        color: white !important;
    }}
    
    /* Cards Pretos com borda Neon */
    .product-card {{
        background: rgba(0, 0, 0, 0.85) !important;
        border: 1px solid rgba(0, 188, 212, 0.4);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 10px;
    }}

    /* Estilo dos Botões e Inputs - Fim do Fundo Branco */
    div.stButton > button {{
        background-color: #00bcd4 !important;
        color: #000000 !important;
        border: none !important;
        font-weight: 900 !important;
        text-transform: uppercase;
    }}
    
    /* Botão Sair Customizado */
    button[kind="secondary"] {{
        background-color: rgba(255, 75, 75, 0.2) !important;
        color: #ff4b4b !important;
        border: 1px solid #ff4b4b !important;
    }}

    /* Console Estilo Hacker */
    .stCodeBlock, div[data-testid="stCodeBlock"], div[data-testid="stCodeBlock"] > pre {{
        background-color: #000000 !important;
        border: 1px solid #00bcd4 !important;
    }}
    code {{ color: #00ff88 !important; background-color: transparent !important; }}

    /* Header Justificado à Direita */
    .header-box {{ text-align: right; padding-right: 15px; }}
    .main-title {{ color: white; font-size: 34px; font-weight: 900; margin: 0; line-height: 1; }}
    .sub-title {{ color: #00bcd4; font-size: 16px; font-weight: bold; margin: 0; letter-spacing: 1px; }}
    .slogan {{ color: rgba(255,255,255,0.6); font-size: 12px; font-style: italic; margin-top: 4px; }}

    /* Legenda de Meta Reforçada */
    .meta-label-bold {{
        color: #00bcd4 !important;
        font-weight: 900 !important;
        font-size: 15px;
        text-transform: uppercase;
        display: block;
        margin-bottom: 8px;
    }}
    </style>
""", unsafe_allow_html=True)

# Lógica de Estado
if 'logado' not in st.session_state: st.session_state.logado = False
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 100.0
if 'lucro_hoje' not in st.session_state: st.session_state.lucro_hoje = 42.50

if not st.session_state.logado:
    # Login Central
    _, col_log, _ = st.columns([1, 1, 1])
    with col_log:
        st.markdown(f'<div style="text-align:center; margin-top:100px;"><img src="data:image/png;base64,{logo_base64}" width="160"></div>', unsafe_allow_html=True)
        with st.form("auth"):
            u = st.text_input("USUÁRIO")
            p = st.text_input("SENHA", type="password")
            if st.form_submit_button("ACESSAR PORTAL"):
                if u == "admin" and p == "crow123":
                    st.session_state.logado = True
                    st.rerun()
else:
    # --- CABEÇALHO ---
    c_logo, c_head = st.columns([1, 3])
    with c_logo:
        st.image(f"data:image/png;base64,{logo_base64}", width=110)
    with c_head:
        st.markdown(f"""
            <div class="header-box">
                <p class="main-title">CROW TECH</p>
                <p class="sub-title">PORTAL ELITE</p>
                <p class="slogan">Inteligência em cada movimento</p>
            </div>
        """, unsafe_allow_html=True)

    tab_dash, tab_strat, tab_api = st.tabs(["📊 DASHBOARD", "⚙️ CONFIGURAÇÃO SCRIPT", "🔐 CONEXÃO API"])

    with tab_dash:
        # Linha de Métricas (Sem blocos vazios)
        m1, m2, m3 = st.columns([1, 1, 2])
        with m1:
            st.markdown('<div class="product-card"><small>BANCA TOTAL</small><br><span style="font-size:24px; font-weight:bold;">$ 10.250,00</span></div>', unsafe_allow_html=True)
        with m2:
            st.markdown(f'<div class="product-card"><small>LUCRO HOJE</small><br><span style="color:#00ff88; font-size:24px; font-weight:bold;">+ $ {st.session_state.lucro_hoje}</span></div>', unsafe_allow_html=True)
        with m3:
            st.markdown('<div class="product-card">', unsafe_allow_html=True)
            prog = min(st.session_state.lucro_hoje / st.session_state.meta_diaria, 1.0)
            st.markdown(f"<span class='meta-label-bold'>Progresso da Meta: $ {st.session_state.meta_diaria}</span>", unsafe_allow_html=True)
            st.progress(prog)
            st.markdown(f"<p style='text-align:right; font-size:12px; color:#00bcd4; margin-top:5px;'>{prog*100:.1f}% CONCLUÍDO</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        # Gráfico Binance Real
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.components.v1.html("""
            <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <script type="text/javascript">
            new TradingView.widget({
              "width": "100%", "height": 420, "symbol": "BINANCE:BTCUSDT",
              "interval": "1", "theme": "dark", "style": "1", "toolbar_bg": "rgba(0,0,0,0)"
            });
            </script>
        """, height=420)
        st.markdown('</div>', unsafe_allow_html=True)

        # Console Log (CORRIGIDO)
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        # O erro estava na f-string abaixo, agora isolada para evitar conflitos de caracteres
        log_time = datetime.now().strftime('%H:%M:%S')
        st.code(f"""
>>> [SISTEMA] Crow Tech Portal v.C18.9.1.5 Conectado.
>>> [INFO] Estratégia EMA 20 Ativa.
>>> [SCAN] Analisando RSI: {st.session_state.get('rsi_val', 30)}
>>> [{log_time}] Monitorando mercado...
        """, language="bash")
        
        c_btn1, c_btn2 = st.columns([4, 1])
        with c_btn1: st.button("🚀 INICIAR OPERAÇÕES", use_container_width=True)
        with c_btn2: 
            if st.button("SAIR", use_container_width=True, kind="secondary"):
                st.session_state.logado = False
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with tab_strat:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("### 🛠️ Ajuste Fino do Algoritmo")
        c_a, c_b = st.columns(2)
        with c_a:
            st.markdown("<b style='color:#00bcd4;'>Gatilho RSI</b>", unsafe_allow_html=True)
            st.markdown("<small>O bot entrará quando o RSI atingir este nível de sobrevenda.</small>", unsafe_allow_html=True)
            st.session_state.rsi_val = st.slider("RSI", 10, 50, 30, label_visibility="collapsed")
            
            st.markdown("<br><b style='color:#00bcd4;'>Stop Loss (%)</b>", unsafe_allow_html=True)
            st.markdown("<small>Limite máximo de perda permitida por operação.</small>", unsafe_allow_html=True)
            st.number_input("SL", 0.5, 5.0, 1.5, label_visibility="collapsed")
        
        with c_b:
            st.markdown("<b style='color:#00bcd4;'>Meta de Lucro Diário ($)</b>", unsafe_allow_html=True)
            st.markdown("<small>Lucro total acumulado no dia para desligamento automático.</small>", unsafe_allow_html=True)
            st.session_state.meta_diaria = st.number_input("Meta $", 10.0, 5000.0, float(st.session_state.meta_diaria), label_visibility="collapsed")

            st.markdown("<br><b style='color:#00bcd4;'>Média Móvel (EMA)</b>", unsafe_allow_html=True)
            st.markdown("<small>Configuração fixa do seu script operacional.</small>", unsafe_allow_html=True)
            st.text_input("EMA", value="EMA 20 (PADRÃO DO SCRIPT)", disabled=True, label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab_api:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        st.markdown("### 🔐 Conexão com Corretora")
        st.info("Suas chaves API são usadas apenas para execução de ordens e monitoramento de banca.")
        st.text_input("API KEY BINANCE", type="password")
        st.text_input("SECRET KEY", type="password")
        st.button("VINCULAR CONTA")
        st.markdown('</div>', unsafe_allow_html=True)
