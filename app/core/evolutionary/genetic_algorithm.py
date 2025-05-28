from app.core.evaluation.fitness import avaliacao, ordenar
from app.core.evolutionary.operators import cruzamento, mutacao
from app.core.evolutionary.population import pop_inicial
from app.core.evolutionary.selection import selecao


def algoritmo_genetico(periodos, tam_pop=10, geracoes=50, taxa_mutacao=0.1):
    """
    Executa o algoritmo genético para gerar o melhor horário possível.

    Args:
        periodos (list): Lista dos períodos com disciplinas
        tam_pop (int): Tamanho da população
        geracoes (int): Quantidade de gerações
        taxa_mutacao (float): Taxa de mutação

    Returns:
        dict: Melhor indivíduo encontrado
    """
    # População inicial
    pop = pop_inicial(periodos, tam_pop)
    populacao = [{"horarios": ind, "choques": avaliacao(ind)} for ind in pop]
    populacao = ordenar(populacao)

    for _ in range(geracoes):
        nova_pop = []

        while len(nova_pop) < tam_pop:
            pai1, pai2 = selecao(populacao)
            filho1, filho2 = cruzamento(pai1, pai2)
            filho1 = mutacao(filho1, taxa_mutacao)
            filho2 = mutacao(filho2, taxa_mutacao)
            nova_pop.extend([filho1, filho2])

        populacao = ordenar(nova_pop[:tam_pop])

    melhor = populacao[0]
    return melhor
