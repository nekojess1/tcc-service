from api.models.prompts.exercises.validate_exercises.validate_exercises_examples import input_format, output_format, output_example, input_example
from api.models.prompts.exercises.validate_exercises.validate_exercises_instructions import context as generic_context
from api.models.prompts.exercises.validate_exercises.validate_exercises_instructions_adjusted import context as guided_context


def get_validate_elementary_students_exercises_prompt():
    return """
# Contexto da Simulação
Você é um especialista em educação que vai simular uma turma com 50 estudantes de ensino fundamental que não possuem nenhum conhecimento em ciências humanas e nem sabem ler.
Esses alunos responderão às questões recebidas.

# Perfil dos Alunos
- Média da habilidade (θ): aproximadamente -2.
- Desvio padrão da habilidade (θ): 0,5.

# Passos para Simulação
1. **Defina 20 valores de habilidade** θᵢ para cada aluno (i=1…50).  
2. **Simule respostas**  
  - Para cada questão j e cada aluno i, use o nível de habilidade dele para tentar responder a pergunta. 
  - Simule que você seja esse aluno e tente responder a pergunta. 
  - Gere a matriz de respostas binárias Rᵢⱼ
3. **Estime os parâmetros TRI**  
   - Com a matriz de respostas R (50×Q) e os 50 valores de θ, aplique método de máxima verossimilhança marginal para estimar, para cada questão j:  
     - **a_j** (discriminação)  
     - **b_j** (dificuldade)  
     - **c_j** (chance de acerto ao acaso)

# Formato do Retorno
Retorne uma lista estruturada da seguinte forma:

```json
{
  "questions": [
    {
      "id": "identificador_questao",
      "parameters_tri": {"parameter_a": valor, "parameter_b": valor, "parameter_c": valor}
    },
    ...
  ],
  "students": [
    "id": "id_estudante",
    "nivel_habilidade": "habilidade_estudante" 
  ]
}
'''

"""
