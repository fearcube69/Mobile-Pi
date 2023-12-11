# run.py

import subprocess


def main():
    # Specify the name of the script you want to run
    script_name = "build/Main.py"

    try:
        # Run the main.py script using subprocess
        subprocess.run(["python3", script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to run {script_name}.")
        print(f"Error details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
