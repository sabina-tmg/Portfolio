from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-field',
        'placeholder': 'Enter Your Name',
        'id': 'name',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input-field',
        'placeholder': 'Enter Your Email',
    }))
    number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-field',
        'placeholder': 'Enter Your Phone',
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'input-field textarea-field',
        'placeholder': 'Enter Messages',
        'rows': 5,
    }))
