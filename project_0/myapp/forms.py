from django import forms
from .models import Request
from .models import User


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['request_description', 'proofs']  # Include proofs as a single file


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'academic_email', 'academic_year', 'profile_picture']  # Include necessary fields


