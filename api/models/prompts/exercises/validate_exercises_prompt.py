from api.models.prompts.exercises.validate_exercises_examples import input_format, output_format, output_example, input_example
from api.models.prompts.exercises.validate_exercises_instructions import context

def get_validate_exercise_prompt():
    """Generate an exercise with different subjects"""
    return f"""
        {context}

        Input format:

        {input_format}

        Output format:

        {output_format}

        Return the exercise in JSON format.

        Example filled return:

        {output_example}
        
        Example filled input:
        
        {input_example}
        """
