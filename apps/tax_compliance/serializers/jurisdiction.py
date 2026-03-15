from rest_framework import serializers

from ..models import Jurisdiction


class JurisdictionSerializer(serializers.ModelSerializer):
    level_name = serializers.CharField(source="level.name", read_only=True)

    class Meta:
        model = Jurisdiction
        fields = [
            "id",
            "name",
            "level",
            "level_name",
            "due_date_time",
        ]
