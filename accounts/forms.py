from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CreateUserDoctorForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom d'utilisateur"}), label='')

    adresse = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Saisir votre Address"}), label='')

    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Entre votre Email"}), label='')

    telephone = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Télephone"}), label='')

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Créer un Mot de passe"}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Confirmation mot de passe"}), label='')
    photo_profile = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': "Votre Photo de profile"}), label='Votre photo de profile')

    isDoctor = forms.BooleanField(initial=True, widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "telephone",
            "password1",
            "password2",
            "photo_profile",
            "adresse",
            "isDoctor",
        )


class CreateUserPatientForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom d'utilisateur", 'class': 'form-control' }), label='')
    profession = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Entre votre Profession"}), label='')
    adresse = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Saisir votre Address"}), label='')
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Entre votre Email"}), label='')
    telephone = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Télephone"}), label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Créer un Mot de passe"}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Confirmation mot de passe"}), label='')
    photo_profile = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': "Votre Photo de profile"}))

    isPatient = forms.BooleanField(initial=True, widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "telephone",
            "profession",
            "password1",
            "password2",
            "photo_profile",
            "adresse",
            "isPatient",
        )



class ConnexionForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': "Nom d'utilisateur", 
    }), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Mot de passe', 
    }), label='')

    class Meta:
        model = User
        fields = ('username', 'password')

