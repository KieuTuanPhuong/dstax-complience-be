import factory
from factory.django import DjangoModelFactory

from apps.core.models import (
    Client,
    LegalEntity,
    User,
)


class ClientFactory(DjangoModelFactory):
    class Meta:
        model = Client

    name = factory.Sequence(lambda n: f"Client {n}")


class LegalEntityFactory(DjangoModelFactory):
    class Meta:
        model = LegalEntity

    client = factory.SubFactory(ClientFactory)
    name = factory.Sequence(lambda n: f"LegalEntity {n}")


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    managed_client = factory.SubFactory(ClientFactory)

    @factory.post_generation
    def assigned_legal_entities(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of groups using bulk addition
        self.assigned_legal_entities.add(*extracted)
