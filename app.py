import streamlit as st
import base64
import pandas as pd
from datetime import datetime

# 1. CONFIGURAÇÕES DE MARCA E TEMA
st.set_page_config(page_title="Crow Tech Elite Portal", layout="wide", initial_sidebar_state="collapsed")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

# --- CSS DEFINITIVO (RESTAURANDO O LOGIN E ELIMINANDO FUNDOS BRANCOS) ---
st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 20% !important;
        background-attachment: fixed !important;
        color: white !important;
    }}

    /* LOGIN CARD (RESTAURADO) */
    .login-container {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 40px;
        margin-top: 50px;
    }}

    /* CARDS DO DASHBOARD */
    .product-card {{
        background: rgba(0, 0, 0, 0.8) !important;
        border: 1px solid rgba(0, 188, 212, 0.3);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    }}

    /* CONSOLE PRETO ABSOLUTO */
    .stCodeBlock, div[data-testid="stCodeBlock"], div[data-testid="stCodeBlock"] pre {{
        background-color: #000000 !important;
        border: 1px solid #00bcd4 !important;
    }}
    code {{ color: #00ff88 !important; background-color: transparent !important; }}

    /* CABEÇALHO E SLOGAN */
    .header-box {{ text-align: right; }}
    .main-title {{ color: white; font-size: 38px; font-weight: 900; line-height: 1; margin: 0; }}
    .sub-title {{ color: #00bcd4; font-size: 16px; font-weight: bold; margin: 0; }}
    .slogan {{ color: rgba(255,255,255,0.5); font-size: 13px; font-style: italic; }}

    /* META LEGENDA */
    .meta-bold {{ color: #00bcd4 !important; font-weight: 900; font-size: 15px; text-transform: uppercase; }}

    /* CORREÇÃO DE BOTÕES */
    .stButton>button {{
        background-color: #00bcd4 !important;
        color: black !important;
        font-weight: bold !important;
        border: none !important;
    }}
    </style>
""", unsafe_allow_html=True)

if 'logado' not in st.session_state: st.session_state.logado = False
if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 100.0
if 'lucro_hoje' not in st.session_state: st.session_state.lucro_hoje = 42.50

# --- LÓGICA DE ACESSO ---
if not st.session_state.logado:
    _, col_login, _ = st.columns([1, 1.2, 1])
    with col_login:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.image(f"data:image/png;base64,{logo_base64}", width=150)
        st.markdown("<h2 style='text-align:center;'>CROW TECH</h2>", unsafe_allow_html=True)
        u = st.text_input("USUÁRIO", placeholder="Username")
        p = st.text_input("SENHA", type="password", placeholder="Password")
        if st.button("ACESSAR TERMINAL"):
            if u == "admin" and p == "crow123":
                st.session_state.logado = True
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
else
