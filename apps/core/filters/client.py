from django_filters import rest_framework as filters

from ..models import Client


class ClientFilter(filters.FilterSet):
    class Meta:
        model = Client
        fields = {"id": ["exact", "in"], "name": ["exact", "icontains"], "is_active": ["exact"]}
