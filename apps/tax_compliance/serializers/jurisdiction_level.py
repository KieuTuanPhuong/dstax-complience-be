from rest_framework import serializers

from ..models import JurisdictionLevel


class JurisdictionLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = JurisdictionLevel
        fields = [
            "id",
            "name",
        ]
