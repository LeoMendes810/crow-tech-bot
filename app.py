import streamlit as st

# ================= CONFIG =================
st.set_page_config(page_title="Crow Tech", layout="wide")

if "logado" not in st.session_state:
    st.session_state.logado = False

# ================= CSS =================
st.markdown("""
<style>
.stApp { background:#0b1016; }
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 14px;
    margin-bottom: 16px;
}
</style>
""", unsafe_allow_html=True)

# ================= LOGIN =================
if not st.session_state.logado:

    with st.form("login"):
        st.markdown("<h3 style='text-align:center;color:white'>Crow Tech</h3>",
                    unsafe_allow_html=True)
        user = st.text_input("Usuário")
        pwd = st.text_input("Senha", type="password")
        entrar = st.form_submit_button("ENTRAR")

        if entrar:
            if user == "admin" and pwd == "crow123":
                st.session_state.logado = True
                st.rerun()
            else:
                st.error("Login inválido")

# ================= DASHBOARD =================
else:
    st.markdown("<h2 style='color:white'>Dashboard</h2>",
                unsafe_allow_html=True)

    tabs = st.tabs(["📊 Dashboard", "⚙️ Estratégia", "🔐 API"])

    # TAB 0
    with tabs[0]:
        st.markdown("<div class='card'>Sistema ativo</div>",
                    unsafe_allow_html=True)

    # TAB 1
    with tabs[1]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Estratégia Spot")
        st.write("EMA 20")
        st.write("RSI 35–50")
        st.write("Volume > 1.10x")
        st.write("Uso de 85% do saldo")
        st.write("Break-even + Trailing")
        st.markdown("</div>", unsafe_allow_html=True)

    # TAB 2
    with tabs[2]:
        st.markdown("<div class='card'>API Bitget (futuro)</div>",
                    unsafe_allow_html=True)
