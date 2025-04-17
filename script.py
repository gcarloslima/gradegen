import streamlit as st
import random
import pandas as pd
from pprint import pprint

def avaliacao(individuo):
    choque = 0
    for h in range(0, 20):
        for i in range(0, 5):
            for j in range(0, 4 - i):
                if individuo[i * 20 + h]["professor"] == individuo[i * 20 + ((j + 1) * 20) + h]["professor"]:
                    choque += 1

    return choque


def pop_inicial(periodos, tam_pop):
    pop = [[{} for _ in range(100)] for _ in range(tam_pop)]
    for k in range(tam_pop):
        j = 0
        for periodo in periodos:
            aux = []
            for disciplina in periodo:
                aux.extend([disciplina] * 4)
            random.shuffle(aux)
            for s in aux:
                pop[k][j] = s
                j += 1
    return pop


def formatar_em_grade(lista_20_disciplinas):
    dias = ['SEG', 'TER', 'QUA', 'QUI', 'SEX']
    grade = {dia: [] for dia in dias}

    for i, dia in enumerate(dias):
        for j in range(4):
            d = lista_20_disciplinas[i * 4 + j]
            texto = f"{d['nome']}\n({d['professor']})"
            grade[dia].append(texto)

    return pd.DataFrame(grade)


# Dados
disciplinas = [
    "Introdução à Programação", "Matemática Discreta", "Algoritmos", "Fundamentos de Sistemas de Informação", "Comunicação e Expressão",
    "Programação Orientada a Objetos", "Cálculo I", "Banco de Dados I", "Arquitetura de Computadores", "Sociologia",
    "Estrutura de Dados", "Engenharia de Software I", "Cálculo II", "Banco de Dados II", "Contabilidade",
    "Redes de Computadores", "Sistemas Operacionais", "Engenharia de Software II", "Estatística", "Ética e Cidadania",
    "Inteligência Artificial", "Compiladores", "Computação Gráfica", "Gestão de Projetos", "Trabalho de Conclusão de Curso"
]

professores = [
    "Prof. Ana Martins", "Prof. Carlos Souza", "Prof. Beatriz Lima", "Prof. João Oliveira", "Prof. Larissa Costa",
    "Prof. Pedro Ribeiro", "Prof. Fernanda Rocha", "Prof. Marcelo Andrade", "Prof. Aline Duarte", "Prof. Rafael Nunes"
]

todas_disciplinas = [
    {"nome": disciplina, "professor": professores[i % len(professores)]}
    for i, disciplina in enumerate(disciplinas)
]



periodos_determinados = [
    todas_disciplinas[0:5],
    todas_disciplinas[5:10],
    todas_disciplinas[10:15],
    todas_disciplinas[15:20],
    todas_disciplinas[20:25],
]

st.set_page_config(page_title="População Inicial", layout="wide")
st.title("🧬 Gerador de População Inicial de Horários")


tam_pop_determinada = st.slider("Tamanho da população", 1, 100, 5)

if st.button("Gerar população"):
    populacao = pop_inicial(periodos_determinados, tam_pop_determinada)

    populacao_com_choque = [ { "horarios": individuo, "choques": avaliacao(individuo) } for individuo in populacao ]

    for idx, individuo in enumerate(populacao_com_choque):
        st.markdown(f"## 👤 Indivíduo {idx+1} - Choques: {individuo["choques"]}")

        for p in range(5):
            inicio = p * 20
            fim = inicio + 20
            periodo_data = individuo["horarios"][inicio:fim]
            st.markdown(f"### 🗓️ {p+1}º Período")
            tabela = formatar_em_grade(periodo_data)
            st.dataframe(
                tabela.style.set_properties(**{
                    'text-align': 'center',
                    'white-space': 'pre-wrap',
                    'font-size': '13px',
                    'width': '1000px'
                }),
                use_container_width=True
            )

        st.markdown("---")
