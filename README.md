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
python3 app.py
```
## requirements.txt
Add necessary packages:
bash
pip freeze > requirements.txt

## Docker 

You can start the project with docker using this command:
```bash
docker-compose up --build
```
This command exposes the web application on port 5000, mounts current directory