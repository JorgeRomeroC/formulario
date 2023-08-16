from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre y Apellido', required=True, min_length=5, max_length=30,
                           widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese sus datos'}))
    
    email = forms.EmailField(label='Correo Electronico', required=True, max_length=100,
                             widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Ingrese su correo electronico'}))
    
    message = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(attrs={'class':'form-control','rows':5}))