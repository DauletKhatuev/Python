from django.urls import path
from .views import hello_view

urlpatterns = [
    path("hallo/", hello_view,  name="hello"),
]