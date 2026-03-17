from rest_framework import serializers

from ..models import LegalEntity


class LegalEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalEntity
        fields = ["client", "name", "is_active"]
