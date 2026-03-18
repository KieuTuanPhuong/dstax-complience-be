from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from ..filters import ClientFilter
from ..models import Client
from ..serializers import ClientSerializer


@extend_schema(tags=["Core: Client"])
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @property
    def filterset_class(self):
        return ClientFilter
