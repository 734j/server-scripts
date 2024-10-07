#!/usr/bin/python3
import sys
import subprocess

def run_command(command):
    try:
        # Run the command and capture the output
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        # Output the command's stdout
        print(f"Command succeeded with output:\n{result.stdout}")
        # Optionally return the output
        return result.stdout
    except subprocess.CalledProcessError as e:
        # Handle the case where the command fails
        print(f"Command failed with return code {e.returncode}")
        print(f"Error output: {e.stderr}")
        return None

def choice():
    while 1:
        user_input = input("[Y / N] ? ").strip()
        if user_input == "\n":
            continue
        if user_input == "y" or user_input == "Y":
            return 0
        if user_input == "n" or user_input == "N":
            return 1

if len(sys.argv) < 2 or len(sys.argv) > 2:
    print(f"{sys.argv[0]} [REPO NAME]", file=sys.stderr)
    exit(-1);

reponame = sys.argv[1];
reponame_len = len(reponame)
dotgitstr = ".git"
nodotgit = True
gitdir = "/srv/git/"

if len(reponame) >= 4 and reponame[-4:] == dotgitstr:
    nodotgit = False

if nodotgit:
    reponame += dotgitstr

print(f"The final repository name will be ---> \'{reponame}\'\n Do you want to create it?")
if choice() == 1:
    print("Exiting...")

run_command(f"cd {gitdir} && git init --bare {reponame} && chown -R git:git {reponame}")
