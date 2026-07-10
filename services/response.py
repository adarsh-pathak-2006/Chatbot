from services.build_prompt import build_prompt
from services.ai_integration import generate_output


def generate_response(input):
    prompt=build_prompt(question=input)
    response=generate_output(prompt)
    return response