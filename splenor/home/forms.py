from django import forms
from .models import Contact

class ContactsForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']
