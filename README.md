# knowledge_control

## Virtual environment
Installing virtual environment:

```bash
pip3 install virtualenv
```
Create a virtual environment:
```bash
python3 -m venv env
```
Activate your virtual environment:
```bash
source env/bin/activate
```
Then run app
```bash
python3 main.py
```
## Docker (will be soon)

You can start the project with docker using this command:

```bash
```

If you want to develop in docker with autoreload add `-f deploy/docker-compose.dev.yml` to your docker command.
Like this:

```bash
```

This command exposes the web application on port 8080, mounts current directory