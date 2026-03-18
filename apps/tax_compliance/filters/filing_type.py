from django_filters import rest_framework as filters

from ..models import FilingType


class FilingTypeFilter(filters.FilterSet):
    class Meta:
        model = FilingType
        fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "created_at": ["exact", "gte", "lte"],
        }
