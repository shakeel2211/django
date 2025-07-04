from django import forms
from .models import ChaiVarity

# jab form dropdown bnana ho 
class ChaiVarityForm(forms.Form):
   chai_varity = forms.ModelChoiceField(
       queryset=ChaiVarity.objects.all(),
       label="Select chai variety"
   )
