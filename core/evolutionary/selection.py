import random

def selecao(populacao_total):
    """
    Seleciona dois indivíduos aleatórios da população.
    
    Args:
        populacao_total (list): A população total
        
    Returns:
        tuple: Dois indivíduos selecionados
    """
    escolhido1, escolhido2 = random.sample(populacao_total, 2)
    return escolhido1, escolhido2 