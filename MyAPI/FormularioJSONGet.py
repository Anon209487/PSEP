from urllib import response
from pip._vendor import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())
todo={"userid":1,"title":"wash car","completed":True}
response = requests.post(api_url,json=todo)
print (response.json())
print (response.status_codse)