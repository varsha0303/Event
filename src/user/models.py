from django.contrib.auth.models import (AbstractBaseUser)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from user.managers import CustomUserManager
from user.choices import (GENDER, USER_TYPE)


class User(AbstractBaseUser):
    """
    This model stores information about User
    """
    id = models.AutoField(primary_key=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('First Name'), max_length=255)
    last_name = models.CharField(_('Last Name'), max_length=255)
    gender = models.CharField(_('Gender'), choices=GENDER, max_length=255,
    null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    user_type = models.CharField(_('Type'), choices=USER_TYPE, max_length=255,
    null=True, blank=True)
    mobile_number = models.CharField(_('Mobile number'), max_length=10)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name')


    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'
