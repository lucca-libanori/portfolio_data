import os
import streamlit as st

st.set_page_config(page_title="Projetos | Lucca Libanori", layout="wide")

N_APOSTAS = "1.601"
ROI = "0,14%"
HIT_RATE = "47,46%"
MAX_DD = "63,94"

N_SIMS = "5.000"
DD_OBSERVADO = 69.81 
DD_MEDIANO = 49.62     
DD_P95 = 74.37         
PCT_PIOR = None        


def fmt(x):
    return f"{x:.2f}".replace(".", ",")


st.title("Projetos")

st.header("Plataforma de Análise de Performance")
st.caption("Python · Streamlit · PostgreSQL · SQLAlchemy · Pandas · NumPy · Plotly")

link_col, _ = st.columns([1, 3])
with link_col:
    st.link_button("🔗 Ver repositório no GitHub", "https://github.com/lucca-libanori/performance-analytics-platform")

st.markdown("---")

st.subheader("1. Problema")
st.write(f"""
Quem toma decisões recorrentes com capital em risco costuma olhar apenas o lucro
total e não sabe *de onde* vem o resultado nem *quanto risco* ele embute. As
perguntas que o projeto responde são: qual fonte ou categoria gera
retorno de forma consistente? Qual apenas acumula volatilidade? E o resultado
observado é desempenho ou apenas variância?

Os dados são de **apostas esportivas reais** ({N_APOSTAS} registros), usadas como caso de
uso. A arquitetura é adaptável a qualquer domínio com a mesma estrutura, como
trading e investimentos.
""")

st.subheader("2. Metodologia")
st.markdown("""
- **Ingestão e validação (ETL):** um script em Python lê o CSV, valida datas, odds,
  stakes e status, e rejeita registros inconsistentes com mensagens de erro
  específicas antes de qualquer inserção no banco.
- **Modelagem relacional:** schema PostgreSQL com restrições (CHECK em status,
  odds > 1 e stake > 0) e índices nas colunas mais filtradas.
- **Métricas de retorno:** Profit, ROI, Hit Rate e Stake total.
- **Métricas de risco:** Sharpe (lucro / desvio padrão), volatilidade *rolling* de
  7 dias, Max Drawdown e duração do drawdown, por Sportsbook, Esporte e faixa de
  odds (faixas configuráveis pelo usuário).
- **Simulação de Monte Carlo:** o histórico de apostas é reordenado milhares de vezes
  para estimar qual drawdown máximo é *normal* e comparar com o observado.
""")

st.subheader("3. Ferramentas")
st.markdown("""
- **Python** (Pandas, NumPy) para tratamento, métricas e simulação
- **PostgreSQL + SQLAlchemy** para armazenamento e consultas
- **Streamlit** para o dashboard multipage, com CRUD completo e modal de edição
- **Plotly** para visualizações interativas (curvas, áreas, histogramas)
""")


st.subheader("4. Resultados")

k1, k2, k3, k4 = st.columns(4)
k1.metric("Apostas analisadas", N_APOSTAS)
k2.metric("ROI", ROI)
k3.metric("Hit Rate", HIT_RATE)
k4.metric("Max Drawdown", f"-{MAX_DD}u")

img_col1, img_col2 = st.columns(2)
with img_col1:
    st.image("assets/bankroll_over_time.png", use_container_width=True)
    st.caption("Evolução da banca ao longo do tempo (lucro acumulado vs. diário)")
with img_col2:
    st.image("assets/total_risk_vs_return.png", use_container_width=True)
    st.caption("ROI acumulado vs. volatilidade rolling: retorno e risco lado a lado")

if os.path.exists("assets/risk_simulation.png"):
    dd_col, sim_col = st.columns(2)
    with dd_col:
        st.image("assets/drawdown.png", use_container_width=True)
        st.caption("Drawdown ao longo do tempo: distância entre o resultado atual e o melhor momento histórico")
    with sim_col:
        st.image("assets/risk_simulation.png", use_container_width=True)
        st.caption("Simulação de Monte Carlo: distribuição do drawdown máximo vs. o drawdown observado")
else:
    st.image("assets/drawdown.png", use_container_width=True)
    st.caption("Drawdown ao longo do tempo: distância entre o resultado atual e o melhor momento histórico")

if DD_OBSERVADO > DD_P95:
    leitura = ("o drawdown observado ficou além do percentil 95, ou seja, foi pior do que "
               "a variância costuma produzir (azar incomum ou apostas menos independentes "
               "do que o modelo assume)")
elif DD_OBSERVADO > DD_MEDIANO:
    leitura = ("o drawdown observado ficou acima da mediana, mas abaixo do percentil 95: "
               "foi um período ruim, ainda dentro do que a variância sozinha explica")
else:
    leitura = "o drawdown observado ficou abaixo da mediana, um caminho mais suave que o típico"

pct_txt = ""
if PCT_PIOR is not None:
    pct_txt = f" Em {PCT_PIOR:.1f}% das simulações o drawdown foi igual ou pior que o observado."

sim_txt = (f" Para testar se esse tombo foi azar, as apostas foram reordenadas aleatoriamente "
           f"{N_SIMS} vezes (Monte Carlo): o drawdown mediano simulado foi de -{fmt(DD_MEDIANO)}u e o "
           f"percentil 95 de -{fmt(DD_P95)}u. Medido aposta a aposta, o drawdown real foi de "
           f"-{fmt(DD_OBSERVADO)}u; {leitura}.{pct_txt}")

with st.container(border=True):
    st.markdown("**Conclusão**")
    st.write(f"""
Em {N_APOSTAS} apostas, o ROI ficou próximo de zero ({ROI}), com Hit Rate de {HIT_RATE} e
drawdown máximo de -{MAX_DD}u no dashboard.{sim_txt}

O resultado é compatível com uma estratégia de retorno neutro. O dashboard permite
identificar onde o desempenho foi melhor ou pior (por sportsbook, esporte e faixa de
odds), mas esse volume ainda não basta para separar habilidade de variância.
Próximos passos: intervalo de confiança do ROI por bootstrap e CLV (*closing line
value*) como métrica de qualidade menos ruidosa que o lucro.
""")

st.markdown("---")

with st.container(border=True):
    st.subheader("Próximos projetos")
    st.write("""
    Estou desenvolvendo um sistema de gestão financeira pessoal, que deve entrar aqui assim
    que atingir um estágio apresentável.
    """)