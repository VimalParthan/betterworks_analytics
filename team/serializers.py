from rest_framework import serializers

from team.models import Team


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'team_lead_id', 'department_id', 'average_pay']
        read_only_fields = ['id']
