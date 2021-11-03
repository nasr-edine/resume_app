from django.forms import ModelForm
# from django.forms import Textarea
from .models import Contact
from django import forms


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "text"]

        name = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={
                                   'placeholder': '*Full name..'
                               }))
        email = forms.EmailField(max_length=254, required=True,
                                 widget=forms.TextInput(attrs={
                                     'placeholder': '*Email..'
                                 }))
        text = forms.CharField(max_length=1000, required=True,
                               widget=forms.Textarea(attrs={
                                   'placeholder': '*Message..'
                               }))
