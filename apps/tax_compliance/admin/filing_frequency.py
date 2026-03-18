from django.contrib import admin

from ..models.filing_frequency import FilingFrequency


@admin.register(FilingFrequency)
class FilingFrequencyAdmin(admin.ModelAdmin):
    list_display = ["id", "code", "created_at", "updated_at"]
    odering = ["id", "code", "created_at", "updated_at"]
