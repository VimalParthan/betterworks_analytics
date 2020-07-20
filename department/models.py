import datetime

from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=30, null=False)
    location = models.CharField(max_length=30, null=False)
    date_of_inauguration = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "departments"
