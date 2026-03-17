from django_filters import rest_framework as filters

from ..models import LegalEntity


class LegalEntityFilter(filters.FilterSet):
    class Meta:
        model = LegalEntity
        fields = {
            "id": ["exact", "in"],
            "client": ["exact", "in"],
            "name": ["exact", "icontains"],
            "is_active": ["exact"],
        }
