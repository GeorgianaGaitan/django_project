from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserLoginMetadata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='loginmetadata')
    #login time, user_agent, ip address
    login_time = models.DateTimeField()
    ip_adress = models.CharField(max_length=255)
    user_agent = models.CharField(null=True, blank=True, max_length=255)


    def __str__(self):
        return 'User {} last login {}, with IP {}, user agent: {}'.format(self.user.username, self.login_time, self.ip_adress,
                                                                          self.user_agent)



