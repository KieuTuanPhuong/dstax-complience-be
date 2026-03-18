from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from ..filters import TaxTypeFilter
from ..models import TaxType
from ..serializers import TaxTypeSerializer


@extend_schema(tags=["Tax Compliance: Tax Type"])
class TaxTypeViewSet(viewsets.ModelViewSet):
    queryset = TaxType.objects.all()
    serializer_class = TaxTypeSerializer

    @property
    def filterset_class(self):
        return TaxTypeFilter
