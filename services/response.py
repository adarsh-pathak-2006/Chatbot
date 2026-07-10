from services.build_prompt import build_prompt
from services.ai_integration import generate_ouput


def generate_response(input):
    prompt=build_prompt(question=input)
    response=generate_ouput(prompt)
    return response