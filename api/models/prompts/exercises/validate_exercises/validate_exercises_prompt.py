from .validate_exercises_examples import output_format, general_students_list

students_quantity = len(general_students_list)

def get_validate_exercise_prompt(num_questions: int, student_list: list):
    return f"""
# Simulation Context
You are an educational assessment specialist performing a simulation. For each question, you will **role-play** as a high-school student with a specific ability (θ).

# Role-Play Instructions
For each student and question:
1. **Adopt the student's persona explicitly**:
   Example: "I am a student with ability θ = 0.6553. Given my ability level, I will attempt to answer question j."

2. **Internally reason your likelihood of answering correctly**, considering:
   - If uncertain about the answer, you may **simulate a guess**, reflecting real-world student behavior.
   - Even if you have high ability, remember you are not perfect; there is always at least a 10% chance you might make a mistake due to distractions, confusion, or uncertainty.
   - If your ability clearly matches or slightly exceeds the difficulty of the question, you have a high chance of being correct (around 80-90%), but not guaranteed.
   - If your ability is below the question's difficulty, you have only a **20% chance of guessing correctly** (1 correct option out of 5).
   - If ability is less than difficulty, answer correctly only with a 20% guessing chance.

3. **Emit only the final choice**:
   - Correct answer: 1
   - Incorrect answer: 0

# Inputs
- **Questions**: An array containing objects with the fields `(id, question, options)`.
- **Student abilities**:
  {student_list}

# Simulation Steps
1. For each student `i` (ability θᵢ) and each question `j`:
   - Simulate realistically, considering both skill level and occasional mistakes.

2. Collect all simulated responses into the provided JSON structure:
  {output_format}

# Output Requirements
- Respond exclusively with the JSON object containing the simulated answers.
- Provide **no** additional text, comments, or explanations.
"""
