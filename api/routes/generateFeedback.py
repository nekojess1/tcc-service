import openai
import json 
import os
from api.models.context.feedBackContext import get_feedback_prompt

openai.api_key = os.environ.get("OPENAI_API_KEY")

def get_feedback(userContent, feedbackList):
    print(get_feedback_prompt(feedbackList))
    print("uhu")
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": get_feedback_prompt(feedbackList)},
            {"role": "user", "content": str(userContent)}
        ]
    )
    response = json.loads(completion.choices[0].message.content)
    return response

