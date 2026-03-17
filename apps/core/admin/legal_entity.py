from django.contrib import admin

from ..models import LegalEntity


@admin.register(LegalEntity)
class LegalEntityAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "client",
        "name",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_filter = [
        "id",
        "client",
        "name",
        "is_active",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "id",
        "name",
    ]
