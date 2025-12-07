# start_sandbox.py
from e2b_code_interpreter import Sandbox
from pathlib import Path
import time

ID_FILE = Path("sandbox_id.txt")

def main():
    sandbox = Sandbox.create()
    print("Sandbox started 🟢")
    print("Sandbox ID:", sandbox.sandbox_id)

    # Save ID for other scripts
    ID_FILE.write_text(sandbox.sandbox_id)
    print(f"Saved sandbox ID to {ID_FILE.resolve()}")

    print("\nKeep this script running while you demo.")
    print("Other scripts will read sandbox_id.txt and connect to this sandbox.")

    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nScript stopped. Sandbox may still live for a short timeout.")

if __name__ == "__main__":
    main()
