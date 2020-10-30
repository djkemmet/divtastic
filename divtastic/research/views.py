from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import symbol_lookup_form
from research.functions import *
import yfinance as yf
from lxml import etree
import requests

# Create your views here.
def symbol_research(request):

    form = symbol_lookup_form()

    if request.method == 'POST':
        form = symbol_lookup_form(request.POST)

    # If the form is good, go get all the data.
    if form.is_valid():
        
        data = dict()
        data['symbol'] = request.POST['symbol'].upper()

        # yfinance Data
        symbol = yf.Ticker(request.POST['symbol'])
        data['yfinance_data'] = symbol.info

        # Get the ACTUAL LINK (aka handle their redirect...)
        url1 = 'https://dividend.com/search?q=' + request.POST['symbol']
        response1 = requests.get(url1, allow_redirects=True)

        url = response1.url
        response = requests.get(url)

        html = response.text
        dom = etree.HTML(html)

        data['tax_type'] = 'Source From Dividend.com'
        data['frequency'] = dom.xpath('/html/body/main/section/section[1]/div/div/div/article/div[2]/div[3]/div[1]/section/div[2]/div/div[1]/div[5]/div[2]/text()')[0]
        data['consecutive_increase'] = dom.xpath('/html/body/main/section/section[1]/div/div/div/article/div[2]/div[3]/div[1]/section/div[2]/div/div[1]/div[4]/div[2]/text()')[0]
        data['payout_ratio'] = dom.xpath('/html/body/main/section/section[1]/div/div/div/article/div[2]/div[3]/div[1]/section/div[2]/div/div[1]/div[3]/div[2]/text()')[0]
        data['next_payout'] = dom.xpath('/html/body/main/section/section[1]/div/div/div/article/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/text()')[0]
        data['next_payout_date'] = dom.xpath('/html/body/main/section/section[1]/div/div/div/article/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/text()')[0]
        data['tax_mode'] = dom.xpath('/html/body/main/section/section[1]/div/div/div/article/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/text()')[0]
        data['latest_quote'] = dom.xpath('/html/body/main/div[5]/div[1]/section/div/div[2]/div[2]/div[1]/div[2]/div[2]/text()')[0].strip('\n')

        # Return a profile_results.html template here with the data returned from, 
        # this function i guess?
        return render(request, 'research/profile_results.html', context=data)
    else:
        print(form.errors)

    return render(request, 'research/new_stock_profile.html',{'form':form} )
    
def redirect_app_root(request):
    return HttpResponseRedirect('/')