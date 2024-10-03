from urllib import response
from pip._vendor import requests
class FormularioJSONPatch:
    @staticmethod
    def patch(title,completedBolean):
     api_url = "https://jsonplaceholder.typicode.com/todos/10"
     # creacionObjeto
     todo={"title":title,"completed":completedBolean}
     # Peticion pacth
     response = requests.patch(api_url,json=todo)
     print (response.json())
     print ("codigo de estado:" , response.status_code)