from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.core import validators

User = get_user_model()


class ContactUsForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی', 'class': "form-control"}),
        label='نام و نام خانوادگی',
        validators=[
            validators.MaxLengthValidator(30, 'طولش نباید بیشتر از 30 بشود'),
        ]
    )

    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'مضوع', 'class': "form-control"}),
                              label='نام و نام خانوادگی',
                              validators=[
                                  validators.MaxLengthValidator(150, 'طولش نباید بیشتر از 150 بشود'),
                              ])

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'E-mail', 'class': "form-control", }),
        label='E-mail',
        validators=[validators.EmailValidator('ایمیل معتبر نمیباشد'),
                    validators.MaxLengthValidator(100, 'طولش نباید بیشتر از 100 بشود')])

    explaining = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'توضیحات', 'required class': "form-control", 'rows': 8, 'id': "message"}),
        label='توضیحات',
        validators=[validators.MaxLengthValidator(1000, 'طولش نباید بیشتر از 1000 بشود')])
