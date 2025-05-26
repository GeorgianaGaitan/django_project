from importlib.metadata import metadata

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.http import HttpResponse, HttpRequest
from datetime import datetime

from accounts.models import UserLoginMetadata

@receiver(user_logged_in)
def log_user_login(sender, request: HttpRequest, user, **kwargs):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    ip = request.META.get('REMOTE_ADDR', '')
    now = datetime.now()


    metadata = UserLoginMetadata.objects.create(
        user=user,
        ip_address=ip,
        user_agent=user_agent,
        login_time=now,
    )



