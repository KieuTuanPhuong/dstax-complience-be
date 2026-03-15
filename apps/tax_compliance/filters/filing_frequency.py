from django_filters import rest_framework as filters

from ..models import FilingFrequency


class FilingFrequencyFilter(filters.FilterSet):
    class Meta:
        model = FilingFrequency
        fields = {
            "id": ["exact", "in"],
            "code": ["exact", "icontains"],
        }
