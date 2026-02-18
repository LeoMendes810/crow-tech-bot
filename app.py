import streamlit as st
import base64
from datetime import datetime

# ======================================================
# CONFIGURAÇÃO DA PÁGINA
# ======================================================
st.set_page_config(page_title="Crow Tech Elite Portal", layout="wide")

# ======================================================
# FUNÇÃO PARA CARREGAR IMAGENS
# ======================================================
def get_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

bg_base64 = get_base64("assets/corvo_bg.png")
logo_base64 = get_base64("assets/logo.png")

# ======================================================
# SESSION STATE (MEMÓRIA)
# ======================================================
if "logado" not in st.session_state:
    st.session_state.logado = False

if "meta_diaria" not in st.session_state:
    st.session_state.meta_diaria = 100.0

if "lucro_acumulado" not in st.session_state:
    st.session_state.lucro_acumulado = 42.50

if "rsi_val" not in st.session_state:
    st.session_state.rsi_val = 30

# ======================================================
# CSS GLOBAL (LOGIN + DASHBOARD)
# ======================================================
st.markdown(f"""
<style>
header, footer, .stDeployButton, [data-testid="stHeader"] {{
    visibility: hidden !important;
}}

.stApp {{
    background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center;
    background-size: 25%;
    background-attachment: fixed;
}}

.product-card {{
    background: rgba(10,15,20,0.85);
    border: 1px solid rgba(0,188,212,0.35);
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 12px;
    box-shadow: 0 0 25px rgba(0,188,212,0.15);
}}

.config-label {{
    color: #00bcd4;
    font-weight: bold;
    font-size: 14px;
}}

.instruction-text {{
    color: white;
    font-size: 12px;
    opacity: 0.8;
}}

.stCodeBlock {{
    background-color: #000 !important;
    border: 1px solid #00bcd4 !important;
}}

code {{
    color: #00ff88 !important;
}}

.stTextInput input {{
    background: rgba(255,255,255,0.85) !important;
    color: #000 !important;
    font-weight: bold;
    border: none !important;
    border-bottom: 2px solid #00bcd4 !important;
}}

.stButton > button {{
    background: rgba(0,188,212,0.18) !important;
    color: #eaffff !important;
    font-weight: 800 !important;
    height: 46px;
    border: 1px solid rgba(0,188,212,0.6) !important;
    border-radius: 10px !important;
    box-shadow: 0 0 15px rgba(0,188,212,0.35);
}}

.stButton > button:hover {{
    background: rgba(0,188,212,0.35) !important;
    box-shadow: 0 0 22px rgba(0,188,212,0.7);
}}
</style>
""", unsafe_allow_html=True)

# ======================================================
# LOGIN
# ======================================================
if not st.session_state.logado:

    st.markdown("""
    <style>
    [data-testid="stForm"] {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 360px;
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(25px);
        border-radius: 22px;
        padding: 28px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.6);
    }
    </style>
    """, unsafe_allow_html=True)

    with st.form("login"):
        st.markdown(
            f"<div style='text-align:center'><img src='data:image/png;base64,{logo_base64}' width='150'></div>",
            unsafe_allow_html=True
        )

        usuario = st.text_input("Usuário", placeholder="Digite seu usuário")
        senha = st.text_input("Senha", type="password", placeholder="Digite sua senha")

        st.markdown(
            "<div style='text-align:right;font-size:11px;color:#9adfe6;'>Esqueci a senha</div>",
            unsafe_allow_html=True
        )

        entrar = st.form_submit_button("ENTRAR")

        st.markdown(
            "<div style='text-align:center;font-size:11px;color:#00bcd4;margin-top:12px;'>Não tem conta? Cadastre-se</div>",
            unsafe_allow_html=True
        )

        if entrar:
            if usuario == "admin" and senha == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Usuário ou senha inválidos")

