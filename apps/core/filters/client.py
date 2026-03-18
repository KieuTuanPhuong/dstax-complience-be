import django_filters

from ..models import Client


class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = {"id": ["exact", "in"], "name": ["exact", "icontains"], "is_active": ["exact"]}
