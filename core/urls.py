from django.urls import path
   from . import views

   urlpatterns = [
       path('dolar_agora', views.dolar_agora),
       path('', views.home),
   ]