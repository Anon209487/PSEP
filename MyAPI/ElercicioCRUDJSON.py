from FormularioJSONPost import *
from FormularioJSONGet import *
from FormularioJSONPatch import *
from FormularioJSONDelete import *
from turtle import st
from pip._vendor import requests
# funcion que pide datos
def mostrarDatos():
    print("OPCIONES:")
    print("1.Post.")
    print("2.Get.")
    print("3.Patch.")
    print("4.Delete.")
    print("0.Salida.")
# variable para condicionar el bucle
salida=False
# bucle con condicional
while salida==False:
   userid=int(input("Introduce el ID: "))
   title=(input("Introduce el titulo: "))
   completedBolean =False
   completed = bool(input("Completado: True / False: "))
   # implementacion boolean
   if completed == ("True"):
        completedBolean=True
   # Llamada a la funcion que imprime los datos
   mostrarDatos()
   # variable que sirve para establecer opciones
   opcion=int(input("Seleccione una opcion:"))

   if opcion==1:
       # llamada a la clase post
        FormularioJSONPost.post(userid,title,completedBolean)
   elif opcion==2:
       # llamada a la clase get
        FormularioJSONGet.get(userid,title,completedBolean)
   elif opcion==3:
        # llamada a la clase patch
        FormularioJSONPatch.patch(title,completedBolean)
   elif opcion==4:
        # llamada a la clase delete
        FormularioJSONDelete.delete()
   elif opcion==0 :
       # salida
        salida=True
   else:
     print("OPCION NO VALIDA")
print("Ha salido del programa.")