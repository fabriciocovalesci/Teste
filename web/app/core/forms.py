
from django import forms 
from .models import *
  
class FotoForm(forms.ModelForm): 
  
    class Meta: 
        model = Foto 
        fields = ['name', 'foto_carregada'] 