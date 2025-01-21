from django.forms import TextInput,EmailInput,NumberInput
from django import forms
from .models import Order




class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["name","place","email","address","city","phonenumber"] 
        widgets = {
            'name' : TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name',
            }),
            'place' : TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder' : 'Enter your place',
            }),
            'email' : EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder' : 'Enter your email',
            }),
            'address' : TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder' : 'Enter your addres'
            }),
            'city' : TextInput(attrs={
               'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder' : 'Enter your city'
            }),
            'phonenumber' : TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder' : 'Enter your mobile number'
            }),
        }
        
 
    

