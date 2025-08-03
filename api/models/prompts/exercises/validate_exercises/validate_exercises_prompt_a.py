from .validate_exercises_examples import output_format, general_students_list

students_quantity = len(general_students_list)

def get_validate_exercise_prompt(num_questions: int, student_list: list) -> str:
    return f"""
   # Context
   You are an expert in educational assessment. Your task is to simulate each student’s responses to ENEM-style multiple-choice questions based on their ability level (θ).

   # Input Parameters
   - List of students with ability levels:
   {student_list}

   # Simulation Rules
   1. **Question Difficulty (b):**  
      Assign each question a difficulty rating on a scale from −3 (very easy) to +3 (very hard).  
   2. **Student Response:**  
      For each student _i_, simulate their answer based on ability θᵢ and the question’s difficulty.  
   3. **Guessing Behavior:**  
      If the student appears not to know the answer, assume a 20% chance of guessing correctly.  
   4. **Recording Results:**  
      For each question, output:
      - `1` = correct  
      - `0` = incorrect 
       
   The list of student answers must strictly follow the same order as the input questions to ensure proper alignment between each response and its corresponding question.

   # Output Format
   
   Return **only** a JSON object conforming to this schema:
   {output_format}

   > **Do not** include any additional text—output strictly the JSON.
- A ordem das respostas deve corresponder exatamente à ordem das perguntas.
- Cada array `"answers"` deve conter exatamente {num_questions} elementos.
   """
