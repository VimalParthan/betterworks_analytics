from rest_framework import serializers

from department.models import Department


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'location', 'date_of_inauguration']
        read_only_fields = ['id']
