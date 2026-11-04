import os
import streamlit as st

st.set_page_config(page_title="Lucca Libanori | Data Analyst", layout="wide")

PROJETOS_PAGE = "pages/2_Projetos.py"  
CV_PATH = "assets/Curriculo_Lucca_Libanori_Analista_de_Dados.pdf"
IMG_DESTAQUE = "assets/bankroll_over_time.png"
REPO = "https://github.com/lucca-libanori/performance-analytics-platform"


st.title("Lucca Libanori")
st.subheader("Data Analyst | Python • SQL • PostgreSQL • Data Visualization")

st.write("""
Em transição para Data Analytics, desenvolvo pipelines e dashboards de análise de ponta
a ponta, com foco em medir retorno e risco com método.
""")

if os.path.exists(CV_PATH):
    with open(CV_PATH, "rb") as f:
        st.download_button(
            "Baixar currículo (PDF)",
            data=f.read(),
            file_name="Curriculo_Lucca_Libanori.pdf",
            mime="application/pdf",
        )

st.markdown("---")

st.header("Projeto em destaque")

left, right = st.columns([1.2, 1])

with left:
    st.subheader("Performance Analytics Platform")
    st.caption("Python · PostgreSQL · SQLAlchemy · Pandas · Streamlit · Plotly")
    st.write("""
Plataforma de análise de ponta a ponta: um pipeline de ETL valida e carrega os dados em
um banco PostgreSQL, e um dashboard interativo mostra retorno e risco (ROI, Sharpe,
drawdown). Uma simulação de Monte Carlo testa se o pior resultado foi azar ou variância
normal.
""")

    m1, m2, _ = st.columns([1, 1, 1])
    m1.metric("Registros", "~1.600")
    m2.metric("Simulações", "5.000")

    b1, b2, _ = st.columns([1.2, 1.2, 2])
    with b1:
        if os.path.exists(PROJETOS_PAGE):
            st.page_link(PROJETOS_PAGE, label="Ver detalhes")
        else:
            st.caption("Veja a página Projetos no menu.")
    with b2:
        st.link_button("Código no GitHub", REPO)

with right:
    if os.path.exists(IMG_DESTAQUE):
        st.image(IMG_DESTAQUE, use_container_width=True)
        st.caption("Evolução da banca ao longo do tempo")