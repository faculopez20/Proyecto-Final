from django.shortcuts import render, redirect
from Inicio.models import Usuario 


def inicio(request): 
  
    usuario = Usuario.objects.all()
    return render(request, "Base.html", {})

def usuario(request):
    usuario = Usuario.objects.all()
    return render(request, "usuario.html", {"usuario": usuario})

#def crear_cliente(request, nombre,apellido, edad):
 #   cliente = Cliente (nombre=nombre, apellido=apellido, edad=edad, dinero_gastado=random.randint(1,100))
 #   cliente.save() 
 #   return render(request, "crear_cliente.html", {"cliente":cliente})
