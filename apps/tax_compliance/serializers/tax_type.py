from rest_framework import serializers

from ..models import TaxType


class TaxTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxType
        fields = ["id", "name"]
