# stop_sandbox.py
from e2b_code_interpreter import Sandbox
from pathlib import Path
from e2b.exceptions import NotFoundException

ID_FILE = Path("sandbox_id.txt")

def main():
    if not ID_FILE.exists():
        print("❌ sandbox_id.txt not found.")
        return

    sandbox_id = ID_FILE.read_text().strip()

    try:
        sandbox = Sandbox.connect(sandbox_id)
    except NotFoundException:
        print(f"❌ Sandbox {sandbox_id} not found or already gone.")
        return

    sandbox.kill()
    print("Sandbox killed 🔴")

if __name__ == "__main__":
    main()
