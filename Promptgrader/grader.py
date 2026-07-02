import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)

SYSTEM_PROMPT = """
You are an expert Prompt Grader.

Evaluate the user's prompt using the following rubric.

Clarity (2)
Context (2)
Specificity (2)
Constraints (2)
Output Format (2)

Return ONLY valid JSON.

Do not wrap the JSON inside markdown.

Return exactly this format:

{
    "overall_score":0,
    "clarity":0,
    "context":0,
    "specificity":0,
    "constraints":0,
    "output_format":0,
    "strengths":[],
    "weaknesses":[],
    "suggestions":[]
}
"""


def grade_prompt(prompt):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            SYSTEM_PROMPT,
            prompt
        ]
    )

    text = response.text.strip()

    # Remove markdown if Gemini adds it
    if text.startswith("```json"):
        text = text.replace("```json", "", 1)

    if text.startswith("```"):
        text = text.replace("```", "", 1)

    if text.endswith("```"):
        text = text[:-3]

    text = text.strip()

    return json.loads(text)