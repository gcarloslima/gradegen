import pandas as pd

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