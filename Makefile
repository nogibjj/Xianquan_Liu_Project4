install:
		pip install --upgrade pip &&\
			pip install -r requirements.txt

test:
		python -m pytest -vv test_hello.py

format:
		black *.py


lint:
		pylint --disable=R,C hello.py

build:
		docker build -t deploy-fastapi .

run:

deploy:
		aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 105813801991.dkr.ecr.us-east-1.amazonaws.com
		docker build -t password_generator .
		docker tag password_generator:latest 105813801991.dkr.ecr.us-east-1.amazonaws.com/password_generator:latest
		docker push 105813801991.dkr.ecr.us-east-1.amazonaws.com/password_generator:latest

all: install lint test deploy
