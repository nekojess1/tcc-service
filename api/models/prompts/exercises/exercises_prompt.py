from api.models.prompts.exercises.exercises_examples import input_example, output_example
from api.models.prompts.exercises.exercises_instructions import context

def get_exercise_prompt():
    """Generate an exercise with different subjects"""
    return f"""
{context}

# Exemplo de Entrada: 

{input_example}

# Exemplo de Retorno JSON:

{output_example}
"""
