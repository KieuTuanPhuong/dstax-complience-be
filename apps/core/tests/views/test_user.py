import pytest
from django.urls import reverse
from rest_framework import status

from ..factories import ClientFactory, LegalEntityFactory, UserFactory


@pytest.mark.django_db
class TestUserViewSet:
    def test_list_user(self, client):
        UserFactory.create_batch(3)
        url = reverse("user-list")
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data) >= 3

    def test_list_assigned_legal_entities(self, client):
        legal_entities = LegalEntityFactory.create_batch(3)
        u1 = UserFactory()
        u1.assigned_legal_entities.set([legal_entities[0], legal_entities[1]])
        u2 = UserFactory()
        u2.assigned_legal_entities.set([legal_entities[0], legal_entities[1]])
        u3 = UserFactory()
        u3.assigned_legal_entities.set([legal_entities[2]])
        url = reverse("user-list")
        response = client.get(f"{url}?assigned_legal_entities={legal_entities[0].name},{legal_entities[1].name}")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        assert len(results) == 2
        assert results[0]["assigned_legal_entities"][0]["name"] == legal_entities[0].name

    def test_filter_by_id_in(self, client):
        clients = ClientFactory.create_batch(3)
        u1 = UserFactory(managed_client=clients[0])
        u2 = UserFactory(managed_client=clients[1])
        u3 = UserFactory(managed_client=clients[2])
        url = reverse("user-list")
        response = client.get(f"{url}?managed_client__in={clients[0].id},{clients[1].id}")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        assert len(results) == 2

    def test_filter_by_managed_client_in(self, client):
        j1 = UserFactory()
        j2 = UserFactory()
        j3 = UserFactory()
        url = reverse("user-list")
        response = client.get(f"{url}?id__in={j1.id},{j2.id}")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        assert len(results) == 2
