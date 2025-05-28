# gradegen

Um gerador de horários baseado em algoritmo genético para instituições de ensino.

## 📂 Estrutura do Projeto

```
.
├── app/
│   └── pages/          # Páginas da aplicação Streamlit
│
├── core/
│   ├── evolutionary/   # Componentes do algoritmo genético
│   └── evaluation/     # Funções de avaliação de fitness
│
└── config/             # Arquivos de configuração e dados

```

## ⚙️ Instalação

1. Crie um ambiente virtual:
```bash
python -m venv .venv
```

2. Ative o ambiente virtual:
```bash
# No Windows
.venv\Scripts\activate

# No Unix ou MacOS
source .venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🚀 Executando a Aplicação

Para iniciar a aplicação Streamlit:

```bash
PYTHONPATH=. streamlit run app/Home.py
```

## ✨ Funcionalidades

- Otimização de horários baseada em algoritmos genéticos
- Detecção automática de conflitos entre professores
- Visualização interativa dos horários gerados
- Geração e avaliação de múltiplas populações

---

