from api.models.prompts.exercises.exercises_examples import input_format, output_format, output_example
from api.models.prompts.exercises.exercises_instructions import context

def get_exercise_prompt():
    """Generate an exercise with different subjects"""
    return f"""
        {context}

        Input format:

        {input_format}

        Output format:

        {output_format}

        Return the exercise in JSON format.


        """
