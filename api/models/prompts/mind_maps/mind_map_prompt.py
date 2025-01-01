from api.models.prompts.mind_maps.mind_map_examples import input_format, input_example, output_format, output_example
from api.models.prompts.mind_maps.mind_map_instructions import context

def get_mind_map_prompt():
   return f"""

   {context}
    
   Input format:

   {input_format}
   
   Input example:
   
   {input_example}
   
   Output format:
   
   {output_format}
   
   Output example: 
   
   {output_example}

   Return the mind map in JSON format.
   
   """
