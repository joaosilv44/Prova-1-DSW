from django.urls import  path
from views import mostrar_home

urlpatterns = [
    path("/", mostrar_home, name="jogos:index")
]