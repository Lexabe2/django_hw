from django import forms

class AddPhoto(forms.Form):
    title = forms.ChoiceField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'style': 'width: 200px'}))
    description = forms.ChoiceField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'style': 'width: 200px'}))
    prace = forms.ChoiceField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'style': 'width: 200px'}))
    quantity = forms.ChoiceField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'style': 'width: 200px'}))
    date_added = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'class': 'form-control',
        'style': 'width: 200px'}))
    photo = forms.ImageField()