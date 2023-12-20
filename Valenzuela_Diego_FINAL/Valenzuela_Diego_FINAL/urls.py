"""
URL configuration for Valenzuela_Diego_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from final_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('inscripciones/', views.inscripciones),
    path('institucion/', views.instituciones),
    path('api/instituciones/', views.listar_insituciones),
    path('lista-inscritos/', views.Inscritos_List_class.as_view()),
    path('lista-inscritos/<int:id>/', views.Inscritos_detalle_class.as_view()),
    path('estudiante/', views.estudiante)
]
