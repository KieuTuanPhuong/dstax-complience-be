from django.contrib import admin

from ..models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "managed_client",
        "role",
        "get_assigned_legal_entities",
        "created_at",
        "updated_at",
    ]
    list_filter = [
        "id",
        "managed_client",
        "role",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "id",
        "managed_client",
    ]

    def get_assigned_legal_entities(self, obj):
        return ", ".join([entity.name for entity in obj.assigned_legal_entities.all()])

    get_assigned_legal_entities.short_description = "Assigned Legal Entities"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related("assigned_legal_entities")
