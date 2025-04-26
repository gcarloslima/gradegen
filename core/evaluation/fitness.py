def avaliacao(individuo):
    """
    Avalia a aptidão de um indivíduo (horário) com base em conflitos de professores.
    
    Args:
        individuo (list): O horário individual a ser avaliado
        
    Returns:
        int: Número de conflitos (quanto menor, melhor)
    """
    choque = 0
    for i in range(0, 20):
        for j in range(0, 5):
            for k in range(0, 4 - j):
                if individuo[j * 20 + i]["professor"] == individuo[j * 20 + ((k + 1) * 20) + i]["professor"]:
                    choque += 1
    return choque

def ordenar(populacao_nao_ordenada):
    """
    Ordena a população com base no número de choques.
    
    Args:
        populacao_nao_ordenada (list): População a ser ordenada
        
    Returns:
        list: População ordenada por número de choques
    """
    return sorted(populacao_nao_ordenada, key=lambda individuo: individuo["choques"]) 