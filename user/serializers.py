from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from objective.models import Objective
from team.models import Team
from user.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'team_id']
        read_only_fields = ['id']

    def validate(self, data):
        team_id = self.initial_data.get('team_id')

        if not team_id:
            return self.data

        try:
            team = Team.objects.get(id=data.get('team_id'))
        except Exception as e:
            raise ValidationError('invalid team id')
