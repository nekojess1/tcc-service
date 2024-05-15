import openai
import graphviz 
import json 
import os
import random
from api.models.context.feedback_prompt import get_feedback_prompt
from api.models.context.mind_map_prompt import get_mind_map_prompt
from api.models.context.study_guide_prompt import get_study_guide_prompt
from api.models.context.exercises_prompt import get_exercise_prompt
from api.models.common.Graph import Graph
from api.models.request.study_guide_request import StudyGuideRequest
from api.models.request.exercises_request import ExerciseRequest

openai.api_key = os.environ.get("OPENAI_API_KEY")

def get_feedback(question, feedback_list):
    """Generates personalized feedback using OpenAI GPT-3.5 Turbo"""
    completion = openai.chat.completions.create(
        model="gpt-4-0125-preview",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": get_feedback_prompt(feedback_list)},
            {"role": "user", "content": str(question)}
        ]
    )
    response = json.loads(completion.choices[0].message.content)
    return response

def get_mind_map(questions):
    """Generates personalized feedback using OpenAI gpt-4-0125-preview"""
    completion = openai.chat.completions.create(
        model="gpt-4-0125-preview",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": get_mind_map_prompt()},
            {"role": "user", "content": str(questions)}
        ]
    )

    response = json.loads(completion.choices[0].message.content)
    custom_model_instance = Graph(**response)
    generate_mind_map_pdf(custom_model_instance)
    return response

def get_exercises(exercise_request: ExerciseRequest):
    """Generates personalized study guide using OpenAI gpt-4-0125-preview"""
    completion = openai.chat.completions.create(
        model="gpt-4-0125-preview",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": get_exercise_prompt()},
            {"role": "user", "content": str(exercise_request)}
        ]
    )
    response = json.loads(completion.choices[0].message.content)
    return response

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

def generate_mind_map_pdf(graph: Graph):
    randomNumber = str(random.random())
    dot = graphviz.Digraph(comment='The Round Table', format='pdf', node_attr={'color': 'lightblue2', 'style': 'filled', 'imagescale' : 'true'})
    for node in graph.nodes:
        dot.node(node.id, node.content)
        
    for edge in graph.edges:
        dot.edge(edge.source, edge.target, constraint='false')
    file_name = f'{randomNumber}.dot'
    dot.render(directory='doctest-output/', filename=file_name)
