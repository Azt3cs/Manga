from allauth.account.forms import SignupForm, LoginForm
from django import forms


class SignUp(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', required=False)
    last_name = forms.CharField(max_length=30, label='Last Name', required=False)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

class SignIn(LoginForm):
    username = forms.CharField(max_length=20, label='username', required=False)

