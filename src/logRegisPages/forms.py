from django.contrib.auth.forms import  UserCreationForm, PasswordResetForm
from .models import CustomUser
from django import forms
from django.contrib.auth import get_user_model, authenticate, password_validation
import unicodedata
from django.contrib.auth.hashers import UNUSABLE_PASSWORD_PREFIX, identify_hasher
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext as _


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['name', 'surename', 'email', 'phone']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = f'{self.cleaned_data["name"]}{self.cleaned_data["email"]}'
        if commit:
            user.save()
        return user

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')
        return password2
    def clean_name(self):
        return self.cleaned_data['name']
    def clean_surename(self):
        return self.cleaned_data['surename']
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = _('Имя')
        self.fields['surename'].widget.attrs['placeholder'] = _('Фамилия')
        self.fields['email'].widget.attrs['placeholder'] = _('Почта')
        self.fields['phone'].widget.attrs['placeholder'] = _('Телефон')
        self.fields['password1'].widget.attrs['placeholder'] = _('Пароль')
        self.fields['password2'].widget.attrs['placeholder'] = _('Подтверждение пароля')
        self.fields['password1'].widget.attrs['id'] = 'password-input'
        self.fields['password2'].widget.attrs['id'] = 'password-input1'


User = get_user_model()

class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Почта', max_length=254, required=True)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            raise forms.ValidationError('Неверная почта или пароль.')
        return self.cleaned_data
    
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = _('Почта')
        self.fields['password'].widget.attrs['placeholder'] = _('Пароль')
        self.fields['password'].widget.attrs['id'] = 'password-input'


def _unicode_ci_compare(s1, s2):
    """
    Perform case-insensitive comparison of two identifiers, using the
    recommended algorithm from Unicode Technical Report 36, section
    2.11.2(B)(2).
    """
    return (
        unicodedata.normalize("NFKC", s1).casefold()
        == unicodedata.normalize("NFKC", s2).casefold()
    )

class CustomPasswordResetForm(forms.Form):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

    def send_mail(
        self,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name=None,
    ):
        """
        Send a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = "".join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)

        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        if html_email_template_name is not None:
            html_email = loader.render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, "text/html")

        email_message.send()

    def get_users(self, email):
        
        email_field_name = User.get_email_field_name()
        active_users = User._default_manager.filter(
            **{
                "%s__iexact" % email_field_name: email,
                "is_active": True,
            }
        )
        return (
            u
            for u in active_users
            if u.has_usable_password()
            and _unicode_ci_compare(email, getattr(u, email_field_name))
        )

    def save(
        self,
        domain_override=None,
        subject_template_name="registration/password_reset_subject.txt",
        email_template_name="registration/password_reset_email.html",
        use_https=False,
        token_generator=default_token_generator,
        from_email=None,
        request=None,
        html_email_template_name=None,
        extra_email_context=None,
    ):
        """
        Generate a one-use only link for resetting password and send it to the
        user.
        """
        email = self.cleaned_data["email"]
        if not domain_override:
            current_site = get_current_site(request)
            site_name = current_site.name
            domain = current_site.domain
        else:
            site_name = domain = domain_override
        email_field_name = User.get_email_field_name()
        for user in self.get_users(email):
            user_email = getattr(user, email_field_name)
            context = {
                "email": user_email,
                "domain": domain,
                "site_name": site_name,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "user": user,
                "token": token_generator.make_token(user),
                "protocol": "https" if use_https else "http",
                **(extra_email_context or {}),
            }
            self.send_mail(
                subject_template_name,
                email_template_name,
                context,
                from_email,
                user_email,
                html_email_template_name=html_email_template_name,
            )

    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Почта'




class CustomSetPasswordForm(forms.Form):
    """
    A form that lets a user set their password without entering the old
    password
    """

    error_messages = {
        "password_mismatch": _("The two password fields didn’t match."),
    }
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "placeholder": "Новый пароль",
            'id': 'password-input'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    def clean_new_password2(self):
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        password_validation.validate_password(password2, self.user)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
    
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password2'].widget.attrs.update({
            'placeholder': 'Подтверждение пароля',
            'id': 'password-input1',
        })