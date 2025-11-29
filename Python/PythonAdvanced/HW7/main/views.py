from django.shortcuts import render
from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Hallo, Boss")

# Create your views here.
