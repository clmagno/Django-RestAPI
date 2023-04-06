import requests


def get_data(id):
    api_url = f"https://my-json-server.typicode.com/clmagno/api/tasks/{id}"
    response = requests.get(api_url)
    print(response.json())


def post_data(name, description):
    import json
    api_url = "http://127.0.0.1:8000/post/"
    todo = {name, description}
    response = requests.post(api_url, json=todo)
    print(f"adding {response.json()}\nstatus:{response.status_code}")

def get_all_data():
    api_url = "http://127.0.0.1:8000/"
    response = requests.get(api_url,data={'id':1})
    print(response.json())

def put_data(id):
    api_url = f"https://my-json-server.typicode.com/clmagno/api/tasks/{id}"
    todo = {"userId": 1, "title": "Prepare Tools", "completed": True}
    response = requests.put(api_url, json=todo)
    print(f"modifying... {response.json()}\nstatus: {response.status_code}")

post_data(name="Fundamentals of Java",description="Learn about the fundamental concepts of JAVA Programming for newbies")
