from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def divtastic_landing(request):
    return HttpResponse("<h1> You've Reached the home page</h1>")
