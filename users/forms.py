from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationsForm(UserCreationForm):
    """ registration form for user """

    username = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'abid'
        })
    )

    password1 = forms.CharField(max_length=255, min_length=8, required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Password contain minimum 8 characters!'
                                })
                                )
    password2 = forms.CharField(max_length=255, min_length=8, required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Repeat your password'
                                })
                                )

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        username_qs = User.objects.filter(Q(username=username))
        if username_qs.exists():
            raise forms.ValidationError("Sorry, User with this username  already exists!")
        if password1 != password2:
            raise forms.ValidationError("password didn't match!")
        return super(UserRegistrationsForm, self).clean(*args, **kwargs)


class LoginForm(forms.Form):
    """ login form for user login """
    username = forms.CharField(max_length=255, required=True,
                                        widget=forms.TextInput(attrs={
                                            'class': 'form-control form--control-custom',
                                            'placeholder': 'Username Or Email'
                                        }))
    password = forms.CharField(max_length=255, required=True,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control form--control-custom mb-1',
                                   'placeholder': 'Password'
                               }))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        # checking user existence of user
        user_qs = User.objects.filter(username=username)
        if not user_qs.exists():
            raise forms.ValidationError("Invalid credentials, User does not exist.")
        user_obj = user_qs.first()
        # checking the password
        if not user_obj.check_password(password):
            raise forms.ValidationError('Credentials are not correct.')

        return super(LoginForm, self).clean(*args, **kwargs)

