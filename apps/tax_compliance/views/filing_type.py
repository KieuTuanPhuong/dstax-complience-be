from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from ..filters import FilingTypeFilter
from ..models import FilingType
from ..serializers import FilingTypeSerializer


@extend_schema(tags=["Tax Compliance: Filing Type"])
class FilingTypeViewSet(viewsets.ModelViewSet):
    queryset = FilingType.objects.all()
    serializer_class = FilingTypeSerializer

    @property
    def filterset_class(self):
        return FilingTypeFilter
