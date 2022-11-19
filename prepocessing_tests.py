import requests

data = {
        "text":"Hello, my name is Joao, I'm 21. My email is Joao@duke.edu", 
        "steps":["replace_email"]
    }
response = requests.get( "http://0.0.0.0:8080/preprocess/", json=data )