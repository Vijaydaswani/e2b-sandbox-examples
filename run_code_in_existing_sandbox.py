# run_code_in_existing_sandbox.py
from e2b_code_interpreter import Sandbox
from pathlib import Path
from e2b.exceptions import NotFoundException

ID_FILE = Path("sandbox_id.txt")

CODE = """
x = globals().get("x", 0)
x += 1
print("x is now:", x)
x
"""

def main():
    if not ID_FILE.exists():
        print("❌ sandbox_id.txt not found. Run start_sandbox.py first.")
        return

    sandbox_id = ID_FILE.read_text().strip()
    print("Read sandbox ID:", sandbox_id)

    try:
        sandbox = Sandbox.connect(sandbox_id)
    except NotFoundException:
        print(f"❌ Sandbox {sandbox_id} not found or already expired.")
        print("   Run start_sandbox.py again to create a new sandbox.")
        return

    print("Connected to sandbox ✅")

    execution = sandbox.run_code(CODE)

    logs = getattr(execution, "logs", None)
    stdout = getattr(logs, "stdout", None) if logs else None

    print("=== STDOUT ===")
    if stdout:
        print("".join(stdout))

    print("=== Last expression (execution.text) ===")
    print(execution.text)

if __name__ == "__main__":
    main()
