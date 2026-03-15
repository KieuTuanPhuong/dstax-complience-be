from django.contrib import admin

from ..models.tax_type import TaxType


@admin.register(TaxType)
class TaxTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    ordering = ["id", "name"]
