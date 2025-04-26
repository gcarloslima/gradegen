import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core.evolutionary.selection import selecao
from core.evolutionary.population import pop_inicial
from core.evaluation.fitness import avaliacao, ordenar
from core.utils import formatar_em_grade
from config.data import get_periodos_determinados

def display_schedule_table(horarios, title, subtitle=None):
    """Exibe uma tabela de horários com formatação adequada."""
    st.markdown(title)
    if subtitle:
        st.caption(subtitle)

    for p in range(5):
        inicio = p * 20
        fim = inicio + 20
        periodo_data = horarios[inicio:fim]
        st.markdown(f"### 📚 {p + 1}º Período")
        tabela = formatar_em_grade(periodo_data)
        st.dataframe(
            tabela.style.set_properties(**{
                'text-align': 'center',
                'white-space': 'pre-wrap',
                'font-size': '14px',
                'width': '1000px'
            }),
            use_container_width=True
        )
        st.markdown("---")

# Configuração da página
st.set_page_config(page_title="🧬 População Inicial", page_icon="🧬", layout="wide")
st.title("🧬 Gerador de População Inicial de Horários")
st.write("Crie e visualize diferentes combinações de horários organizados.")

# Controles de entrada
with st.sidebar:
    st.header("⚙️ Configurações")
    tam_pop_determinada = st.slider("Selecione o tamanho da população", 1, 100, 5)
    gerar = st.button("🚀 Gerar nova população")

if gerar:
    periodos = get_periodos_determinados()
    populacao = pop_inicial(periodos, tam_pop_determinada)

    populacao_com_choque = [{"horarios": individuo, "choques": avaliacao(individuo)} for individuo in populacao]
    populacao_ordenada = ordenar(populacao_com_choque)

    # Mostra indivíduos selecionados
    st.markdown("## 🎯 Seleção de Dois Indivíduos")

    escolhido1, escolhido2 = selecao(populacao_ordenada)

    with st.expander("👤 Primeiro Indivíduo - 🔥 Choques: " + str(escolhido1["choques"]), expanded=False):
        display_schedule_table(escolhido1["horarios"], "### 📅 Horários", "Melhor avaliação")

    with st.expander("👤 Segundo Indivíduo - 🔥 Choques: " + str(escolhido2["choques"]), expanded=False):
        display_schedule_table(escolhido2["horarios"], "### 📅 Horários", "Segunda melhor avaliação")

    # Separador
    st.markdown("---")
    st.markdown("## 👥 Visualização de Toda a População")
    st.caption("Todos os indivíduos gerados, ordenados por menor número de choques.")

    for idx, individuo in enumerate(populacao_ordenada):
        with st.expander(f"👤 Indivíduo {idx+1} - 🔥 Choques: {individuo['choques']}", expanded=False):
            display_schedule_table(
                individuo["horarios"],
                f"### 📅 Horários do Indivíduo {idx+1}"
            )
