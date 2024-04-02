from .models import CustomUser
from django.utils import timezone

def delete_inactive_accounts():
    """
    Deletes user accounts that have not been activated within 15 minutes of registration.
    """
    threshold_time = timezone.now() - timezone.timedelta(minutes=15)
    inactive_users = CustomUser.objects.filter(is_active=False, date_joined__lt=threshold_time)

    for user in inactive_users:
        user.delete()

