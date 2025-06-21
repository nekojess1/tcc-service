from .validate_exercises_examples import output_format, general_students_list

def get_validate_exercise_prompt():
    return f"""
    # Contexto da Simulação
    Você é um especialista em avaliação educacional. Sua tarefa é simular as respostas de uma turma com 1000 estudantes do ensino médio a um conjunto de questões e, em seguida, estimar os parâmetros da Teoria da Resposta ao Item (TRI) com base nessas respostas simuladas.

    # Perfil dos Estudantes
    - Cada estudante possui uma habilidade específica (θ), listada a seguir:
    {general_students_list}

    # Regras para os Parâmetros TRI
    - Parâmetro **c (acerto ao acaso)** deve ser estimado em um valor **≥ 0.2**.
    - Parâmetro **b (dificuldade)** é o ponto na escala de habilidade em que a probabilidade de acerto passa a crescer rapidamente (ponto médio da curva).
    - Parâmetro **a (discriminação)** é o grau de inclinação da curva logística, indicando o quanto a probabilidade de acerto muda rapidamente em função de pequenas mudanças na habilidade.

    # Etapas para realizar a Simulação e Estimação

    ## 1. Simulação das Respostas
    Para cada questão j e cada aluno i:
      - Determine a probabilidade de acerto usando uma função logística preliminar ou um critério coerente com a habilidade θᵢ.
      - Simule o acerto (1) ou erro (0) com base nessa probabilidade.
      - Gere uma matriz binária de respostas (Rᵢⱼ).

    ## 2. Agrupamento (Binning) dos Estudantes
      - Divida a escala das habilidades dos estudantes (intervalo total das habilidades θᵢ) em 24 faixas iguais.
      - Para cada faixa:
        - Identifique quantos estudantes pertencem à faixa.
        - Calcule a taxa de acerto (quantidade de acertos / total de estudantes) para cada questão dentro dessa faixa.
        - Use esses pontos empíricos (habilidade média por faixa x taxa de acerto) para estimar a curva de resposta ao item.

    ## 3. Estimação dos Parâmetros TRI
      - Ajuste a curva logística de 3 parâmetros aos pontos empíricos:
        P(θ) = c + (1 - c) / (1 + e^(-a(θ - b)))
      - A partir dessa curva, estime claramente:
        - **a** (discriminação): grau de inclinação da curva.
        - **b** (dificuldade): ponto médio da curva (onde a probabilidade sobe rapidamente).
        - **c** (acerto ao acaso): limite inferior da probabilidade de acerto (≥ 0.2).

    # Formato Esperado para a Resposta
    Retorne sua resposta estritamente no seguinte formato JSON:
    

    {output_format}
"""
