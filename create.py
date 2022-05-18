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
        help=f"The path to the default workspace where the newly created repo will be cloned to. By default, this is {os.path.join(_HOME, 'Documents')}"
    )
    parser.add_argument(
        "-a",
        "--api",
        type=str,
        help = f"The name of the API to generate an API project structure, if relevant."
    )
    args = parser.parse_args()
    return args
    
def create_api_structure(api_name, repo):
    with open("api-docs/pull_api_data.py", "r") as api_file:
        api_content = api_file.read()
    repo.create_file(f"src/pull_{api_name}_api_data.py", "added api pull file", api_content)
    with open("api-docs/json_to_df.py", "r") as j2df:
        j2df_content = j2df.read()
    repo.create_file(f"src/json_to_df.py","added fson to df file", j2df_content)
    with open("api-docs/sample_requirements.txt", "r") as req:
        req_content = req.read()
    repo.create_file("requirements.txt", "added requirements file", req_content)


def create(args):
    repo_name = args.github_repo
    workspace = args.workspace_path
    api_name = args.api
    if not workspace:
        workspace = os.path.join(_HOME, "Documents")
    g = Github(_ACCESS_TOKEN)
    o = g.get_organization("Harvest-Digital-Ltd")
    r = o.create_repo(repo_name, private=True)
    r.create_file('README.md', 'initial commit', f'# {repo_name}')
    print(f"Succesfully created remote repository {repo_name}")
    if api_name:
        create_api_structure(api_name, r)
        print(f"Created folder structure for API: {api_name}")
    os.chdir(workspace)
    os.system(f"git clone git@github.com:Harvest-Digital-Ltd/{repo_name}")
    print(f"Succesfully created local repository {repo_name}")
    os.chdir(os.path.join(os.getcwd(),f"{repo_name}"))

def main():
    args = command_parser()
    create(args)

if __name__ == '__main__':
    main()