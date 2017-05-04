
from django import forms

class teamForm(forms.Form):
    mainSearch = forms.CharField(label='mainSearch', max_length=100)