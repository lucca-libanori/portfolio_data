import streamlit as st

st.set_page_config(page_title="Contato | Lucca Libanori", layout="wide")

st.title("Contato")

st.write("""
Caso queira debater sobre algum projeto ou algo relacionado à área de dados, 
aqui estão algumas maneiras de entrar em contato comigo.
""")

st.markdown("---")

email = "luccalibanori66@gmail.com"
linkedin_url = "https://www.linkedin.com/in/lucca-libanori/"
github_url = "https://github.com/lucca-libanori"

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.subheader("E-mail")
        st.write(email)
        st.link_button("Enviar e-mail", f"mailto:{email}")

with col2:
    with st.container(border=True):
        st.subheader("LinkedIn")
        st.write("Lucca Libanori")
        st.link_button("Ver perfil", linkedin_url)

with col3:
    with st.container(border=True):
        st.subheader("GitHub")
        st.write("lucca-libanori")
        st.link_button("Ver perfil", github_url)