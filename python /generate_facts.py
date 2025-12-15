import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

FACT_PROMPT = """
Give me 20 useless, chaotic, unhinged Gen-Z brainrot facts.
Each fact must be:
- under 12 words
- funny, weird, or mildly disturbing
- zoomer-coded
- no numbers or bullet points
Return each fact on a new line.
"""

def generate_facts():
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": FACT_PROMPT}],
        max_tokens=200
    )

    facts = response["choices"][0]["message"]["content"].strip().split("\n")
    return [f.strip("-• ") for f in facts if f.strip()]

if __name__ == "__main__":
    print(generate_facts())
