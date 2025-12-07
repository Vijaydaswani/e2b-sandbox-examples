from e2b_code_interpreter import Sandbox
from pathlib import Path

DATA_FILE = Path("sales.csv")

ANALYSIS_CODE = """
import pandas as pd

df = pd.read_csv("sales.csv")
summary = df.groupby("region")["amount"].sum().reset_index()

print("Total sales by region:")
print(summary.to_string(index=False))
"""

def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError("sales.csv not found – create it next to this script.")

    with Sandbox.create() as sandbox:
        print("Sandbox started 🟢")

        # 1) Upload CSV into the sandbox
        data = DATA_FILE.read_text()
        sandbox.files.write("sales.csv", data)
        print("Uploaded sales.csv to sandbox 🟢")

        # 2) Install pandas in the sandbox
        sandbox.commands.run("pip install pandas --quiet")
        print("Installed pandas 🟢")

        # 3) Run the analysis code
        execution = sandbox.run_code(ANALYSIS_CODE)

        # ✅ Read stdout from logs (where prints go)
        logs = getattr(execution, "logs", None)
        stdout_lines = getattr(logs, "stdout", None) if logs is not None else None

        print("=== Analysis Output ===")
        if stdout_lines:
            # logs.stdout is a list → join into one string
            print("".join(map(str, stdout_lines)))
        else:
            # Fallback: show last-expression value if any
            print(execution.text)

if __name__ == "__main__":
    main()
