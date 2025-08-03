from .validate_exercises_examples import output_format


def get_validate_exercise_prompt(questions: list, student_list: list) -> str:
    return f"""
   # Context
   You are a psychometrics and educational assessment expert simulating student responses to ENADE-style questions in the area of Ciencias Humanas. These questions are designed to assess knowledge and skills consolidated in Brazilian high school education, aligned with the BNCC (Base Nacional Comum Curricular), focusing on:

- Interpretation and critical analysis of historical, geographic, political, philosophical, and sociological contexts.
- Reading comprehension, textual interpretation, and argument evaluation.
- Use of conceptual and procedural knowledge in real-world and sociohistorical problem situations.

INPUT PARAMETERS
----------------
- student_list: A list of students, each with a latent trait score (ability level) θᵢ, typically ranging from −3 to +3:
    θ ≤ −2          : insufficient mastery of high school content
    −2 < θ ≤ 0       : partial mastery
    0 < θ ≤ +2       : proficient
    θ > +2           : advanced understanding and interpretation

{student_list}

- question_bank: A list of questions in Human Sciences, each defined by:
    a                : discrimination parameter
    b                : difficulty (−3 = easy; +3 = very hard)
    c                : guessing parameter (e.g., 0.20 for 5-option MCQs)

{questions}

SIMULATION MODEL (IRT - 3PL)
----------------------------
For each student–question pair:
- Compute the probability of correct response using the 3-parameter logistic model:

    P(θᵢ) = c + (1 - c) / (1 + exp(-a * (θᵢ - b)))

- Simulate the response:
    - 1 (correct) with probability P(θᵢ)
    - 0 (incorrect) otherwise

Use a pseudo-random generator to sample the outcome based on the probability.
The list of student answers must strictly follow the same order as the input questions to ensure proper alignment between each response and its corresponding question.

OUTPUT FORMAT
-------------
Return a JSON object with the following structure:

{output_format}

- Each student must answer {len(questions)} questions.
- Do NOT include any explanatory text or commentary.
- Output ONLY the JSON object, and nothing else.
"""
