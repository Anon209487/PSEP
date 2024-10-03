from http.client import responses
from urllib import response
from pip._vendor import requests
from pip._vendor.requests.api import delete
api_url = "https://jsonplaceholder.typicode.com/todos/10"
# Peticion delete
response = requests.delete(api_url)
print(response.status_code)
print(response.json())
