
from turtle import st
from pip._vendor import requests
salir=False
api_url="https://jsonplaceholder.typicode.com/todos/1"
response=requests.get(api_url)
print(response.json())

while(salir is False):
    opcion=int(input("Elige dato del 1 al 10 usa 0 salida: "))
    if(opcion>0):
        response=requests.get(api_url+str(opcion))
        print (response.json())
    elif(opcion<0):
        print("opcion no valida.")
    else:
        salir=True
print("salida.")