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


## To use:
When inside the `automate-create-project` folder:
```
$ py create.py <your_project_name>
```