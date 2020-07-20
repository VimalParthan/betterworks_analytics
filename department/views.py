from rest_framework import viewsets

from department.models import Department
from department.serializers import DepartmentSerializer


class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

