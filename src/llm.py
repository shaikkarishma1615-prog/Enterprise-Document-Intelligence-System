import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class GeminiLLM:

    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in .env")

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate_answer(self, question, context):

        prompt = f"""
You are an AI assistant.

Answer ONLY using the context below.

If the answer is not available in the context, say:
"I couldn't find that information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""

        response = self.model.generate_content(prompt)

        return response.text