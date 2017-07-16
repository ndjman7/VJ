from django import forms
from django.contrib.auth import password_validation

from .models import VJUser


class VJLoginForm(forms.Form):
    userid = forms.CharField(label='ID', max_length=30)
    password = forms.CharField(label='Password', max_length=30)

class VJSignUpForm(forms.ModelForm):
    password1 = forms.CharField(max_length=30)
    password2 = forms.CharField(max_length=30)

    class Meta:
        model = VJUser
        fields = [
            'userid', 'name', 'phone_number', 'grade',
            'password1', 'password2',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
            password_validation.validate_password(
                self.cleaned_data['password2'],
                self.instance
            )
        return password2

    def save(self, commit=False):
        user = super(VJSignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.save()
