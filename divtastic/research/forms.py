from django import forms
from research.models import symbol_lookup_model


class symbol_lookup_form(forms.ModelForm):
    symbol = forms.CharField(max_length=5, help_text="AAPL,TSLA,SBUX,...")



    class Meta:
        model = symbol_lookup_model
        fields = '__all__'