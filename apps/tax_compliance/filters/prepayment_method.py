from django_filters import rest_framework as filters

from ..models import PrepaymentMethod


class PrepaymentMethodFilter(filters.FilterSet):
    class Meta:
        model = PrepaymentMethod
        fields = {
            "id": ["exact", "in"],
            "jurisdiction": ["exact", "in"],
            "method_description": ["exact", "icontains"],
            "created_at": ["exact", "gte", "lte"],
        }
