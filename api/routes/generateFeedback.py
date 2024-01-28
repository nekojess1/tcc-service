import openai
import json 
import os
from api.models.context.feedBackContext import teste

openai.api_key = os.environ.get("OPENAI_API_KEY")

def get_feedback(userContent, feedbackList):
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": teste(feedbackList)},
            {"role": "user", "content": userContent}
        ]
    )
    response = json.loads(completion.choices[0].message.content)
    return response

