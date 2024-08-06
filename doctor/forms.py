from django import forms
from .models import Messages
from django.contrib.auth import get_user_model

User = get_user_model()

class MessagesForm(forms.ModelForm):
    destinateur = forms.ModelChoiceField(queryset=User.objects.all(), label='', error_messages={'required': ''})
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Description'}), error_messages={'required': ''})

    class Meta:
        model = Messages
        fields = ['destinateur', 'message']

    def __init__(self, *args, **kwargs):
        super(MessagesForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required': '', 'invalid': ''}