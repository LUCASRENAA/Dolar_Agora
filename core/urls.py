from django.urls import path
from . import views

urlpatterns = [
    path('dolar_agora', views.dolar_agora),
    path('dolar_agora_redundancia', views.dolar_agora_api),
    path('', views.home),
   ]