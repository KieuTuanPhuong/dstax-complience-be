from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from ..filters import LegalEntityFilter
from ..models import LegalEntity
from ..serializers import LegalEntitySerializer


@extend_schema(tags=["Core: Legal Entity"])
class LegalEntityViewSet(viewsets.ModelViewSet):
    queryset = LegalEntity.objects.all()
    serializer_class = LegalEntitySerializer

    @property
    def filterset_class(self):
        return LegalEntityFilter
