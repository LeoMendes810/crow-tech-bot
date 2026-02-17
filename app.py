import streamlit as st
import base64

# 1. Configuração da página
st.set_page_config(page_title="Crow Tech Elite", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return None

# Carregamento da Marca d'água (assets/corvo_bg.png)
bg_base64 = get_base64('assets/corvo_bg.png')
bg_css = f"url(data:image/png;base64,{bg_base64})" if bg_base64 else "none"

if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- CSS PARA REPRODUZIR A IMAGEM ESCOLHIDA ---
st.markdown(f"""
    <style>
    /* Remover elementos padrão do Streamlit */
    header, footer, .stDeployButton {{ visibility: hidden !important; }}
    [data-testid="stHeader"] {{ background: rgba(0,0,0,0) !important; }}

    /* FUNDO DARK COM O CORVO CENTRALIZADO */
    .stApp {{
        background-color: #0b1016 !important;
        background-image: linear-gradient(rgba(11, 16, 22, 0.8), rgba(11, 16, 22, 0.8)), {bg_css} !important;
        background-size: 60% !important;
        background-repeat: no-repeat !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }}

    /* CONTAINER CENTRAL (O QUADRADO DE VIDRO) */
    .glass-box {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 50px 40px;
        width: 400px;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
        z-index: 1000;
    }}

    /* ÍCONE DE USUÁRIO (AVATAR) */
    .avatar-circle {{
        width: 75px;
        height: 75px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 50%;
        margin: 0 auto 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}

    /* INPUTS (LINHA MINIMALISTA) */
    .stTextInput input {{
        background-color: transparent !important;
        color: white !important;
        border: none !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 0px !important;
        padding: 10px 0px !important;
        font-size: 14px !important;
        margin-bottom: 5px;
    }}
    .stTextInput input:focus {{
        border-bottom: 2px solid #00bcd4 !important;
    }}

    /* BOTÃO LOGIN (CIANO NEON) */
    .stButton > button {{
        background-color: #00bcd4 !important;
        color: #000 !important;
        font-weight: bold !important;
        width: 130px !important;
        border: none !important;
        padding: 8px !important;
        border-radius: 5px !important;
        margin-top: 30px !important;
        transition: 0.3s;
    }}
    .stButton > button:hover {{
        box-shadow: 0 0 20px rgba(0, 188, 212, 0.6);
    }}

    /* LABELS DISCRETAS */
    label {{ color: rgba(255, 255, 255, 0.6) !important; font-size: 11px !important; text-transform: uppercase; text-align: left !important; }}
    
    /* LINKS DE RODAPÉ */
    .footer-links {{
        margin-top: 15px;
        display: flex;
        justify-content: space-between;
        font-size: 11px;
        color: rgba(255, 255, 255, 0.4);
    }}

    [data-testid="stForm"] {{
