import requests
def get_data(id):
    api_url = f"https://my-json-server.typicode.com/clmagno/api/tasks/{id}"
    response = requests.get(api_url)
    print(response.json())


def get_status_code():
    api_url = "https://my-json-server.typicode.com/clmagno/api/tasks/"
    response = requests.get(api_url)
    print(response.status_code)

def get_headers():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url)
    print(response.headers)

def post_data():
    import json
    api_url = "https://my-json-server.typicode.com/clmagno/api/tasks"
    todo = {"userId": 1, "title": "Rehearse Slides", "completed": False}
    response = requests.post(api_url, json=todo)
    print(f"adding {response.json()}\nstatus:{response.status_code}")

def get_all_data():
    api_url = f"https://my-json-server.typicode.com/clmagno/api/tasks"
    response = requests.get(api_url)
    print(response.json())

def put_data(id):
    api_url = f"https://my-json-server.typicode.com/clmagno/api/tasks/{id}"
    todo = {"userId": 1, "title": "Prepare Tools", "completed": True}
    response = requests.put(api_url, json=todo)
    print(f"modifying... {response.json()}\nstatus: {response.status_code}")
put_data(3)