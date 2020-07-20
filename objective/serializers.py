from rest_framework import serializers

from objective.models import Objective


class ObjectiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Objective
        fields = ['id', 'user_id', 'objective_text']
        read_only_fields = ['id']
