from .forms import  CustomSetPasswordForm, RegistrationForm, UserLoginForm, CustomPasswordResetForm
from django.contrib.auth import login as auth_login, authenticate, logout, get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponseRedirect 
from django.utils.encoding import force_bytes, force_str 
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.template.loader import render_to_string
from .custom_utils import delete_inactive_accounts
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from .tokens import TokenGenerator
from django.utils import timezone
from .models import CustomUser


account_activation_token = TokenGenerator()
User = get_user_model()
def registration(request):
    if request.method == 'POST': 
        delete_inactive_accounts()
        form = RegistrationForm(request.POST) 
        if form.is_valid(): 
            email = form.cleaned_data.get('email')
            # Проверяем, существует ли пользователь с такой почтой
            try:
                existing_user = User.objects.get(email=email)
                # Проверяем, активен ли пользователь
                if not existing_user.is_active:
                    # Удаляем неактивного пользователя
                    existing_user.delete()
                else:
                    # Показываем сообщение об ошибке
                    return render(request, 'registration/error_message.html', {
                        'error': 'Аккаунт с такой почтой уже существует и активен.'
                    })
            except User.DoesNotExist:
                # Нет пользователя с такой почтой, продолжаем регистрацию
                pass
            user = form.save(commit=False) 
            user.is_active = False 
            user.save() 
            current_site = get_current_site(request) 
            mail_subject = 'Ссылка для активации аккаунта на сайте ' + str(current_site) 
            message = render_to_string('registration/acc_active_email.html', { 
                'user': user, 
                'domain': current_site.domain, 
                'uid':urlsafe_base64_encode(force_bytes(user.pk)), 
                'token':account_activation_token.make_token(user), 
            }) 
            to_email = form.cleaned_data.get('email') 
            print(to_email)
            email = EmailMessage( 
                        mail_subject, message, to=[to_email] 
            ) 
            email.send() 
            return render(request,'registration/registr_email_messege.html', {'email' : to_email}) 
    else: 
        form = RegistrationForm() 
    return render(request, 'registration/registration.html', {'form': form})

def activate(request, uidb64, token): 
    try: 
        uid = force_str(urlsafe_base64_decode(uidb64)) 
        user = CustomUser.objects.get(pk=uid) 
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist): 
        user = None 

    if user is not None and account_activation_token.check_token(user, token):
        time_elapsed = timezone.now() - user.date_joined
        if time_elapsed.total_seconds() <= 900:  # 900 секунд = 15 минут
            user.is_active = True 
            user.save() 
            print(user)
            return render(request, 'registration/registr_email_active.html') 
        else: 
            delete_inactive_accounts()
            return render(request,'registration/registr_email_activate_fail.html')

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                auth_login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('index')



class PasswordContextMixin:
    extra_context = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {"title": self.title, "subtitle": None, **(self.extra_context or {})}
        )
        return context
class CustomPasswordResetView(PasswordContextMixin, FormView):
    email_template_name = "registration/password_reset_email.html"
    extra_email_context = None
    form_class = CustomPasswordResetForm
    from_email = None
    html_email_template_name = None
    subject_template_name = "registration/password_reset_subject.txt"
    success_url = reverse_lazy("password_reset_done")
    template_name = "registration/password_reset_form.html"
    title = _("Password reset")
    token_generator = default_token_generator

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        opts = {
            "use_https": self.request.is_secure(),
            "token_generator": self.token_generator,
            "from_email": self.from_email,
            "email_template_name": self.email_template_name,
            "subject_template_name": self.subject_template_name,
            "request": self.request,
            "html_email_template_name": self.html_email_template_name,
            "extra_email_context": self.extra_email_context,
        }
        form.save(**opts)
        return super().form_valid(form)
    
INTERNAL_RESET_SESSION_TOKEN = "_password_reset_token"

class CustomPasswordResetConfirmView(PasswordContextMixin, FormView):
    form_class = CustomSetPasswordForm
    post_reset_login = False
    post_reset_login_backend = None
    reset_url_token = "set-password"
    success_url = reverse_lazy("password_reset_complete")
    template_name = "registration/password_reset_confirm.html"
    title = _("Enter new password")
    token_generator = default_token_generator

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        if "uidb64" not in kwargs or "token" not in kwargs:
            raise ImproperlyConfigured(
                "The URL path must contain 'uidb64' and 'token' parameters."
            )

        self.validlink = False
        self.user = self.get_user(kwargs["uidb64"])

        if self.user is not None:
            token = kwargs["token"]
            if token == self.reset_url_token:
                session_token = self.request.session.get(INTERNAL_RESET_SESSION_TOKEN)
                if self.token_generator.check_token(self.user, session_token):
                    # If the token is valid, display the password reset form.
                    self.validlink = True
                    return super().dispatch(*args, **kwargs)
            else:
                if self.token_generator.check_token(self.user, token):
                    # Store the token in the session and redirect to the
                    # password reset form at a URL without the token. That
                    # avoids the possibility of leaking the token in the
                    # HTTP Referer header.
                    self.request.session[INTERNAL_RESET_SESSION_TOKEN] = token
                    redirect_url = self.request.path.replace(
                        token, self.reset_url_token
                    )
                    return HttpResponseRedirect(redirect_url)

        # Display the "Password reset unsuccessful" page.
        return self.render_to_response(self.get_context_data())

    def get_user(self, uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User._default_manager.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            User.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.user
        return kwargs

    def form_valid(self, form):
        user = form.save()
        del self.request.session[INTERNAL_RESET_SESSION_TOKEN]
        if self.post_reset_login:
            auth_login(self.request, user, self.post_reset_login_backend)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.validlink:
            context["validlink"] = True
        else:
            context.update(
                {
                    "form": None,
                    "title": _("Password reset unsuccessful"),
                    "validlink": False,
                }
            )
        return context