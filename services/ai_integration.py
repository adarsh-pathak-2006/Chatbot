from google import genai
from django.conf import settings

client=genai.Client(
    api_key=settings.GEMINI_API_KEY
)

def generate_output(prompt):
    output=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return output.text.strip()