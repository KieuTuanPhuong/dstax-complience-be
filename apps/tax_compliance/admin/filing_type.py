from django.contrib import admin

from ..models.filing_type import FilingType


@admin.register(FilingType)
class FilingTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    odering = ["id", "name"]
