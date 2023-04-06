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
    api_url = "https://jsonplaceholder.typicode.com/todos"
    todo = {"userId": 11, "title": "Attend Training", "completed": False}
    headers =  {"Content-Type":"application/json"}
    response = requests.post(api_url, data=json.dumps(todo), headers=headers)
    print(f"adding {response.json()} with status:{response.status_code}")


get_status_code()