# ======================================================
# DASHBOARD COMPLETO
# ======================================================
else:
    # HEADER
    h1, h2, h3 = st.columns([1,4,1])
    with h1:
        st.image(f"data:image/png;base64,{logo_base64}", width=60)
    with h2:
        st.markdown(
            "<h2 style='text-align:center;color:white;'>CROW TECH <span style='color:#00bcd4;'>PORTAL ELITE</span></h2>",
            unsafe_allow_html=True
        )
    with h3:
        if st.button("SAIR"):
            st.session_state.logado = False
            st.rerun()

    tab1, tab2, tab3 = st.tabs(["📊 DASHBOARD", "⚙️ CONFIGURAÇÃO SCRIPT", "🔐 API CONNECTION"])

    # ================= TAB 1 =================
    with tab1:
        c1, c2, c3 = st.columns([1,1,2])

        with c1:
            st.markdown(
                "<div class='product-card'><small>BANCA ATUAL (USDT)</small><br><b>$ 10.250</b></div>",
                unsafe_allow_html=True
            )

        with c2:
            st.markdown(
                f"<div class='product-card'><small>LUCRO HOJE</small><br>"
                f"<span style='color:#00ff88;font-size:20px;'>+ $ {st.session_state.lucro_acumulado}</span></div>",
                unsafe_allow_html=True
            )

        with c3:
            pct = min(st.session_state.lucro_acumulado / st.session_state.meta_diaria, 1.0)
            st.markdown("<div class='product-card'>", unsafe_allow_html=True)
            st.markdown(
                f"<small>PROGRESSO META DIÁRIA ($ {st.session_state.meta_diaria})</small>",
                unsafe_allow_html=True
            )
            st.progress(pct)
            st.markdown(
                f"<p style='text-align:right;font-size:11px;color:#00bcd4;'>{pct*100:.1f}% CONCLUÍDO</p>",
                unsafe_allow_html=True
            )
            st.markdown("</div>", unsafe_allow_html=True)

        # CHART (PLACEHOLDER)
        st.markdown("<div class='product-card'>", unsafe_allow_html=True)
        st.markdown("<small>LIVE CHART (TradingView)</small>", unsafe_allow_html=True)
        st.components.v1.html("""
<div class="tradingview-widget-container">
  <div id="tradingview_crow"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget({
    "width": "100%",
    "height": 420,
    "symbol": "BINANCE:BTCUSDT",
    "interval": "1",
    "timezone": "Etc/UTC",
    "theme": "dark",
    "style": "1",
    "locale": "br",
    "toolbar_bg": "#0b1016",
    "hide_top_toolbar": false,
    "allow_symbol_change": true,
    "container_id": "tradingview_crow"
  });
  </script>
</div>
""", height=420)
        st.markdown("</div>", unsafe_allow_html=True)

        # CONSOLE
        st.markdown("<div class='product-card'>", unsafe_allow_html=True)
        st.markdown("<small>LOG DE EXECUÇÃO</small>", unsafe_allow_html=True)
        st.code(f"""
>>> [OK] API conectada
>>> [SCAN] EMA 9 / 21
>>> [INFO] RSI aguardando nível {st.session_state.rsi_val}
>>> [{datetime.now().strftime('%H:%M:%S')}] Monitorando mercado
        """, language="bash")
        st.button("🚀 LIGAR ROBÔ", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ================= TAB 2 =================
    with tab2:
        st.markdown("<div class='product-card'>", unsafe_allow_html=True)
        st.markdown("### 🛠️ Parâmetros do Robô")

        st.markdown("<p class='config-label'>Gatilho RSI</p>", unsafe_allow_html=True)
        st.session_state.rsi_val = st.slider("RSI", 10, 50, st.session_state.rsi_val)

        st.markdown("<p class='config-label'>Meta de Lucro Diário ($)</p>", unsafe_allow_html=True)
        st.session_state.meta_diaria = st.number_input(
            "Meta", 10.0, 5000.0, st.session_state.meta_diaria
        )

        st.markdown("</div>", unsafe_allow_html=True)

    # ================= TAB 3 =================
    with tab3:
        st.markdown("<div class='product-card'>", unsafe_allow_html=True)
        st.info("Suas chaves ficam protegidas.")
        st.text_input("API KEY BINANCE", type="password")
        st.text_input("SECRET KEY BINANCE", type="password")
        st.button("VINCULAR E TESTAR CONEXÃO")
        st.markdown("</div>", unsafe_allow_html=True)
