from urllib import response
from pip._vendor import requests
# pedir datos
userid=int(input("Introduce el ID: "))
title=(input("Introduce el titulo: "))
completedBolean =False
completed = bool(input("Completado: True / False: "))
if completed == ("True"):
    completedBolean=True

# post
api_url = "https://jsonplaceholder.typicode.com/todos"
todo={"userid":userid,"title":title,"completed":completedBolean}
response = requests.post(api_url,json=todo)
print (response.json())
print ("codigo de estado:" , response.status_code)