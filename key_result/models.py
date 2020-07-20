import datetime
from django.db import models
from objective.models import Objective


class KeyResult(models.Model):

    class StatusChoice(models.TextChoices):
        COMPLETE = 'complete'
        IN_PROGRESS = 'in_progress'

    objective = models.ForeignKey(Objective, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=15,
        choices=StatusChoice.choices,
        default=StatusChoice.IN_PROGRESS,
    )
    due_date = models.DateField(default=None)
    date_of_creation = models.DateField(default=datetime.date.today, null=False)

    class Meta:
        db_table = "key_results"



