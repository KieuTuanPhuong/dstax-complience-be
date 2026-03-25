import pytest
from django.urls import reverse
from rest_framework import status

from ..factories import ClientFactory, LegalEntityFactory


@pytest.mark.django_db
class TestLegalEntityViewSet:
    def test_list_legal_entity(self, client):
        LegalEntityFactory.create_batch(3)
        url = reverse("legal_entity-list")
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        assert len(results) >= 3

    def test_create_client_invalid_data(self, client):
        url = reverse("legal_entity-list")
        # Missing required 'name'
        data = {}
        response = client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        # Standardized errors format
        error_data = response.json()
        assert error_data["type"] == "validation_error"
        errors = [err["attr"] for err in error_data["errors"]]
        assert "name" in errors

    def test_filter_by_id_in(self, client):
        c1 = LegalEntityFactory(name="legal_entities 1")
        c2 = LegalEntityFactory(name="legal_entities 2")
        LegalEntityFactory(name="legal_entities 3")

        url = reverse("legal_entity-list")
        response = client.get(f"{url}?id__in={c1.id},{c2.id}")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        assert len(results) == 2
        names = [item["name"] for item in results]
        assert "legal_entities 1" in names
        assert "legal_entities 2" in names
        assert "legal_entities 3" not in names

    def test_filter_by_name_icontains(self, client):
        LegalEntityFactory(name="legal_entities 1")
        LegalEntityFactory(name="legal_entities 2")

        url = reverse("legal_entity-list")
        response = client.get(f"{url}?name__icontains=1")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        assert len(results) == 1
        assert results[0]["name"] == "legal_entities 1"

    def test_filter_by_client(self, client):
        c1 = ClientFactory()
        c2 = ClientFactory()
        l1 = LegalEntityFactory(client=c1)
        l2 = LegalEntityFactory(client=c2)
        url = reverse("legal_entity-list")
        response = client.get(f"{url}?client__in={c1.id}")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        assert len(results) == 1
        assert results[0]["client"] == c1.id


@pytest.mark.django_db
class TestLegalEntityPagination:
    def test_pagination_default(self, client):
        LegalEntityFactory.create_batch(30)
        url = reverse("legal_entity-list")
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "count" in data
        assert "results" in data
        assert data["count"] == 30
        assert len(data["results"]) == 25

    def test_pagination_custom_page_size(self, client):
        LegalEntityFactory.create_batch(30)
        url = reverse("legal_entity-list")
        response = client.get(f"{url}?page_size=10")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data["results"]) == 10
        assert data["count"] == 30

    def test_pagination_max_page_size(self, client):
        LegalEntityFactory.create_batch(150)
        url = reverse("legal_entity-list")
        response = client.get(f"{url}?page_size=200")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data["results"]) == 100

    def test_pagination_navigation(self, client):
        LegalEntityFactory.create_batch(50)
        url = reverse("legal_entity-list")
        response = client.get(f"{url}?page=2")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["previous"] is not None
        assert data["next"] is None
        assert len(data["results"]) == 25
