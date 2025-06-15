from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Colaborador

class CadastroColaboradorForm(UserCreationForm):
    tipo = forms.ChoiceField(
        choices=Colaborador.TIPO_CHOICES,
        widget=forms.RadioSelect,
        label="Você é servidor da Secretaria de Turismo do GDF ou colaborador?"
    )

    class Meta:
        model = Colaborador
        fields = ['username', 'email', 'tipo', 'password1', 'password2']

