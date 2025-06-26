from .validate_exercises_examples import output_format, elementary_student_list

def get_validate_elementary_students_exercises_prompt():
    return f"""
      # Simulation Context
      You are an educational assessment expert. Your task is to simulate the responses of a group of 1000 elementary school students with very low skills in reading, comprehension, and humanities. Based on their answers, estimate the Item Response Theory (IRT) parameters for each question.

      # Student Profile
      - Student abilities (θ) range from -3 to -2, and are listed below:
      {elementary_student_list}

      # Rules for IRT Parameters
      - The **c parameter (guessing)** must be estimated as **≥ 0.2**.
      - The **b parameter (difficulty)** is the point on the ability scale where the probability of a correct answer begins to increase rapidly.
      - The **a parameter (discrimination)** reflects how sharply the probability of success increases with small changes in ability.

      # Simulation and Estimation Steps

      ## 1. Simulating Student Responses
      - For each question j and student i:
        - Assume the student has ability θᵢ.
        - Simulate the resolution of the question using only the knowledge expected from a student with that level of ability.
        - If the student would answer correctly, register a 1; otherwise, register a 0.
        - Generate a binary response matrix (Rᵢⱼ).

      ## 2. Grouping Students (Binning)
      - Divide the θ range (-3 to -2) into 5 to 7 equal-width bins.
      - For each interval:
        - Count the number of students in the interval.
        - Calculate the accuracy rate (correct answers / total students in the interval).
        - Use these points (average θ in the interval × accuracy rate) to estimate the empirical response curve.

      ## 3. Estimating IRT Parameters
      - Fit the 3-parameter logistic curve:
        P(θ) = c + (1 - c) / (1 + e^(-a(θ - b)))
      - From this curve, estimate:
        - **a**: discrimination (slope of the curve).
        - **b**: difficulty (point of rapid increase).
        - **c**: guessing parameter (≥ 0.2).

      # Expected Output Format
      Return the data strictly in the following JSON format:

      {output_format}

"""
