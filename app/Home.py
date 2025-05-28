import streamlit as st

st.set_page_config(
    page_title="GradeGen - Gerador de Horários",
    page_icon="📅",
    layout="wide"
)

st.title("📅 GradeGen")
st.subheader("Um gerador de horários inteligente para instituições de ensino")

st.markdown("---")

st.markdown(
    """
    🎯 **GradeGen** é uma aplicação que utiliza **algoritmos genéticos** para otimizar 
    a geração de horários escolares, garantindo menos conflitos e maior eficiência.

    #### 🔧 Funcionalidades principais:
    - ✅ Otimização de horários baseada em algoritmos genéticos
    - ✅ Detecção automática de conflitos entre professores
    - ✅ Visualização interativa dos horários gerados
    - ✅ Geração e avaliação de múltiplas populações

    ---
    """
)

st.info(
    "👈 Use o menu lateral para acessar as funcionalidades."
)

st.markdown(
    """
    #### 🚀 Como começar?
    1. Configure os parâmetros do algoritmo.
    2. Execute a geração dos horários.
    3. Visualize, analise e exporte os resultados.
    """
)

st.markdown("---")

st.caption("Desenvolvido com ❤️ por GradeGen")
