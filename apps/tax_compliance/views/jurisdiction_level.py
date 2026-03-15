from rest_framework import viewsets

from ..filters import JurisdictionLevelFilter
from ..models import JurisdictionLevel
from ..serializers import JurisdictionLevelSerializer


class JurisdictionLevelViewSet(viewsets.ModelViewSet):
    queryset = JurisdictionLevel.objects.all()
    serializer_class = JurisdictionLevelSerializer

    @property
    def filterset_class(self):
        return JurisdictionLevelFilter
