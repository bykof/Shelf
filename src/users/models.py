# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser


# Subclass AbstractUser
class User(AbstractUser):

    def __unicode__(self):
        return u'{} {}'.format(self.first_name, self.last_name)
