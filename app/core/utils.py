import pandas as pd
import streamlit as st

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


def formatar_em_grade(lista_20_disciplinas):
    """
    Formata uma lista de disciplinas em uma tabela de horários.
    
    Args:
        lista_20_disciplinas (list): Lista de disciplinas
        
    Returns:
        pd.DataFrame: Tabela de horários formatada
    """
    dias = ['SEG', 'TER', 'QUA', 'QUI', 'SEX']
    grade = {dia: [] for dia in dias}

    for i, dia in enumerate(dias):
        for j in range(4):
            d = lista_20_disciplinas[i * 4 + j]
            texto = f"{d['nome']}\n({d['professor']})"
            grade[dia].append(texto)

    return pd.DataFrame(grade) 