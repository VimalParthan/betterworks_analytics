from django.db import models
from django.db.models import PROTECT, Count

from team.models import Team


class User(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    team = models.ForeignKey(Team, on_delete=PROTECT, null=True)

    class Meta:
        db_table = "users"

    @staticmethod
    def get_department_to_users_count_dict():
        qry_result = User.objects.filter(
            team__isnull=False
        ).values('team__department__name').annotate(
            users_count=Count('id', distinct=True)
        )

        department_to_users_count_dict = {
            res_dict['team__department__name']:
                res_dict['users_count'] for res_dict in qry_result
        }

        return department_to_users_count_dict
