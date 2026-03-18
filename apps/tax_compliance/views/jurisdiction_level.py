from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from ..filters import JurisdictionLevelFilter
from ..models import JurisdictionLevel
from ..serializers import JurisdictionLevelSerializer


@extend_schema(tags=["Tax Compliance: Jurisdiction Level"])
class JurisdictionLevelViewSet(viewsets.ModelViewSet):
    queryset = JurisdictionLevel.objects.all()
    serializer_class = JurisdictionLevelSerializer

    @property
    def filterset_class(self):
        return JurisdictionLevelFilter
