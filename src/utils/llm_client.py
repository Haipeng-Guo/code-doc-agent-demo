import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class LLMClient:
    def __init__(self):
        api_key = os.getenv("MIMO_API_KEY") or os.getenv("OPENAI_API_KEY")
        base_url = os.getenv("MIMO_BASE_URL") or os.getenv("OPENAI_BASE_URL")
        self.model = os.getenv("MIMO_MODEL", "gpt-3.5-turbo")
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def generate(self, prompt: str, system: str = "You are a helpful AI assistant.") -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
        )
        return response.choices[0].message.content