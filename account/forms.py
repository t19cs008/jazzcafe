# from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email', 'username',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = ''
        self.fields["email"].widget.attrs.pop('required')
        self.fields["last_name"].widget.attrs['autofocus'] = ''
        self.fields["last_name"].widget.attrs['placeholder'] = '田中'
        self.fields["first_name"].widget.attrs['placeholder'] = '一郎'
        self.fields["email"].widget.attrs['placeholder'] = '****@gmail.com'

