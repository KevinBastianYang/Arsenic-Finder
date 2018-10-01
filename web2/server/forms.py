from django import forms

class MyForm(forms.Form):
    seq = forms.CharField(max_length=10000,widget = forms.Textarea)
    p_value = forms.CharField(max_length=100)
