from urllib import response
from pip._vendor import requests

api_url = "https://jsonplaceholder.typicode.com/todos/10"
# creacionObjeto
todo={"title":"HOLA"}
# Peticion pacth
response = requests.patch(api_url,json=todo)
print (response.json())
print ("codigo de estado:" , response.status_code)