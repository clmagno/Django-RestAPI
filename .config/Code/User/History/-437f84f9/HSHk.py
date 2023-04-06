import requests


def get_data(id):
    api_url = f"http://127.0.0.1:8000/id/{id}"
    response = requests.get(api_url)
    print(response.json())
def get_all_data():
    api_url = "http://127.0.0.1:8000/all"
    response = requests.get(api_url,data={'id':1})
    print(response.json())

def post_data(name, description):
    api_url = "http://127.0.0.1:8000/"
    todo = {"name":name, "description":description}
    response = requests.post(api_url, json=todo)
    print(f"adding {response.json()}\nstatus:{response.status_code}")

def put_data(id,name, description):
    api_url = f"http://127.0.0.1:8000/{id}/"
    todo = {"name":name,"description":description}
    response = requests.put(api_url, json=todo)
    print(f"updating... {response.json()}\nstatus: {response.status_code}")

#post_data(name="Machine Learning",description="Fundamentals of Machine Learning")
#get_data(1)
put_data("Fundamentals of Machine Learning","Machine Learning course for those who are knowledgeable with python")
