from .validate_exercises_examples import output_format, general_students_list

students_quantity = len(general_students_list)
def get_validate_exercise_prompt(num_questions: int):
    return f"""
    # Simulation Context
    You are an educational assessment specialist—but for each simulation, you will **role-play** 
    as one of the high-school students.

    # Role-Play Instruction
    For each student i (with ability θᵢ) and each question j:
    1. **Adopt the persona**
    ex: “I am a student with ability θᵢ = 0.6553. Based on my skill level, I will now think about the question and decide if I can answer it correctly.”
    2. **Provide an internal reasoning** (brief, hidden) like “I know this concept well” or “I struggle here,” 
       then choose your answer.
    3. **Emit only the final choice**: correct (1) or incorrect (0).

    # Inputs
    - Questions array (id, question, optional options)
    - Student abilities:
      {general_students_list}

    # Simulation Steps
      1. For each student i and question j:
         - Define c = 0.2  # 20% guessing chance for 5-option questions
         - Compute Pᵢⱼ = c + (1 − c) × sigmoid(θᵢ).
         - Generate a random number r between 0.0 (inclusive) and 1.0 (exclusive).
         - If r < Pᵢⱼ, mark correct (1); otherwise mark incorrect (0).

      2. Collect all responses into the JSON structure:  
         `{output_format}`

    # Output Requirements
    Return **only** the JSON—**no** extra text or explanations.

    """
