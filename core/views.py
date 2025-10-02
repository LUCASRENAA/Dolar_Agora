from django.shortcuts import render
import os

def dolar_agora(request, ip):
    return render(request, 'core/dolar_agora.html')

def home(request):
    return render(request, 'core/index.html')