# automate-create-project

Automates the process of creating a new project by creating a new repository on GitHub and cloning it to your local machine. 

## To install:

```
$ git clone https://github.com/quibbleahr/automate-create-project.git
$ cd automate-create-project/
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ touch .env
```

## .env file:

After creating the `.env` file as shown above, put in your access token like so:

```
ACCESS_TOKEN="<your_access_token>"
```


## Usage:
When inside the `automate-create-project` folder:
```
$ py create.py -h

usage: create.py [-h] [-w WORKSPACE_PATH] github_repo

Creates remote GitHub repository and clones it locally.

positional arguments:
  github_repo           The GitHub repository to be created remotely and cloned locally.

optional arguments:
  -h, --help            show this help message and exit
  -w WORKSPACE_PATH, --workspace_path WORKSPACE_PATH
                        The path to the default workspace where the newly created repo will be cloned to. By default, this is ~/Documents
```