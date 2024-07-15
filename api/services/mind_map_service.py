import openai
import json
from api.models.prompts.mind_maps.mind_map_prompt import get_mind_map_prompt
from api.utils.graph import generate_mind_map, GraphStructure

def get_mind_map(mindMapRequest):
    """Generates personalized feedback using OpenAI gpt-4-0125-preview"""
    completion = openai.chat.completions.create(
        model="gpt-4-0125-preview",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": get_mind_map_prompt()},
            {"role": "user", "content": str(mindMapRequest)}
        ]
    )
    response = json.loads(completion.choices[0].message.content)
    custom_model_instance = GraphStructure(**response)
    generate_mind_map(custom_model_instance)
    return response