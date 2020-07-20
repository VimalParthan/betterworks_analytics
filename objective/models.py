from django.db import models
from django.db.models import Count, Q, F

from common.date_utils import get_today_date
from user.models import User


class Objective(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    objective_text = models.TextField(null=False)

    def __str__(self):
        return self.objective_text

    class Meta:
        db_table = "objective"

    @staticmethod
    def get_on_track_summary():
        from key_result.models import KeyResult

        result = Objective.objects.filter(user__team__isnull=False).aggregate(
            total_count=Count('pk', distinct=True),
            not_on_track_count=Count('pk', filter=Q(keyresult__status=KeyResult.StatusChoice.IN_PROGRESS,
                                                    keyresult__due_date__lt=get_today_date()))
        )

        return result

    @staticmethod
    def get_on_track_dept_wise_summary():
        from key_result.models import KeyResult

        result_list = Objective.objects.filter(user__team__isnull=False).values(
            department_name=F('user__team__department__name')).annotate(
            total_count=Count('pk', distinct=True),
            not_on_track_count=Count(
                'pk', filter=Q(keyresult__status=KeyResult.StatusChoice.IN_PROGRESS,
                               keyresult__due_date__lt=get_today_date()), distinct=True),
            users_count=Count('user__id', distinct=True),
            department_id=F('user__team__department__id')
        )

        return list(result_list)

    @staticmethod
    def get_on_track_team_wise_summary_for_a_dept(department_id):
        from key_result.models import KeyResult

        result_list = Objective.objects.filter(
            user__team__isnull=False, user__team__department_id=department_id).values(
            team_id=F('user__team__id')).annotate(
            total_count=Count('pk', distinct=True),
            not_on_track_count=Count(
                'pk', filter=Q(keyresult__status=KeyResult.StatusChoice.IN_PROGRESS,
                               keyresult__due_date__lt=get_today_date()), distinct=True),
            team_lead_name=F('user__team__team_lead__first_name')
        )

        return list(result_list)
