from django.contrib import admin

from ..models.tax_type import TaxType


@admin.register(TaxType)
class TaxTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_at", "updated_at"]
    ordering = ["id", "name", "created_at", "updated_at"]
