from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())
