import streamlit as st

st.set_page_config(page_title="Certificados | Lucca Libanori", layout="wide")

st.title("Certificados")

st.write("""
Cursos e especializações que venho concluindo para consolidar minha base técnica.
""")

st.markdown("---")

certificados = [
    {
        "imagem": "assets/certificados/certificado_excel_powerbi.png",
        "titulo": "Excel to Power BI: Data Analysis & Business Intelligence",
        "instituicao": "Coursera — Knowledge Accelerators",
        "tipo": "Especialização (4 cursos)",
        "data": "Concluído em 11/09/2026",
        "descricao": (
            "Progressão de habilidades fundamentais em planilhas até visualização de dados "
            "e criação de dashboards, com foco em organizar, analisar e comunicar dados "
            "para apoiar decisões orientadas a dados."
        ),
        "cursos": [
            "Excel Basics for Beginners: Workbooks, Formatting, Charts and Core Skills",
            "Intermediate Excel: Data Modeling, Analysis, and Dashboards",
            "From Excel to Power BI",
            "Dive Deeper into Data-Driven Decisions with Power BI",
        ],
        "link": "https://coursera.org/verify/specialization/1JKW8LQEE8QN",
        "link_label": "🔗 Verificar certificado",
    },
    {
        "imagem": "assets/certificados/certificado_python_hype.png",
        "titulo": "Python para Ciência de Dados",
        "instituicao": "Hype Data & AI",
        "tipo": "Certificado de curso",
        "data": "Concluído em 16/05/2026 e 17/05/2026 · Duração: 2 horas",
        "descricao": "Curso introdutório de Python aplicado à Ciência de Dados.",
        "cursos": [],
        "link": None,
        "link_label": None,
    },
]

cols = st.columns(2)

for i, cert in enumerate(certificados):
    with cols[i % 2]:
        with st.container(border=True):
            st.image(cert["imagem"], use_container_width=True)
            st.subheader(cert["titulo"])
            st.caption(f'{cert["instituicao"]} · {cert["tipo"]}')
            st.write(cert["data"])

            if cert["descricao"]:
                st.write(cert["descricao"])

            if cert["cursos"]:
                with st.expander("Ver cursos inclusos"):
                    for curso in cert["cursos"]:
                        st.markdown(f"- {curso}")

            if cert["link"]:
                st.link_button(cert["link_label"], cert["link"])