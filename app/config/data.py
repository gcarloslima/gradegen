disciplinas = [
    "Introdução à Programação", "Matemática Discreta", "Algoritmos", "Fundamentos de Sistemas de Informação", "Comunicação e Expressão",
    "Programação Orientada a Objetos", "Cálculo I", "Banco de Dados I", "Arquitetura de Computadores", "Sociologia",
    "Estrutura de Dados", "Engenharia de Software I", "Cálculo II", "Banco de Dados II", "Contabilidade",
    "Redes de Computadores", "Sistemas Operacionais", "Engenharia de Software II", "Estatística", "Ética e Cidadania",
    "Inteligência Artificial", "Compiladores", "Computação Gráfica", "Gestão de Projetos", "Trabalho de Conclusão de Curso"
]

professores = [
    "Prof. Ana Martins", "Prof. Carlos Souza", "Prof. Beatriz Lima", "Prof. João Oliveira", "Prof. Larissa Costa",
    "Prof. Pedro Ribeiro", "Prof. Fernanda Rocha", "Prof. Marcelo Andrade", "Prof. Aline Duarte", "Prof. Rafael Nunes"
]

def get_todas_disciplinas():
    """
    Retorna uma lista de todas as disciplinas com seus respectivos professores.
    
    Returns:
        list: Lista de dicionários contendo informações de disciplina e professor
    """
    return [
        {"nome": disciplina, "professor": professores[i % len(professores)]}
        for i, disciplina in enumerate(disciplinas)
    ]

def get_periodos_determinados():
    """
    Retorna os períodos predefinidos com suas disciplinas.
    
    Returns:
        list: Lista de períodos com suas disciplinas
    """
    todas_disciplinas = get_todas_disciplinas()
    return [
        todas_disciplinas[0:5],
        todas_disciplinas[5:10],
        todas_disciplinas[10:15],
        todas_disciplinas[15:20],
        todas_disciplinas[20:25],
    ] 