import pytest

from ...models import Client


@pytest.mark.django_db
class TestClientModel:
    def test_model_creation(self):
        client = Client.objects.create(name="Client")
        assert client.name == "Client"
        assert Client.objects.count() == 1
