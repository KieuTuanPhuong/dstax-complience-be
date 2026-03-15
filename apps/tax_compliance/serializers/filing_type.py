from rest_framework import serializers

from ..models import FilingType


class FilingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilingType
        fields = [
            "id",
            "name",
        ]
