from django import forms
from .models import Messages, Alimentation, Medicament
from django.contrib.auth import get_user_model

User = get_user_model()

class MessagesForm(forms.ModelForm):
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'messages'}), error_messages={'required': ''})

    class Meta:
        model = Messages
        fields = ['message']


class AlimentationForm(forms.ModelForm):
    nom = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nom de l\'alimentation'}))
    vitamine = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Vitamine'}))
    description = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'description'}))

    class Meta:
        model = Alimentation
        fields = ['nom', 'vitamine', 'description']


class MedicamentForm(forms.ModelForm):
    nom = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nom de medicament'}))
    dose = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Dosage'}))
    description = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'description'}))

    class Meta:
        model = Medicament
        fields = ['nom', 'dose', 'description']
