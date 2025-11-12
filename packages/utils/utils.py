import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.getenv("GITHUB_TOKEN")
)

def sonata(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=1,
            max_tokens=500
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {e}"