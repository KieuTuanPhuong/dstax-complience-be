import pytest

from ...models import LegalEntity
from ..factories import ClientFactory


@pytest.mark.django_db
class TestLegalEntityModel:
    def test_model_creation(self):
        client = ClientFactory()
        legal_entity = LegalEntity.objects.create(client=client, name="legal_entity")
        assert legal_entity.client == client
        assert legal_entity.name == "legal_entity"
        assert LegalEntity.objects.count() == 1

    def test_delete_level_CASCADE(self):
        client = ClientFactory()
        legal_entity = LegalEntity.objects.create(client=client, name="legal_entity")
        legal_entity_id = legal_entity.id
        client.delete()
        exists = LegalEntity.objects.filter(id=legal_entity_id).exists()
        assert exists is False
