from rest_framework import viewsets

from ..filters import LegalEntityFilter
from ..models import LegalEntity
from ..serializers import LegalEntitySerializer


class LegalEntityViewSet(viewsets.ModelViewSet):
    queryset = LegalEntity.objects.all()
    serializer_class = LegalEntitySerializer

    @property
    def filterset_class(self):
        return LegalEntityFilter
