import openai
import json
from api.models.prompts.feedbacks.feedback_prompt import get_feedback_prompt

def get_feedback(question, feedback_list):
    """Generates personalized feedback using OpenAI GPT-3.5 Turbo"""
    completion = openai.chat.completions.create(
        model="gpt-4o",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": get_feedback_prompt(feedback_list)},
            {"role": "user", "content": str(question)}
        ]
    )
    response = json.loads(completion.choices[0].message.content)
    return response

