import django_filters

from ..models import PrepaymentMethod


class PrepaymentMethodFilter(django_filters.FilterSet):
    class Meta:
        model = PrepaymentMethod
        fields = {
            "id": ["exact", "in"],
            "jurisdiction": ["exact", "in"],
            "method_description": ["exact", "icontains"],
            "created_at": ["exact", "gte", "lte"],
        }
