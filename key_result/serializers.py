from rest_framework import serializers

from department.models import Department


class KeyResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'objective_id', 'status', 'due_date']
        read_only_fields = ['id']
