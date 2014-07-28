from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from common.models import UUIDModel
from django.utils.translation import ugettext as _
from managers import UserManager
from django.conf import settings

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin, UUIDModel):
    '''
    Inherits from both the AbstractBaseUser and PermissionMixin.
    Uses email as login field
    '''
    name = models.CharField(_('Name'), max_length=30)
    email = models.EmailField(_('Email Address'), unique=True, db_index=True)
    is_staff = models.BooleanField(
        _('Staff Status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(
        _('Active'), default=False,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_short_name(self):
        try:
            split_name = self.name.split()
            return split_name[0]
        except IndexError:
            return self.name
