import django_filters

from ..models import FilingFrequency


class FilingFrequencyFilter(django_filters.FilterSet):
    class Meta:
        model = FilingFrequency
        fields = {
            "id": ["exact", "in"],
            "code": ["exact", "icontains"],
            "created_at": ["exact", "gte", "lte"],
        }
