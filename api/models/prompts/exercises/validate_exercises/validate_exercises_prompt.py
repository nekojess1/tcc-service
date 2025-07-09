from .validate_exercises_examples import output_format, general_students_list

students_quantity = len(general_students_list)

def get_validate_exercise_prompt(num_questions: int, student_list: list) -> str:
    return f"""
   # Context
   You are an expert in educational assessment. Your role is to simulate each student’s response based on their ability level (θ).

   # Input Parameters
   - Number of questions: {num_questions}
   - List of students with ability levels:
   {student_list}

   # Simulation Rules
   1. Assign each question a difficulty level between −3 and +3.
   2. For each student:
      - Use this persona template:
      "I am a student with ability θ = 0.6553. Given my ability and the question’s difficulty, I will answer the question."
   3. If the student doesn’t know the answer, they have a 20% chance to guess correctly.
   4. For each question, record:
      - `1` for correct
      - `0` for incorrect

   # Output Format
   Return **only** a JSON object matching this schema:
   {output_format}

   > Do **not** include any additional text—only the JSON results.
   """
