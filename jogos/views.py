from django.shortcuts import render
from django.http import HttpResponse

def mostrar_home(request):
    return HttpResponse(request, "templates/index.html")