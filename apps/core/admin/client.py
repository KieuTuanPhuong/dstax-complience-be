from django.contrib import admin

from ..models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "is_active",
        "created_at",
        "updated_at",
    ]
    list_filter = [
        "id",
        "name",
        "is_active",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "id",
        "name",
    ]
