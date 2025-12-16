from .validate_exercises_examples import output_format_prompt_c

def get_validate_exercise_prompt(questions: list, student_list: list) -> str:
    return f"""
QUESTION SIMULATION MODEL (3rd YEAR HIGH SCHOOL)

1. ABILITY SCALE:
   - Range: -3.0 (severe deficit) to 3.0 (excellence)
   - Reference points:
     • -3.0: 15–25% expected correct
     • 0.0: 45–55% expected correct
     • 3.0: 80–90% expected correct

2. DIFFICULTY FACTORS (calculated automatically):
   a) Text:
      • +0.1 per each 50 words beyond 100
      • +0.2 for historical/technical vocabulary
      • +0.3 for contextualization requirement
   b) Options:
      • +0.15 for each additional plausible distractor
      • +0.1 for similar terms among options
   c) Content:
      • +0.4 for requiring synthesis of multiple concepts
      • +0.25 for interdisciplinary relationships

3. RESPONSE MODEL:
   - Probability of correct = 1 / (1 + e^(-(ability - difficulty)))
   - Systematic errors:
     • 40% chance of choosing a plausible distractor
     • 15% chance of choosing an absurd option
     • Cognitive bias: preference for middle options (B, C, D)

4. INPUT:
   - List of student abilities
   - Question text followed by its options

5. REQUIRED OUTPUT:
   [1] List of selected options (A–E)  
   [2] Binary list of correct answers (0/1)  
   [3] Percentage correct (one decimal)  
   [4] Calculated question difficulty (scale –3.0 to 3.0)

###
STUDENT ABILITIES
{student_list}

###
QUESTIONS
{questions}

OUTPUT FORMAT
-------------
RETURN JSON WITH THE FOLLOWING STRUCTURE:

{output_format_prompt_c}
"""
