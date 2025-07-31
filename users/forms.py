# /home/siisi/atmp/users/forms.py


from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from .models import CustomUser, UserRole


class CustomUserCreationForm(UserCreationForm):
    # Build prompt list by slicing the class attribute
    ROLE_PROMPT = [('', 'Select a role')] + CustomUser.ROLE_CHOICES[1:]

    role = forms.ChoiceField(
        choices=ROLE_PROMPT,
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True,
    )

    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox(attrs={'data-size': 'compact'})
    )

    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'role', 'password1', 'password2', 'captcha']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control form-control-user'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-control form-control-user'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password', 'class': 'form-control form-control-user'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Repeat Password', 'class': 'form-control form-control-user'})


class CustomAuthenticationForm(AuthenticationForm):
    username_field = CustomUser._meta.get_field('email')
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={'data-size': 'compact'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
