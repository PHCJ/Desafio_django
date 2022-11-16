from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    dataNascimento = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
    class Meta:
        model = Usuario
        fields = ['nomeUsuario','dataNascimento','senha']
        