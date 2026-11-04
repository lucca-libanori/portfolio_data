import streamlit as st

st.set_page_config(page_title="Sobre mim | Lucca Libanori", layout="wide")

st.title("Sobre mim")

st.write("""
Sou formado em Ciência da Computação pela PUCPR e estou em transição para a área de
Data Analytics. Tive interesse em dados ao perceber que conceitos que eu já usava na prática, como
probabilidade, risco e retorno e variância, são a base da análise de dados, e quis aprofundar
meus estudos com eles com método. Minha base em programação e em tratamento de dados
(APIs, JSON) me ajuda a lidar com os dados da coleta até a análise.
""")

st.write("""
Meu principal projeto é uma plataforma de análise de performance feita de ponta a ponta:
ETL em Python, banco PostgreSQL e dashboard interativo com métricas de retorno e risco
(ROI, Sharpe, drawdown). Usei uma simulação de Monte Carlo para testar se um resultado
ruim era azar ou variância normal, e concluí com os dados em vez de forçar uma narrativa.
Ele me mostrou a diferença entre um resultado parecer bom e ser estatisticamente
sustentável. Também estou desenvolvendo um sistema de gestão financeira pessoal que irei publicar quando estiver mais desenvolvido.
""")

st.write("""
Busco uma oportunidade como Data Analyst para aplicar essa base técnica e o meu cuidado
em interpretar os dados com honestidade.
""")

st.subheader("Skills")

st.markdown("""
- **Análise e linguagens:** Python (Pandas, NumPy), SQL
- **Banco de dados:** PostgreSQL
- **Visualização:** Streamlit, Plotly, Power BI, Excel
- **Estatística aplicada:** métricas de risco e retorno, simulação de Monte Carlo
- **Ferramentas:** Git/GitHub
""")