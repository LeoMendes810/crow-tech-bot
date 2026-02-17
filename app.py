import streamlit as st
import base64

# 1. Configuração essencial
st.set_page_config(page_title="Crow Tech Elite", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- CSS DE TRAVAMENTO TOTAL ---
st.markdown(f"""
    <style>
    /* Limpeza de interface */
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    
    /* Fundo com Corvo Centralizado */
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 50% !important;
    }}

    /* A CAIXA DE VIDRO (Centralizada e Fixa) */
    .glass-card {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 400px;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 40px;
        z-index: 1000;
        text-align: center;
        box-shadow: 0 20px 50px rgba(0,0,0,0.6);
    }}

    /* Estilização dos campos de texto reais */
    .stTextInput input {{
        background: transparent !important;
        border: none !important;
        border-bottom: 1px solid rgba(255,255,255,0.2) !important;
        color: white !important;
        border-radius: 0 !important;
        padding: 10px 0 !important;
    }}
    
    .stTextInput input:focus {{
        border-bottom: 2px solid #00bcd4 !important;
        box-shadow: none !important;
    }}

    /* Botão de Login Neon */
    .stButton button {{
        background: #00bcd4 !important;
        color: black !important;
        font-weight: bold !important;
        width: 100% !important;
        border: none !important;
        padding: 10px !important;
        margin-top: 20px !important;
        box-shadow: 0 0 15px rgba(0,188,212,0.4) !important;
    }}

    /* Ajuste das labels para não sumirem */
    label {{ color: rgba(255,255,255,0.5) !important; font-size: 11px !important; }}
    
    /* Remove as bordas do formulário que o Streamlit cria */
    [data-testid="stForm"] {{ border: none !important; padding: 0 !important; }}
    </style>
""", unsafe_allow_html=True)

if not st.session_state.logado:
    # Estrutura do Card
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    # Elementos Visuais do Topo
    st.markdown("""
        <div style="width: 60px; height: 60px; background: rgba(255,255,255,0.1); border-radius: 50%; margin: 0 auto 15px; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(255,255,255,0.2);">
            <svg width="30" height="30" viewBox="0 0 24 24" fill="white"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08s5.97 1.09 6 3.08c-1.29 1.94-3.5 3.22-6 3.22z"/></svg>
        </div>
    """, unsafe_allow_html=True)
    
    st.image(f"data:image/png;base64,{logo_base64}", width=180)
    st.markdown('<p style="color:#00bcd4; font-size:10px; letter-spacing:2px; margin-top:5px;">CROW TECH ELITE</p>', unsafe_allow_html=True)

    # Formulário de Login (Agora dentro da div do card)
    with st.form("login_final"):
        user = st.text_input("USUÁRIO", placeholder="Username")
        password = st.text_input("SENHA", type="password", placeholder="Password")
        
        st.markdown("""
            <div style="display: flex; justify-content: space-between; font-size: 10px; color: rgba(255,255,255,0.3); margin-top: 10px;">
                <span>☐ Lembrar-me</span>
                <span>Esqueceu a senha?</span>
            </div>
        """, unsafe_allow_html=True)
        
        if st.form_submit_button("LOGIN"):
            if user == "admin" and password == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Dados incorretos")

    st.markdown('<p style="color:rgba(255,255,255,0.2); font-size:9px; margin-top:15px;">Não tem uma conta? Registre-se agora</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.success("SISTEMA CROW TECH ATIVADO")
    if st.button("Sair"):
        st.session_state.logado = False
        st.rerun()
