from django_filters import rest_framework as filters

from ..models import JurisdictionLevel


class JurisdictionLevelFilter(filters.FilterSet):
    class Meta:
        model = JurisdictionLevel
        fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
        }
