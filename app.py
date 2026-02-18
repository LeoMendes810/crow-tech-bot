import streamlit as st
import base64
from datetime import datetime

# 1. Configurações de Marca
st.set_page_config(page_title="Crow Tech Elite", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

# --- CSS: RESTAURANDO LOGIN E CORRIGINDO ERROS ---
st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 20% !important;
        background-attachment: fixed !important;
        color: white !important;
    }}

    /* RESTAURAÇÃO DA TELA DE LOGIN (CARD TRANSLÚCIDO ORIGINAL) */
    .login-box {{
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 40px;
        text-align: center;
    }}

    /* Dashboard: Fim dos fundos brancos nos inputs */
    div[data-testid="stTextInput"] input, div[data-testid="stNumberInput"] input {{
        background-color: rgba(0, 0, 0, 0.5) !important;
        color: white !important;
        border: 1px solid #00bcd4 !important;
    }}

    /* Botão Iniciar Operações (Ciano) */
    div.stButton > button {{
        background-color: #00bcd4 !important;
        color: black !important;
        font-weight: bold !important;
        width: 100% !important;
    }}

    /* Títulos e Slogan */
    .header-right {{ text-align: right; }}
    .slogan-text {{ 
        color: rgba(255,255,255,0.6); 
        font-size: 14px; 
        font-style: italic;
    }}
    
    /* Legenda de Meta Reforçada */
    .meta-destaque {{
        color: #00bcd4 !important;
        font-weight: 900 !important;
        text-transform: uppercase;
        font-size: 16px;
    }}
    </style>
""", unsafe_allow_html=True)

if 'logado' not in st.session_state: st.session_state.logado = False

# --- TELA DE LOGIN ORIGINAL ---
if not st.session_state.logado:
    _, col_login, _ = st.columns([1, 1.2, 1])
    with col_login:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.image(f"data:image/png;base64,{logo_base64}", width=120)
        st.markdown("<h2 style='color:white; margin-bottom:0;'>CROW TECH</h2><p style='color:#00bcd4;'>CROW TECH ELITE</p>", unsafe_allow_html=True)
        
        u = st.text_input("USUÁRIO", placeholder="Username")
        p = st.text_input("SENHA", type="password", placeholder="Password")
        
        # Botão centralizado e sem erro
        if st.button("ACESSAR SISTEMA"):
            if u == "admin" and p == "crow123":
                st.session_state.logado = True
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- DASHBOARD APÓS LOGIN ---
    c_l, c_r = st.columns([1, 3])
    with c_l: 
        st.image(f"data:image/png;base64,{logo_base64}", width=100)
    with c_r:
        st.markdown("""
            <div class="header-right">
                <h1 style="margin:0;">CROW TECH <span style="color:#00bcd4;">PORTAL ELITE</span></h1>
                <p class="slogan-text">Inteligência em cada movimento</p>
            </div>
        """, unsafe_allow_html=True)

    t1, t2, t3 = st.tabs(["📊 DASHBOARD", "⚙️ CONFIGURAÇÃO", "🔐 API"])

    with t1:
        col_m1, col_m2, col_m3 = st.columns([1, 1, 2])
        col_m1.metric("BANCA USDT", "$ 10.250,00")
        col_m2.metric("LUCRO HOJE", "+ $ 425,10")
        with col_m3:
            st.markdown('<p class="meta-destaque">Meta Diária: $ 500.0</p>', unsafe_allow_html=True)
            st.progress(0.85)

        # Gráfico e Console
        st.components.v1.html("""
            <div style="height:400px;"><script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
            <script type="text/javascript">new TradingView.widget({"width": "100%", "height": 400, "symbol": "BINANCE:BTCUSDT", "theme": "dark"});</script></div>
        """, height=400)

        st.code(f">>> [SISTEMA] Crow Tech Online\n>>> [ESTRATÉGIA] EMA 20 Ativa\n>>> [{datetime.now().strftime('%H:%M:%S')}] Monitorando ativos...")
        
        # Correção do erro TypeError: Removi o kind="secondary" que não existe nativamente no st.button padrão dessa forma
        if st.button("🚀 INICIAR OPERAÇÕES"):
            st.success("Bot iniciado com sucesso!")
        
        if st.button("SAIR"):
            st.session_state.logado = False
            st.rerun()

    with t2:
        st.markdown("### Ajuste de Parâmetros")
        st.slider("Gatilho RSI", 10, 50, 30)
        st.number_input("Stop Loss (%)", value=1.50)
        st.text_input("EMA de Referência", value="EMA 20", disabled=True)

    with t3:
        st.text_input("API KEY", type="password")
        st.text_input("SECRET KEY", type="password")
