from django import forms
from . import models


class Converter(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('Quantity','ConvertFrom','ConvertTo')

class Balance(forms.ModelForm):
    class Meta:
        model = models.balance
        fields = ('Address','Coin')