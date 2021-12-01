from django import forms
from .models import Agendar, Servicio 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AgendarForm(forms.ModelForm):

    class Meta:
        model = Agendar
        fields = ["fecha", "servicio", "hora"]

class ServicioForm(forms.ModelForm):

    class Meta:
        model =  Servicio
        fields = ["nombre", "tipo", "precio"]

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
