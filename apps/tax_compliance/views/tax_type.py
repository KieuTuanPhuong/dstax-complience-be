from rest_framework import viewsets

from ..filters import TaxTypeFilter
from ..models import TaxType
from ..serializers import TaxTypeSerializer


class TaxTypeViewSet(viewsets.ModelViewSet):
    queryset = TaxType.objects.all()
    serializer_class = TaxTypeSerializer

    @property
    def filterset_class(self):
        return TaxTypeFilter
