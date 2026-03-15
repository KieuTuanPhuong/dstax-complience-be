from rest_framework import serializers

from ..models import Jurisdiction, PrepaymentMethod
from ..serializers import JurisdictionSerializer


class PrepaymentMethodSerializer(serializers.ModelSerializer):
    jurisdiction = JurisdictionSerializer(read_only=True)
    jurisdiction_id = serializers.PrimaryKeyRelatedField(
        queryset=Jurisdiction.objects.all(),
        write_only=True,
        source="jurisdiction",
    )

    class Meta:
        model = PrepaymentMethod
        fields = ["id", "jurisdiction", "method_description", "jurisdiction_id"]
