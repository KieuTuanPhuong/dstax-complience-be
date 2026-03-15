from rest_framework import serializers

from ..models import FilingFrequency


class FilingFrequencySerializer(serializers.ModelSerializer):
    class Meta:
        model = FilingFrequency
        fields = [
            "id",
            "code",
        ]
