from urllib import response
from pip._vendor import requests
# peticion get
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(response.json())
# creacion de objeto
todo={"userid":1,"title":"wash car","completed":True}
# peticion get 
response = requests.post(api_url,json=todo)
print (response.json())
print (response.status_codse)