from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def symbol_research(request):
    return HttpResponse("<h1>Lets investigate a stock!")
    
def redirect_app_root(request):
    return HttpResponseRedirect('/')