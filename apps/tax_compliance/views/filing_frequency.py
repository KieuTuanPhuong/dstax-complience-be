from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from ..filters import FilingFrequencyFilter
from ..models import FilingFrequency
from ..serializers import FilingFrequencySerializer


@extend_schema(tags=["Tax Compliance: Filing Frequency"])
class FilingFrequencyViewSet(viewsets.ModelViewSet):
    queryset = FilingFrequency.objects.all()
    serializer_class = FilingFrequencySerializer

    @property
    def filterset_class(self):
        return FilingFrequencyFilter
