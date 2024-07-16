import openai
import json
from api.models.prompts.study_guides.study_guide_prompt import get_study_guide_prompt
from api.models.requests.study_guide_request import StudyGuideRequest

def get_study_guide(story_guide_request: StudyGuideRequest):
    """Generates an exercise using OpenAI gpt-4-0125-preview"""
    completion = openai.chat.completions.create(
        model="gpt-4-0125-preview",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": get_study_guide_prompt()},
            {"role": "user", "content": str(story_guide_request)}
        ]
    )
    response = json.loads(completion.choices[0].message.content)
    return response