import os


def count_python_files(directory, exclude_dirs=None):
    if exclude_dirs is None:
        exclude_dirs = ['venv', '__pycache__']

    count = 0
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if file.endswith(".py") and file != "count_py_files.py":
                count += 1
    return count


if __name__ == "__main__":
    project_dir = os.path.dirname(os.path.abspath(__file__))
    total_files = count_python_files(project_dir)

    # Create or update README.md
    with open(os.path.join(project_dir, "README.md"), "w") as readme_file:
        readme_file.write(f"# Project Progress\n\n")
        readme_file.write(f"## Solved Problems: {total_files}/150\n")
        readme_file.write("This repository contains my solutions for the LeetCode 150 problems.\n")