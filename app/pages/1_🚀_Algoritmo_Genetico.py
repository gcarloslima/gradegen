from app.config.data import get_periodos_determinados
from app.core.evolutionary.genetic_algorithm import algoritmo_genetico
import streamlit as st

from app.core.utils import display_schedule_table

st.markdown("# 🚀 Algoritmo Genético - Otimizador de Horários")
st.sidebar.header("⚙️ Configurações do AG")

tam_pop = st.sidebar.slider("Tamanho da População", 2, 100, 10)
geracoes = st.sidebar.slider("Número de Gerações", 10, 500, 100)
taxa_mutacao = st.sidebar.slider("Taxa de Mutação (%)", 0, 100, 10) / 100

executar_ag = st.sidebar.button("🏁 Executar Algoritmo Genético")

if executar_ag:
    st.info("🔄 Executando AG, aguarde...")

    periodos = get_periodos_determinados()
    melhor_individuo = algoritmo_genetico(
        periodos,
        tam_pop=tam_pop,
        geracoes=geracoes,
        taxa_mutacao=taxa_mutacao
    )

    st.success(f"✅ Melhor Horário Encontrado com {melhor_individuo['choques']} choques!")

    display_schedule_table(
        melhor_individuo['horarios'],
        "## 🏆 Melhor Horário Gerado"
    )
