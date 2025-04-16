# Gerador de População Inicial de Horários

Este projeto gera uma população inicial de horários acadêmicos distribuídos em 5 períodos, onde cada disciplina é associada a um professor.

## 🚀 Funcionalidades

- Geração de população com número configurável de indivíduos
- Distribuição aleatória de disciplinas por indivíduo
- Interface simples e interativa em navegador
- Visualização tabular dos indivíduos gerados

## 🛠️ Tecnologias

- Python 3.8+
- Streamlit
- Pandas

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/gcarloslima/gradegen.git
cd gradegen
```

### 2. Crie o ambiente virtual e instale as dependências

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate no Windows
pip install -r requirements.txt
```
Recomendado: use um ambiente virtual.

### 3. Inicie a aplicação com o Streamlit

```bash
streamlit run script.py
```
O navegador será aberto automaticamente com a interface, geralmente em http://localhost:8501.