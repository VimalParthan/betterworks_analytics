from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError

from department.models import Department
from objective.models import Objective
from objective.serializers import ObjectiveSerializer
from objective.services import populate_calculated_fields
from user.models import User


class ObjectiveView(viewsets.ModelViewSet):
    queryset = Objective.objects.all()
    serializer_class = ObjectiveSerializer

    @action(methods=["get"], detail=False, url_path="summary", url_name="summary")
    def on_track_summary(self, request):
        on_track_summary = Objective.get_on_track_summary()
        on_track_summary = populate_calculated_fields(on_track_summary)
        return JsonResponse(on_track_summary)

    @action(methods=["get"], detail=False, url_path="department_wise_summary", url_name="department_summary")
    def on_track_dept_wise_summary(self, request):
        on_track_dept_wise_summary = Objective.get_on_track_dept_wise_summary()
        on_track_dept_wise_summary = populate_calculated_fields(on_track_dept_wise_summary)
        summary_list = {"summary_list": on_track_dept_wise_summary}
        return JsonResponse(summary_list)

    @action(methods=["get"], detail=False, url_path="team_wise_summary", url_name="department_summary")
    def on_track_team_wise_summary(self, request):
        department_id = self.request.GET.get('department_id')

        if not department_id or not Department.objects.filter(id=department_id):
            raise ValidationError("please provide a valid department_id")
        on_track_team_wise_summary = Objective.get_on_track_team_wise_summary_for_a_dept(department_id)
        on_track_team_wise_summary = populate_calculated_fields(on_track_team_wise_summary)
        summary_list = {"summary_list": on_track_team_wise_summary}
        return JsonResponse(summary_list)
