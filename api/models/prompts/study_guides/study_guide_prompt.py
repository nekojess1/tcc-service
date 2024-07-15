from api.models.prompts.study_guides.study_guide_examples import input_example, output_example
from api.models.prompts.study_guides.study_guide_instructions import context

def get_study_guide_prompt():
    """Generate a study guide prompt with examples."""
    
    return f"""
{context}

# JSON Input Example:

{input_example}

# JSON Output Example:

{output_example}
"""
