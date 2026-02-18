import streamlit as st
import base64
from datetime import datetime

# Configurações de Marca
st.set_page_config(page_title="Crow Tech Elite Portal", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

# CSS Estabilizado - Removendo fundos brancos e fixando o visual
st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 20% !important;
        background-attachment: fixed !important;
        color: white !important;
    }}
    .header-box {{ text-align: right; }}
    .main-title {{ color: white; font-size: 38px; font-weight: 900; line-height: 1; margin: 0; }}
    .sub-title {{ color: #00bcd4; font-size: 16px; font-weight: bold; margin: 0; }}
    .slogan {{ color: rgba(255,255,255,0.5); font-size: 13px; font-style: italic; }}
    
    /* Input e Botões sem fundo branco */
    div[data-testid="stTextInput"] input, div[data-testid="stNumberInput"] input {{
        background-color: rgba(0, 0, 0, 0.5) !important;
        color: white !important;
        border: 1px solid #00bcd4 !important;
    }}
    .stButton>button {{
        background-color: #00bcd4 !important;
        color: black !important;
        font-weight: bold !important;
    }}
    </style>
""", unsafe_allow_html=True)

if 'logado' not in st.session_state: st.session_state.logado = False

# Sistema de Login (Corrigido para evitar SyntaxError)
if not st.session_state.logado:
    _, col_login, _ = st.columns([1, 1.2, 1])
    with col_login:
        st.markdown('<div style="background:rgba(255,255,255,0.05); padding:40px; border-radius:20px; text-align:center;">', unsafe_allow_html=True)
        st.image(f"data:image/png;base64,{logo_base64}", width=120)
        u = st.text_input("USUÁRIO")
        p = st.text_input("SENHA", type="password")
        if st.button("ENTRAR"):
            if u == "admin" and p == "crow123":
                st.session_state.logado = True
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
else:
    # Cabeçalho aprovado conforme Captura 222653
    c1, c2 = st.columns([1, 3])
    with c1: st.image(f"data:image/png;base64,{logo_base64}", width=100)
    with c2:
        st.markdown("""
            <div class="header-box">
                <p class="main-title">CROW TECH</p>
                <p class="sub-title">PORTAL ELITE</p>
                <p class="slogan">Inteligência em cada movimento</p>
            </div>
        """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📊 DASHBOARD", "⚙️ CONFIGURAÇÃO", "🔐 API"])

    with tab1:
        m1, m2, m3 = st.columns([1, 1, 2])
        m1.metric("BANCA", "$ 10.250,00")
        m2.metric("LUCRO", "+ $ 425,10")
        with m3:
            st.markdown('<p style="color:#00bcd4; font-weight:bold; margin-bottom:5px;">META DIÁRIA: $ 500.0</p>', unsafe_allow_html=True)
            st.progress(0.85)
        
        # Monitoramento e Console
        st.markdown("### Monitoramento em Tempo Real")
        st.components.v1.html('<div style="height:350px; background:#000; border:1px solid #333; display:flex; align-items:center; justify-content:center; color:#555;">[Gráfico TradingView Ativo]</div>', height=350)
        
        st.code(f">>> [SISTEMA] Crow Tech Online\n>>> [LOG] {datetime.now().strftime('%H:%M:%S')} - Escaneando mercado com EMA 20...")
        
        if st.button("🚀 INICIAR OPERAÇÕES"): st.info("Bot em execução.")
        if st.button("SAIR"):
            st.session_state.logado = False
            st.rerun()

    with tab2:
        st.markdown("### Ajuste de Parâmetros")
        st.slider("Gatilho RSI", 10, 50, 30)
        st.text_input("Estratégia", value="EMA 20 Nativa", disabled=True)

    with tab3:
        st.text_input("API KEY", type="password")
        st.text_input("SECRET KEY", type="password")
