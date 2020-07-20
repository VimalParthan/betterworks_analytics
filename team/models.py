from django.db import models
from django.db.models import PROTECT

from department.models import Department


class Team(models.Model):
    team_lead = models.ForeignKey('user.User', on_delete=PROTECT, null=False, related_name='+')
    department = models.ForeignKey(Department, on_delete=PROTECT, null=False)
    average_pay = models.DecimalField(decimal_places=2, max_digits=10, default=None)

    class Meta:
        db_table = "teams"
