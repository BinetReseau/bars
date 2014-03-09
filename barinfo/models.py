from django.db import models
from django.utils.translation import ugettext_lazy as _

class Bar(models.Model):
    """
    Class containing all the informations about the bar
    """
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    slug = models.SlugField(max_length=255, verbose_name=_("Slug"))
    image = models.ImageField(verbose_name=_("image")))
    email = models.EmailField(verbose_name=_("e-mail"))
    
    has_agios = models.BooleanField(default=False, verbose_name=_("has agios ?"))
    agios_delay = models.PositiveSmallIntegerField(verbose_name=_("delay before agios"))
    agios_formula = models.CharField(max_length=255, verbose_name=_("agios formula"))

    tax = models.DecimalField(max_digits=7, decimal_places=2, verbose_name=_("tax for externals"))
