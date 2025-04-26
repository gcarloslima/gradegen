import random

def pop_inicial(periodos, tam_pop):
    """
    Cria uma população inicial de horários.
    
    Args:
        periodos (list): Lista de períodos com suas disciplinas
        tam_pop (int): Tamanho da população
        
    Returns:
        list: População inicial de horários
    """
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