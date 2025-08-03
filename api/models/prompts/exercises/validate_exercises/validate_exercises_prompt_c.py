from .validate_exercises_examples import output_format_prompt_c

def get_validate_exercise_prompt(questions: list, student_list: list) -> str:
    return f"""
MODELO DE SIMULAÇÃO DE QUESTÕES (3º ANO EM)

1. ESCALA DE HABILIDADE:
   - Faixa: -3.0 (defasagem grave) a 3.0 (excelência)
   - Pontos de referência:
     • -3.0: 15-25% de acerto esperado
     • 0.0: 45-55% de acerto esperado
     • 3.0: 80-90% de acerto esperado

2. FATORES DE DIFICULDADE (calculados automaticamente):
   a) Texto:
      • +0.1 por 50 palavras extras além de 100
      • +0.2 por vocabulário histórico/técnico
      • +0.3 por exigência de contextualização
   b) Alternativas:
      • +0.15 por distrator plausível adicional
      • +0.1 por termos similares entre alternativas
   c) Conteúdo:
      • +0.4 por exigência de síntese de múltiplos conceitos
      • +0.25 por relações interdisciplinares

3. MODELO DE RESPOSTA:
   - Probabilidade de acerto = 1 / (1 + e^(-(habilidade - dificuldade)))
   - Erros sistemáticos:
     • 40% de chance de escolher distrator plausível
     • 15% de chance de escolher alternativa absurda
     • Viés cognitivo: preferência por alternativas médias (B, C, D)

4. ENTRADA
  - Lista de habilidades do estudante
  - Texto da questão seguido das suas opções 

5. SAÍDA OBRIGATÓRIA:
   [1] Lista com alternativas escolhidas (A-E)
   [2] Lista binária de acertos (0/1)
   [3] Percentual de acerto (1 decimal)
   [4] Dificuldade calculada da questão (escala -3.0 a 3.0)
###
HABILIDADES
{student_list}

###
QUESTÕES
{questions}

FORMATO DE SAÍDA
-------------
RETORNE EM JSON COM A SEGUINTE ESTRUTURA:

{output_format_prompt_c}
"""


