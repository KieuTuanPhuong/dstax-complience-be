from django.contrib import admin

from ..models.filing_type import FilingType


@admin.register(FilingType)
class FilingTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_at", "updated_at"]
    odering = ["id", "name", "created_at", "updated_at"]
