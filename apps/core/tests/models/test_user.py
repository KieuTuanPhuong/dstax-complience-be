import pytest

from ...models import User
from ..factories import ClientFactory, LegalEntityFactory, UserFactory


@pytest.mark.django_db
class TestUserModel:
    def test_model_creation(self):
        client = ClientFactory()
        assigned_legal_entities = LegalEntityFactory()
        user = User.objects.create(
            role="DSTAX_ADMIN",
            managed_client=client,
        )
        user.assigned_legal_entities.add(assigned_legal_entities)
        assert user.role == "DSTAX_ADMIN"
        assert user.managed_client == client
        assert assigned_legal_entities in user.assigned_legal_entities.all()
        assert User.objects.count() == 1

    def test_field_assigned_legal_entities_is_ManyToManyField(self):
        user = UserFactory()
        legal_entities1 = LegalEntityFactory()
        legal_entities2 = LegalEntityFactory()
        user.assigned_legal_entities.add(legal_entities1, legal_entities2)
        assert legal_entities1 in user.assigned_legal_entities.all()
        assert legal_entities2 in user.assigned_legal_entities.all()
        assert user.assigned_legal_entities.count() >= 2

    def test_delete_level_set_null(self):
        client = ClientFactory()
        assigned_legal_entities = LegalEntityFactory()
        user = User.objects.create(
            role="DSTAX_ADMIN",
            managed_client=client,
        )
        user.assigned_legal_entities.add(assigned_legal_entities)
        client.delete()
        user.refresh_from_db()
        assert user.managed_client is None

    def test_managed_client_can_null(self):
        user = User.objects.create(role="DSTAX_ADMIN")
        assert user.managed_client is None
