import django_filters

from ..models import User


class UserFilter(django_filters.FilterSet):
    assigned_legal_entities = django_filters.CharFilter(method="filter_assigned_legal_entities")

    class Meta:
        model = User
        fields = {
            "id": ["exact", "in"],
            "role": ["exact"],
            "managed_client": ["exact", "in"],
        }

    def filter_assigned_legal_entities(self, queryset, name, value):
        if not value:
            return queryset
        entities_list = [entity.strip() for entity in value.split(",")]
        return queryset.filter(assigned_legal_entities__name__in=entities_list).distinct()
