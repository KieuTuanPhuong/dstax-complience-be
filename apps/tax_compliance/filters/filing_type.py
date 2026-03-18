import django_filters

from ..models import FilingType


class FilingTypeFilter(django_filters.FilterSet):
    class Meta:
        model = FilingType
        fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "created_at": ["exact", "gte", "lte"],
        }
