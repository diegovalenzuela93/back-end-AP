from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'evaluacion1_app/index.html')