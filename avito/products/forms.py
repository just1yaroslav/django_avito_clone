from django import forms


class SearchProductForm(forms.Form):
    query = forms.CharField()
