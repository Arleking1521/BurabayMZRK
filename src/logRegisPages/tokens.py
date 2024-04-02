from .models import CustomUser
from django.utils import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import timezone

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user: CustomUser, timestamp):
        login_timestamp = timezone.datetime.timestamp(user.date_joined)
        return six.text_type(user.pk)+six.text_type(timestamp)+six.text_type(user.is_active)+six.text_type(login_timestamp)