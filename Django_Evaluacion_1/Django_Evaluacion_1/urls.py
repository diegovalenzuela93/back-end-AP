"""
URL configuration for Django_Evaluacion_1 project.

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
from evaluacion1_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('consolas/', views.consolas),
    path('pcgamer/', views.pc),
    path('accesorios/', views.accesorios),
    path('descripcion/consolas/<str:producto_id>', views.descripcion_consolas),
    path('descripcion/pc/<str:producto_id>', views.descripcion_pc),
    path('descripcion/accesorios/<str:producto_id>', views.descripcion_accesorios),
    path('perfil/', views.usuario)
]
