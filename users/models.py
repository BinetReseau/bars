from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from barinfo.models import *
from decimal import Decimal

class BarUser(models.Model):
    """
    Class containing additional information about the user
    """
    user = models.OneToOneField(User, verbose_name=_("user"))
    displayed_name = models.CharField(verbose_name=_("displayed name"))
    balance = modes.DecimalField(max_digits=8, decimal_places=2, verbose_name=_("Account balance"))

    favorite_bars = models.ManyToManyField(related_name="favorite", verbose_name=_("Favorite bar"))
    #Signed in bars : bars in which this user owns an account
    signed_in_bars = models.ManyToManyField(related_name="signed_in", verbose_name=_("Signed in bars"))

    class Meta:
        verbose_name = _("Bar user")
        verbose_name_plural = _("Bar users")

    def __str__(self):
        return "%s" % (self.displayed_name)
