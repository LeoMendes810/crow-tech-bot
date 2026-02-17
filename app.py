import streamlit as st
import base64

# Configuração da página
st.set_page_config(page_title="Crow Tech Elite", layout="wide")

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except: return ""

# Preparando as imagens
bg_base64 = get_base64('assets/corvo_bg.png')
logo_base64 = get_base64('assets/logo.png')

if 'logado' not in st.session_state:
    st.session_state.logado = False

# --- CSS PARA O FUNDO (FORA DO COMPONENTE) ---
st.markdown(f"""
    <style>
    header, footer, .stDeployButton, [data-testid="stHeader"] {{ visibility: hidden !important; }}
    .stApp {{
        background: #0b1016 url(data:image/png;base64,{bg_base64}) no-repeat center !important;
        background-size: 55% !important;
    }}
    /* Estilizando os campos reais que ficam embaixo do vidro */
    .stForm {{ background: transparent !important; border: none !important; }}
    </style>
""", unsafe_allow_html=True)

if not st.session_state.logado:
    # Renderizando o Design Idêntico via Componente Isolado (Isso impede que vire texto)
    login_html = f"""
    <div style="
        font-family: sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
    ">
        <div style="
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 40px;
            width: 350px;
            text-align: center;
            box-shadow: 0 20px 40px rgba(0,0,0,0.5);
        ">
            <div style="width: 70px; height: 70px; background: rgba(255,255,255,0.1); border-radius: 50%; margin: 0 auto 15px; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(255,255,255,0.2);">
                <img src="https://img.icons8.com/ios-filled/50/ffffff/user-male-circle.png" width="40"/>
            </div>
            <img src="data:image/png;base64,{logo_base64}" width="180">
            <p style="color: #00bcd4; font-size: 10px; letter-spacing: 2px; margin: 10px 0 30px 0;">CROW TECH ELITE</p>
            
            <div style="text-align: left;">
                <p style="color: rgba(255,255,255,0.4); font-size: 10px; margin: 0;">USERNAME</p>
                <div style="border-bottom: 1px solid rgba(255,255,255,0.3); padding: 8px 0; color: rgba(255,255,255,0.2); font-size: 13px; margin-bottom: 20px;">Digite no campo abaixo</div>
                
                <p style="color: rgba(255,255,255,0.4); font-size: 10px; margin: 0;">PASSWORD</p>
                <div style="border-bottom: 1px solid rgba(255,255,255,0.3); padding: 8px 0; color: rgba(255,255,255,0.2); font-size: 13px;">••••••••</div>
            </div>

            <div style="display: flex; justify-content: space-between; margin-top: 15px; font-size: 10px; color: rgba(255,255,255,0.3);">
                <span>Lembrar-me</span>
                <span>Esqueceu a senha?</span>
            </div>
            
            <div style="margin-top: 30px; background: #00bcd4; color: black; padding: 12px; border-radius: 5px; font-weight: bold; font-size: 14px; box-shadow: 0 0 15px rgba(0,188,212,0.4);">
                USE O FORMULÁRIO ABAIXO
            </div>
        </div>
    </div>
    """
    
    # Injetando o HTML de forma segura
    st.components.v1.html(login_html, height=600)

    # Formulário funcional (os campos que você realmente usa)
    with st.form("CrowLogin"):
        u = st.text_input("Usuário", label_visibility="collapsed", placeholder="Usuário")
        p = st.text_input("Senha", type="password", label_visibility="collapsed", placeholder="Senha")
        if st.form_submit_button("ACESSAR SISTEMA"):
            if u == "admin" and p == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Credenciais inválidas")

else:
    st.success("Logado com sucesso!")
    if st.button("Sair"):
        st.session_state.logado = False
        st.rerun()
