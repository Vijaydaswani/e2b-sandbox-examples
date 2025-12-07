import os
from openai import OpenAI
from e2b_code_interpreter import Sandbox

# Make sure OPENAI_API_KEY and E2B_API_KEY are set in your env
client = OpenAI()

SYSTEM_PROMPT = """
You are a helpful Python coding assistant.
You ONLY respond with Python code, no explanations.
Do not use backticks. Just raw code.
"""

USER_TASK = "Create a list of the first 20 Fibonacci numbers and print them."

def main():
    # 1) Ask the LLM to generate Python code
    response = client.responses.create(
        model="gpt-5.1",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_TASK},
        ],
    )

    code = response.output[0].content[0].text
    print("=== Generated code ===")
    print(code)
    print("======================")

    # 2) Run that code in an E2B sandbox
    with Sandbox.create() as sandbox:
        execution = sandbox.run_code(code)
        print("=== Sandbox logs ===")
        print(execution.logs)
        print("=== Sandbox text ===")
        print(execution.text)

if __name__ == "__main__":
    main()
