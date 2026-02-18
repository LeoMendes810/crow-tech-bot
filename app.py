tab1, tab2, tab3 = st.tabs(
    ["📊 DASHBOARD", "⚙️ CONFIGURAÇÃO SCRIPT", "🔐 API CONNECTION"]
)

# ================= TAB 1 =================
with tab1:
    st.markdown("<div class='product-card'>", unsafe_allow_html=True)
    st.markdown("### 📊 Dashboard")
    st.info("Dashboard ativo. (conteúdo mantido)")

    st.markdown("</div>", unsafe_allow_html=True)

# ================= TAB 2 =================
with tab2:
    st.markdown("<div class='product-card'>", unsafe_allow_html=True)
    st.markdown("## ⚙️ Estratégia do Robô (Spot)")

    st.markdown("### 📈 Filtro de Tendência")
    st.number_input("EMA (períodos)", value=20, disabled=True)

    st.divider()

    st.markdown("### 📉 Timing de Entrada (RSI)")
    c1, c2 = st.columns(2)
    with c1:
        st.number_input("RSI mínimo", value=35, disabled=True)
    with c2:
        st.number_input("RSI máximo", value=50, disabled=True)

    st.divider()

    st.markdown("### 🔊 Confirmação por Volume")
    st.number_input("Volume mínimo (× média)", value=1.10, disabled=True)

    st.divider()

    st.markdown("### 💰 Gestão de Capital")
    st.number_input("Percentual do saldo por trade (%)", value=85, disabled=True)

    st.divider()

    st.markdown("### 🛡️ Proteções da Operação")
    c3, c4 = st.columns(2)
    with c3:
        st.number_input("Break-even (%)", value=0.80, disabled=True)
        st.number_input("Stop máximo (%)", value=-2.5, disabled=True)
    with c4:
        st.number_input("Alvo mínimo (%)", value=1.30, disabled=True)
        st.number_input("Recuo do topo (%)", value=0.30, disabled=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ================= TAB 3 =================
with tab3:
    st.markdown("<div class='product-card'>", unsafe_allow_html=True)
    st.info("Configuração de API será feita aqui.")
    st.markdown("</div>", unsafe_allow_html=True)
