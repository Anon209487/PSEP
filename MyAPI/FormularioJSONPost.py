from urllib import response
from pip._vendor import requests
class FormularioJSONPost:
    @staticmethod
    def post(userid,title,completedBolean):
    # post
     api_url = "https://jsonplaceholder.typicode.com/todos"
     todo={"userid":userid,"title":title,"completed":completedBolean}
     response = requests.post(api_url,json=todo)
     print (response.json())
     print ("codigo de estado:" , response.status_code)