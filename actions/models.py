from django.db import models
from django.utils.translation import ugettext_lazy as _

from decimal import Decimal
from users.models import *
from barinfo.models import *
from goods.models import *

class Action(models.Models):
    """
    A class describing all the logged actions
    """

    LIST_OF_ACTIONS = ("purchase", "theft", "disposal", "supply", "gift", 
                       "credit", "refund", "fine", "withdrawal", "agios", "event")

    bar = models.ForeignKey("Bar", related_name="action", verbose_name=_("bar"))
    type_of_action = models.CharField(max_length=30, choices=LIST_OF_ACTIONS, verbose_name=_("type"))

    # amount : amount of money that was involved
    amount = model.DecimalField(max_digits=8, decimal_places=2, verbose_name=_("amount"))
    good = models.ForeignKey("Good", related_name="good", verbose_name=_("good"), null=True)
    quantity = models.DecimalField(max_digits=12, decimal_places=4, verbose_name=_("quantity"))
    # doer : person who does the action (for example, the person who fined)
    doer = models.ForeignKey("BarUser", related_name="doer", verbose_name=_("doer"), null=True)
    #grantee : person who is the target of the action (for example, the person who was fined)
    grantee = models.ForeignKey("BarUser", related_name="grantee", verbose_name=_("grantee"), null=True)

    date = models.DateTimeField(auto_now_add=True, verbose_name=_("date"))

    #info : for example, reason for a fine, or name of the event
    info = models.CharField(max_length=255, verbose_name=_("additional information"))


    class Meta:
        verbose_name = _("action")
        verbose_name_plural = _("actions")

    def __str__(self):
        return self.type_of_action + " of " + str(self.good) + " by " + self.doer.displayed_name + " for " + self.grantee.displayed_name
