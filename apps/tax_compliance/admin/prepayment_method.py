from django.contrib import admin

from ..models.prepayment_method import PrepaymentMethod


@admin.register(PrepaymentMethod)
class PrepaymentMethod(admin.ModelAdmin):
    list_display = ["id", "jurisdiction", "method_description", "created_at", "updated_at"]
    ordering = ["id", "jurisdiction", "created_at", "updated_at"]
