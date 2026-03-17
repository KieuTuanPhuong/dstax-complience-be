from rest_framework import serializers

from ..models import LegalEntity, User
from .legal_entity import LegalEntitySerializer


class UserSerializer(serializers.ModelSerializer):
    assigned_legal_entities = LegalEntitySerializer(read_only=True, many=True)

    assigned_legal_entity_ids = serializers.PrimaryKeyRelatedField(
        queryset=LegalEntity.objects.all(), many=True, write_only=True, source="assigned_legal_entities"
    )

    class Meta:
        model = User
        fields = ["role", "managed_client", "assigned_legal_entities", "assigned_legal_entity_ids"]
