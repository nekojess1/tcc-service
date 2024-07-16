from api.models.prompts.feedbacks.feedback_examples import input_example, output_example
from api.models.prompts.feedbacks.feedback_instructions import context

def get_feedback_prompt(feedbacks):
    """Generate a feedback prompt with examples."""
    return f"""
{context}

# Feedbacks that you should inspire the tone and writing to generate feedback:

{feedbacks}

# Input Example:

{input_example}

# Output Example:

{output_example}

# Verification for numeric correction
"numeric_correction": true
"""
