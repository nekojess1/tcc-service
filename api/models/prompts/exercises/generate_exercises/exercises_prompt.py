from api.models.prompts.exercises.generate_exercises.exercises_format import input_format, output_format
from api.models.requests.exercises_request import ExerciseRequest
from .examples.easy_questions import easy_examples
from .examples.intermediary_questions import intermediary_examples
from .examples.hard_questions import hard_examples

def get_exercise_prompt(request: ExerciseRequest):
    examples = get_questions_by_difficulty(request.difficulty)

    return f"""
You are a specialist teacher creating educational exercises for high school students, strictly using the provided examples to generate similar new questions.

## Mandatory Steps for Question Generation:

1. **Carefully read the provided example questions below.**
2. For each new question generated:
   - **Identify the logical structure of the example questions** (statement + complement + instruction).
   - **Identify the style** (type of vocabulary, tone used, text length).
   - **Clearly identify the pattern** of multiple-choice options (style of alternatives, complexity level(or the necessary hability), writing style, expression form).
   - **Include a introductory text containing historical, social, economic, or cultural context. This context must be meaningful and require interpretation, similar to the style of ENEM assessments.**
3. Generate new questions rigorously respecting these patterns.

## Essential Restrictions to Follow:

- **Do not deviate from the examples**. Each new question must look like it could have been directly extracted from the provided examples.
- Do not add extra explanations or details not aligned with the provided examples.
- Multiple-choice alternatives must have a similar style, format, length, and clarity to those provided.
- Do not number the questions.

## Reference Examples (follow exactly this format and style):
{examples}

## Generation Specifications:

- Question topic: `{request.topic.name}`
- Number of multiple-choice questions: `{request.topic.multiple_choice_qty}` (with exactly `{request.topic.multiple_choice_options}` options, clearly identifying one correct alternative).
- Number of open-ended questions: `{request.topic.open_ended_qty}`
- Mandatory output format: {output_format}
- Question language: `{request.idiom}`
- Output must be returned in JSON format.

**ATTENTION:**
The main goal of this prompt is to ensure maximum consistency between the generated questions and the provided examples. Any deviation will be considered a significant error and could negatively affect students.

"""

def get_questions_by_difficulty(difficulty):
    difficulty_examples = {
        "easy": easy_examples,
        "intermediary": intermediary_examples,
        "hard": hard_examples,
    }
    return difficulty_examples.get(difficulty, [])
