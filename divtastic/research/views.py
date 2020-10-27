from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def symbol_research(request):
    return render(request, 'research/new_stock_profile.html', {"data":"No Data"})
    
def redirect_app_root(request):
    return HttpResponseRedirect('/')