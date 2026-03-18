from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from ..filters import JurisdictionFilter
from ..models import Jurisdiction
from ..serializers import JurisdictionSerializer


@extend_schema(tags=["Tax Compliance: Jurisdiction"])
class JurisdictionViewSet(viewsets.ModelViewSet):
    queryset = Jurisdiction.objects.all()
    serializer_class = JurisdictionSerializer

    @property
    def filterset_class(self):
        return JurisdictionFilter
