import random


def selecao(populacao_total):
    """
    Seleciona dois indivíduos aleatórios da população,
    sendo o primeiro escolhido entre a metade melhor
    (com menor número de choques).

    Args:
        populacao_total (list): População total, já ordenada do menor para o maior número de choques.

    Returns:
        tuple: Dois indivíduos selecionados
    """
    metade_superior = populacao_total[:len(populacao_total) // 2]
    escolhido1 = random.choice(metade_superior)
    escolhido2 = random.choice(populacao_total)
    return escolhido1, escolhido2
