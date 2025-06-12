def get_validate_elementary_students_exercises_prompt():
    return """
# Contexto da Simulação
Você é um especialista em educação que irá simular uma turma com 10 estudantes do ensino fundamental com habilidades muito baixas em leitura, interpretação e ciências humanas. Esses estudantes responderão às questões fornecidas, e sua tarefa é estimar os parâmetros da Teoria da Resposta ao Item (TRI) com base nas respostas.

# Perfil dos Estudantes
- As habilidades dos alunos (θ) devem ser geradas a partir de uma distribuição normal com:
  - Média: -2.5
  - Desvio padrão: 0.5
- As habilidades devem estar no intervalo de -3.0 até -2.0.

# Regras para os Parâmetros TRI
- O valor de **c (acerto ao acaso)** deve ser **≥ 0.2**
- A dificuldade **b** será estimada com base na habilidade onde a curva de acerto cresce.
- A discriminação **a** deve refletir o quanto a probabilidade de acerto muda em função da habilidade.

# Passos para Simulação

1. **Geração de habilidades**
   - Gere 10 valores de θᵢ simulando as habilidades dos alunos com base no perfil acima.

2. **Simulação de Respostas**
   - Para cada questão j e cada aluno i, simule se o aluno acertaria ou erraria com base em sua habilidade θᵢ.
   - Gere a matriz de respostas binárias Rᵢⱼ (com valores 1 para acerto, 0 para erro).

3. **Divida os alunos em faixas de habilidade (binning)**
   - Defina de 5 a 7 faixas igualmente espaçadas no intervalo de habilidade dos alunos (ex: de –3 a 3).
   - Para cada faixa:
     - Calcule a quantidade total de alunos com θᵢ naquela faixa.
     - Calcule a quantidade de acertos daquela questão na faixa.
     - Calcule a taxa de acertos (de 0 a 1).
   - Utilize esses pontos de taxa por faixa como base empírica para estimar a curva da questão.

4. **Estimação dos Parâmetros TRI**
   - Utilize as proporções de acerto por faixa para ajustar uma curva logística de 3 parâmetros:
     \[
     P(θ) = c + \\frac{1 - c}{1 + e^{-a(θ - b)}}
     \]
   - A partir da curva ajustada, estime:
     - **a**: parâmetro de discriminação
     - **b**: parâmetro de dificuldade
     - **c**: parâmetro de acerto ao acaso

# Formato Esperado da Resposta
Retorne os dados no seguinte formato JSON:

```json
{
  "questions": [
    {
      "id": "identificador_questao",
      "parameters_tri": {
        "parameter_a": valor,
        "parameter_b": valor,
        "parameter_c": valor
      }
    }
  ],
  "students": [
    {
      "id": "id_estudante",
      "nivel_habilidade": valor
    },
    ...
  ]
}
"""