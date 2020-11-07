from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def divtastic_landing(request):
    return render(request, 'root/landing.html',)
