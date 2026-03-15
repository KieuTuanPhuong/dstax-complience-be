from django.contrib import admin

from ..models.jurisdiction import Jurisdiction


@admin.register(Jurisdiction)
class JurisdictionAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "level"]
    ordering = ["id", "name", "level"]
