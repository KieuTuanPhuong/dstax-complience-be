import pytest

from ...models import Client
from ...serializers import ClientSerializer


@pytest.mark.django_db
class TestClientSerializer:
    def test_creation_api(self):
        data = {"name": "test"}
        serializer = ClientSerializer(data=data)
        assert serializer.is_valid(), serializer.errors
        instance = serializer.save()
        assert instance.name == "test"
        assert Client.objects.count()
