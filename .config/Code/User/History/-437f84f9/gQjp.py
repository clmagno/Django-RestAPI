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
    api_url = "https://github.com/clmagno/api/db/tasks"
    todo = {"userId": 1, "title": "Conduct Training", "completed": False}
    response = requests.post(api_url, json=todo)
    print(f"adding {response.json()} with status:{response.status_code}")


post_data()
