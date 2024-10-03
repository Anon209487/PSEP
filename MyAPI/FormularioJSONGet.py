from urllib import response
from pip._vendor import requests
# peticion get
class FormularioJSONGet:
    @staticmethod
    def get(userid,title,completedBolean):
     api_url = "https://jsonplaceholder.typicode.com/todos/10"
     response = requests.get(api_url)
     print(response.json())
     # creacion de objeto
     todo={"userid":userid,"title":title,"completed":completedBolean}
     # peticion get 
     response = requests.post(api_url,json=todo)
     print (response.json())
