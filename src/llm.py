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

    def generate_answer(self, question, context, history=""):

        prompt = f"""
You are an Enterprise Document Intelligence Assistant.

You must answer ONLY using the supplied document context.

You are also given the previous conversation.

Use the conversation history to understand follow-up questions.

Rules:

1. Answer ONLY from the document.
2. Never invent information.
3. If the answer exists, answer directly.
4. If it truly doesn't exist, reply:
"I couldn't find that information in the uploaded document."

========================
Conversation History

{history}

========================
Document Context

{context}

========================
Current Question

{question}

========================
Answer
"""

        response = self.model.generate_content(prompt)

        return response.text.strip()

    def summarize_document(self, context):

        prompt = f"""
You are an Enterprise Document Intelligence Assistant.

Generate a concise summary of this document.

Maximum 8 bullet points.

Document:

{context}

Summary:
"""

        response = self.model.generate_content(prompt)

        return response.text.strip()

    def generate_questions(self, context):

        prompt = f"""
Read the following document.

Generate 5 useful questions.

Only return questions.

Document:

{context}
"""

        response = self.model.generate_content(prompt)

        return response.text.strip().split("\n")