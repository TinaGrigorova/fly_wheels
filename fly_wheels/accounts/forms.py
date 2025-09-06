from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="We’ll send receipts here.")
    subscribe_me = forms.BooleanField(
        required=False, initial=True,
        label="Email me news and offers (you can unsubscribe anytime)."
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "subscribe_me")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
