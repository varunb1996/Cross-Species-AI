import requests
import os

from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY"
)

MODEL_NAME = "llama-3.1-8b-instant"

def interpret_behavior(results):

    prompt = f"""
    You are an expert bioacoustic AI researcher.

    Analyze these animal communication patterns.

    Generate:
    - behavioral hypotheses
    - social interaction interpretation
    - emotional/intensity patterns
    - communication structure observations

    Results:
    {results}
    """

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL_NAME,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.3
        }
    )

    output = response.json()

    return output["choices"][0]["message"]["content"]