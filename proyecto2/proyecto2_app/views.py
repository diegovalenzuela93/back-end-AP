from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'proyecto2_app/index.html')

def Electronica(request):
    data = {"titulo" : "Electronica",
            "producto1" : "MacBook",
            "producto2" : "Multimetro",
            "producto3" : "Parlante",
            "foto1" : "electronica1.jpg",
            "foto2" : "electronica2.png",
            "foto3" : "electronica3.jpg"}
    return render(request, 'proyecto2_app/producto.html', data)

def Ropa(request):
    data = {"titulo" : "Ropa",
            "producto1" : "Camisa",
            "producto2" : "Poleron Deportivo",
            "producto3" : "Parka Termica"}
    return render(request, 'proyecto2_app/producto.html', data)

def Jugete(request):
    data = {"titulo" : "Juguetes",
            "producto1" : "Autos",
            "producto2" : "Multimetro",
            "producto3" : "Parlante"}
    return render(request, 'proyecto2_app/producto.html', data)