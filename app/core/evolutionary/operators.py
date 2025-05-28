import random

from app.core.evaluation.fitness import avaliacao


def cruzamento(pai1, pai2):
    """
    Realiza o cruzamento entre dois indivíduos (horários).
    Usa ponto de corte único.

    Args:
        pai1 (dict): Primeiro indivíduo {'horarios': [...], 'choques': int}
        pai2 (dict): Segundo indivíduo {'horarios': [...], 'choques': int}

    Returns:
        tuple: Dois filhos gerados a partir dos pais
    """
    corte = random.randint(1, len(pai1['horarios']) - 2)

    filho1_horarios = pai1['horarios'][:corte] + pai2['horarios'][corte:]
    filho2_horarios = pai2['horarios'][:corte] + pai1['horarios'][corte:]

    return (
        {"horarios": filho1_horarios, "choques": avaliacao(filho1_horarios)},
        {"horarios": filho2_horarios, "choques": avaliacao(filho2_horarios)}
    )

def mutacao(individuo, taxa_mutacao=0.1):
    """
    Realiza mutação em um indivíduo trocando dois genes com uma determinada probabilidade.

    Args:
        individuo (dict): Indivíduo {'horarios': [...], 'choques': int}
        taxa_mutacao (float): Probabilidade de ocorrer a mutação (0 a 1)

    Returns:
        dict: Indivíduo possivelmente modificado
    """
    horarios = individuo['horarios'][:]
    if random.random() < taxa_mutacao:
        i, j = random.sample(range(len(horarios)), 2)
        horarios[i], horarios[j] = horarios[j], horarios[i]
    return {"horarios": horarios, "choques": avaliacao(horarios)}
