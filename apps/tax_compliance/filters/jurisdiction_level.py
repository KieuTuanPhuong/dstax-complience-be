import django_filters

from ..models import JurisdictionLevel


class JurisdictionLevelFilter(django_filters.FilterSet):
    class Meta:
        model = JurisdictionLevel
        fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "created_at": ["exact", "gte", "lte"],
        }
