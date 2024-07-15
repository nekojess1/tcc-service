from api.models.prompts.mind_maps.mind_map_examples import input_format, output_format, output_example
from api.models.prompts.mind_maps.mind_map_instructions import context

def get_mind_map_prompt():
   return f"""

   {context}
    
   Input format:

   {input_format}
   
   Output format:
   
   {output_format}

   Return the mind map in JSON format.

   Example filled return:

   {output_example}
   
   """
