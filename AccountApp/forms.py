from django.forms import ModelForm

from AdminApp.models import LoginTable


class LoginForm(ModelForm):
    class Meta:
        model = LoginTable
        fields = ['Username', 'Password']

