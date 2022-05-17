from github import Github
import argparse
import sys, getopt
import os
from dotenv import load_dotenv

load_dotenv()

_ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
_HOME = os.path.expanduser("~")

def command_parser():
    parser = argparse.ArgumentParser(
        description="Creates remote GitHub repository and clones it locally."
    )
    # The following argument(s) should be provided to run the example.
    parser.add_argument(
        "github_repo",
        type=str,
        help="The GitHub repository to be created remotely and cloned locally."
    )
    parser.add_argument(
        "-w",
        "--workspace_path",
        type=str,
        help=f"The path to the default workspace. By default, this is {os.path.join(_HOME, 'Documents')}"
    )
    args = parser.parse_args()
    return args
    

def create(args):
    repo_name = args.github_repo
    workspace = args.workspace_path
    if not workspace:
        workspace = os.path.join(_HOME, "Documents")
    g = Github(_ACCESS_TOKEN)
    u = g.get_user()
    r = u.create_repo(repo_name)
    r.create_file('README.md', 'initial commit', f'# {repo_name}') 
    print(f"Succesfully created remote repository {repo_name}")
    os.chdir(workspace)
    os.system(f"git clone git@github.com:ariannafharvest/{repo_name}")
    print(f"Succesfully created local repository {repo_name}")
    os.chdir(os.path.join(os.getcwd(),f"{repo_name}"))

def main():
    args = command_parser()
    create(args)

if __name__ == '__main__':
    main()