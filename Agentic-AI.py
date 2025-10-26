
# Clone the repository and change into the task_manager directory using Python.
# This requires 'git' to be installed and available on PATH.

import subprocess
import os
import sys

repo_url = "https://github.com/jaseci-labs/Agentic-AI.git"
clone_dir = "Agentic-AI"
task_manager_subdir = "task_manager"

def check_git_available():
	try:
		subprocess.run(["git", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	except (subprocess.CalledProcessError, FileNotFoundError):
		print("Error: 'git' is not installed or not available in PATH.", file=sys.stderr)
		sys.exit(1)

def clone_repo(url):
	try:
		subprocess.run(["git", "clone", url], check=True)
	except subprocess.CalledProcessError as e:
		print(f"Failed to clone {url}: {e}", file=sys.stderr)
		sys.exit(e.returncode)

def change_to_task_manager(dir_name, subdir):
	path = os.path.join(dir_name, subdir)
	if os.path.isdir(path):
		os.chdir(path)
		print(f"Changed working directory to: {path}")
	else:
		print(f"Directory '{path}' not found after cloning.", file=sys.stderr)
		sys.exit(1)

if __name__ == "__main__":
	check_git_available()
	clone_repo(repo_url)
	change_to_task_manager(clone_dir, task_manager_subdir)