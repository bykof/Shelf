# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

from rest_framework.authtoken.models import Token


# Subclass AbstractUser
class User(AbstractUser):

    def __unicode__(self):
        return u'{} {}'.format(self.first_name, self.last_name)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)