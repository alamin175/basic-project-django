from django import forms
from django.core import validators
class ShowFormsData(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(label='Enter Email', initial='mdalaminh052@gmail.com', disabled=True)

    def clean(self):
        cleaned_data = super().clean()
        rightpass = self.cleaned_data['password']
        wrongpass = self.cleaned_data['repassword']

        if rightpass != wrongpass:
            raise forms.ValidationError('Password does not match')
    