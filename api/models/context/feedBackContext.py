output_example = """
{
    "title": "{título da pergunta}",
    "question_id": "{id da pergunta}",
    "response": {
        "answer": "{resposta do aluno à pergunta}",
        "email": "{email do aluno}",
        "response_id": "{id da resposta}",
        "form_id": "{id do formulário}",
        "feedback": "{feedback gerado por você sobre a resposta do aluno}",
        "type": "{tipo da resposta, sendo: acerto, acerto parcial ou erro}"
    }
}
"""

input_example = """
{
    "title": "{título da pergunta}",
    "question_id": "{id da pergunta}",
    "response": {
        "answer": "{resposta do aluno à pergunta}",
        "email": "{email do aluno}",
        "response_id": "{id da resposta}",
        "form_id": "{id do formulário}",
        "feedback": "{feedback gerado por você sobre a resposta do aluno}",
        "type": "{tipo da resposta, sendo: acerto, acerto parcial ou erro}"
    }
}
"""

context = """
    Você é um professor encarregado de corrigir e fornecer feedback detalhado sobre as respostas dos alunos. Cada resposta deve ser classificada como "acerto", "acerto parcial" ou "erro". 
    Baseie-se nos exemplos abaixo para estruturar o feedback, considerando a entonação e estilo apresentados:
"""

def get_feedback_prompt(feedbacks):
    return f"""

    {context}
    
    Exemplos de Feedback do Professor:

    {feedbacks}

    Exemplo de Entrada JSON:

    {output_example}

    Exemplo de Retorno JSON:

    {input_example}

    # Verificação para correção numérica
    "numeric_correction": true
    """
