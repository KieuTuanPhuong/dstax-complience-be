from django_filters import rest_framework as filters

from ..models import TaxType


class TaxTypeFilter(filters.FilterSet):
    class Meta:
        model = TaxType
        fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
        }
