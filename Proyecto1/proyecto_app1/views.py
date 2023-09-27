from django.shortcuts import render

# Create your views here.

def usotemplate(request):
    data ={"nombre" : "Pedro"}
    return render(request, 'templateapp1/plantilla.html', data)

def userInfo(request):
    data ={"ID" : "123", "Nombre" : "Clark Kent", "Email" : "superman@jl.org"}
    return render(request, 'templateapp1/userInfoTemplate.html', data)
