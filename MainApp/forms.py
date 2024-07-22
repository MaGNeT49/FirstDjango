from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]
        password1 = forms.CharField(label="password", widget=forms.PasswordInput())
        password2 = forms.CharField(label="password confirm", widget=forms.PasswordInput())

    def clean_password2(self):
        pass1 = self.cleaned_data.get("password1")
        pass2 = self.cleaned_data.get("password2")
        if pass1 and pass2 and pass1 == pass2:
            return pass2
        raise ValidationError("Пароли не совпадают или пустые")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
