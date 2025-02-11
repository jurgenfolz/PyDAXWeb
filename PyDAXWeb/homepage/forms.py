# homepage/forms.py
from django import forms

class DAXForm(forms.Form):
    dax_expression = forms.CharField(
        label='DAX Expression',
        widget=forms.Textarea(attrs={'rows': 8, 'cols': 80})
    )
