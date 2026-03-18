from django.contrib import admin

from ..models.jurisdiction_level import JurisdictionLevel


@admin.register(JurisdictionLevel)
class JurisdictionLevelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_at", "updated_at"]
    ordering = ["id", "name", "created_at", "updated_at"]
