import django_filters

from ..models import Jurisdiction


class JurisdictionFilter(django_filters.FilterSet):
    class Meta:
        model = Jurisdiction
        fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "level": ["exact", "in"],
            "due_date_time": ["exact"],
            "created_at": ["exact", "gte", "lte"],
        }
