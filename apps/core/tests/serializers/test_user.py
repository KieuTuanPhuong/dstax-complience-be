import pytest

from ...serializers import UserSerializer
from ..factories import ClientFactory, LegalEntityFactory


@pytest.mark.django_db
class TestUserSerializer:
    def test_creation_api(self):
        managed_client = ClientFactory()
        legal_entity = LegalEntityFactory()
        data = {
            "role": "DSTAX_ADMIN",
            "managed_client": managed_client.id,
            "assigned_legal_entity_ids": [legal_entity.id],
        }
        serializer = UserSerializer(data=data)
        assert serializer.is_valid(), serializer.errors
        instance = serializer.save()
        assert instance.role == "DSTAX_ADMIN"
        assert instance.managed_client == managed_client
        assert legal_entity in instance.assigned_legal_entities.all()

    def test_assigned_legal_entities_is_many_to_many_fields(self):
        managed_client = ClientFactory()
        legal_entities1 = LegalEntityFactory()
        legal_entities2 = LegalEntityFactory()
        data = {
            "role": "DSTAX_ADMIN",
            "managed_client": managed_client.id,
            "assigned_legal_entity_ids": [legal_entities1.id, legal_entities2.id],
        }
        serializer = UserSerializer(data=data)
        assert serializer.is_valid(), serializer.errors
        instance = serializer.save()
        assert legal_entities1 in instance.assigned_legal_entities.all()
        assert legal_entities2 in instance.assigned_legal_entities.all()
