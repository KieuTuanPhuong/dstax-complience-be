import pytest

from ...models import LegalEntity
from ...serializers import LegalEntitySerializer
from ..factories import ClientFactory


@pytest.mark.django_db
class TestLegalEntitySerializer:
    def test_creation_api(self):
        client = ClientFactory()
        data = {
            "name": "test",
            "client": client.id,
        }
        serializer = LegalEntitySerializer(data=data)
        assert serializer.is_valid(), serializer.errors
        instance = serializer.save()
        assert instance.name == "test"
        assert instance.client.id == client.id
        assert LegalEntity.objects.count() == 1
