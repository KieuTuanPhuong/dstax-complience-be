import django_filters

from ..models import LegalEntity


class LegalEntityFilter(django_filters.FilterSet):
    class Meta:
        model = LegalEntity
        fields = {
            "id": ["exact", "in"],
            "client": ["exact", "in"],
            "name": ["exact", "icontains"],
            "is_active": ["exact"],
        }
