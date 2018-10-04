from django import forms

class MyForm(forms.Form):
    sequence = forms.CharField(max_length=10000,widget = forms.Textarea(attrs={'rows':'20',"cols":150,"placeholder":"example input: NLADAVSKAPQLVPKLDEVYNAAYNAADHAAP or fasta-format input"}))
    p_value = forms.FloatField(max_value = 1,min_value = 0)
