import pandas as pd
from google import genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Load dataset
df = pd.read_csv("matches.csv")

print("Dataset loaded successfully!")

while True:
    question = input("\nAsk a cricket question (type exit to quit): ")

    if question.lower() == "exit":
        break

    columns = list(df.columns)

    prompt = f"""
You are a Python data analyst.

Dataset columns:
{columns}

Rules:
1. Generate ONLY Python pandas code.
2. Use dataframe name df.
3. Store the final answer in a variable called result.
4. Do not use import statements.
5. Do not use open(), os, subprocess, eval, exec, or file operations.
6. Return only code without markdown.

Question:
{question}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        code = (
            response.text
            .replace("```python", "")
            .replace("```", "")
            .strip()
        )

        

        # Safety check
        forbidden = [
            "import",
            "open(",
            "os.",
            "subprocess",
            "__",
            "eval(",
            "exec("
        ]

        for word in forbidden:
            if word in code:
                raise Exception("Unsafe code generated")

        local_vars = {"df": df}

        exec(code, {}, local_vars)

        answer = local_vars["result"]

        print("\nAnswer:")

        # Format percentages nicely
        if isinstance(answer, float) and 0 <= answer <= 1:
            print(f"{round(answer * 100, 2)} %")
        else:
            print(answer)

    except Exception as e:
        print("Error:", e)