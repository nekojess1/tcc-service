from api.models.prompts.exercises.generate_exercises.exercises_format import input_format, output_format
from api.models.prompts.exercises.generate_exercises.exercises_instructions import context
from .examples.easy_questions import easy_examples
from .examples.intermediary_questions import intermediary_examples
from .examples.hard_questions import hard_examples

def get_exercise_prompt(difficulty, idiom):
    """Generate an exercise with different subjects"""
    return f"""
        {context}

        Input format:

        {input_format}

        Output format:

        {output_format}

        Questions example: {get_questions_by_difficulty(difficulty)}
        
        Return the exercise in JSON format.

        The output must be in {idiom} language.

        """

def get_questions_by_difficulty(difficulty):
    mapping = {
        "easy": easy_examples,
        "intermediary": intermediary_examples,
        "hard": hard_examples,
    }
    return mapping[difficulty]
  