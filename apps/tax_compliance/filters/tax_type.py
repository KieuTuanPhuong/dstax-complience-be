import django_filters

from ..models import TaxType


class TaxTypeFilter(django_filters.FilterSet):
    class Meta:
        model = TaxType
        fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "created_at": ["exact", "gte", "lte"],
        }
