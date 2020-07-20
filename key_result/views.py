from rest_framework import viewsets

from key_result.models import KeyResult
from key_result.serializers import KeyResultSerializer


class KeyResultView(viewsets.ModelViewSet):
    queryset = KeyResult.objects.all()
    serializer_class = KeyResultSerializer
