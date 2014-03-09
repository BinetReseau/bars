from django.db import models
from django.utils.translation import ugettext_lazy as _
from barinfo.models import *

class Category(models.Model):
    """
    This class contains the information about the good categories specific to each bar.
    """
    bar = models.ForeignKey(Bar, related_name='category', verbose_name=_("bar"))
    name = models.CharField(verbose_name=_("name"))
    default_tax = models.PositiveSmallIntegerField(verbose_name=_("default tax"))

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name

class Good(models.Model):
    """
    This class contains every information about the goods
    """
    bar = models.ForeignKey('Bar', related_name="good", verbose_name=_("bar"))
    name = models.CharField(verbose_name=_("name"))
    search_terms = models.CharField(verbose_name=_("search terms"))
    quantity = models.DecimalField(max_digits=12, decimal_places=4, verbose_name=_("quantity"))

    amount_per_packet = models.DecimalField(max_digits=12, decimal_places=4, verbose_name=_("amount per packet"))
    price_per_packet = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_("price per packet"))
    tax = models.PositiveSmallIntegerField(verbose_name=_("tax"))

    class Meta:
        verbose_name = _("good")
        verbose_name_plural = _("goods")

    def __str__(self):
        return self.name
