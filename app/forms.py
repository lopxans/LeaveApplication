from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'number', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Your full name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Your email address',
            }),
            'number': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Your phone number',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Write your message here...',
                'rows': 4,
            }),
        }
