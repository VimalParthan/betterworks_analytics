from rest_framework import viewsets

from team.models import Team
from team.serializers import TeamSerializer


class TeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
