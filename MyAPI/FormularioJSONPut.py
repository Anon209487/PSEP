from http.client import responses
from urllib import response
from pip._vendor import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"
# Peticion Get
response = requests.get(api_url)
print (response.json())
# creacionObjeto
todo={"userid":1,"title":"washcar","completed":True}
# Peticion PUT
response= requests.put(api_url,json=todo)
print(response.json())
print(response.status_code)