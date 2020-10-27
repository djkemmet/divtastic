from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import symbol_lookup_form

# Create your views here.
def symbol_research(request):

    form = symbol_lookup_form()

    if request.method == 'POST':
        form = symbol_lookup_form(request.POST)

    # If the form is good, go get all the data.
    if form.is_valid():
        form.save(commit=True)
        data = dict()
        data['message'] = "Your results for: %s" %(request.POST['symbol'])
        data['symbol'] = request.POST['symbol']
        data['declaration_date'] = "Find it"
        data['pte_ratio'] = 'Find it.'
        data['payout_ratio'] = 'Find it.'
        data['payout_date'] = 'Find it.'
        data['record_date'] = 'Find it.'
        data['dividend_yeild'] = 'Find it.'

        # Return a profile_results.html template here with the data returned from, 
        # this function i guess?
        return render(request, 'research/profile_results.html', context=data)
    else:
        print(form.errors)

    return render(request, 'research/new_stock_profile.html',{'form':form} )
    
def redirect_app_root(request):
    return HttpResponseRedirect('/')