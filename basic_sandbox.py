from e2b_code_interpreter import Sandbox

def main():
    # Create a sandbox – this starts an isolated environment in the cloud
    with Sandbox.create() as sandbox:
        print("Sandbox started ✅")

        # 1) Run a simple Python statement
        execution = sandbox.run_code('print("Hello from E2B!")')
        print("Logs:", execution.logs)
        print("Text output:", execution.text)

        # 2) Stateful execution: variables persist between calls
        sandbox.run_code("x = 10")
        execution2 = sandbox.run_code("x += 5; x")
        print("x after update:", execution2.text)  # should be 15

if __name__ == "__main__":
    main()
