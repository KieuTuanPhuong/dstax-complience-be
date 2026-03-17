import pytest
from django.urls import reverse
from rest_framework import status

from ..factories import ClientFactory


@pytest.mark.django_db
class TestClientViewSet:
    def test_list_client(self, client):
        ClientFactory.create_batch(3)
        url = reverse("client-list")
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data) >= 3

    def test_filter_by_id_in(self, client):
        j1 = ClientFactory(name="DS_TAX")
        j2 = ClientFactory(name="Apple")
        url = reverse("client-list")
        response = client.get(f"{url}?id__in={j1.id},{j2.id}")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        assert len(results) == 2
        names = [item["name"] for item in results]
        assert "DS_TAX" in names
        assert "Apple" in names

    def test_filter_by_is_active(self, client):
        j1 = ClientFactory(name="DS_TAX")
        j2 = ClientFactory(name="Apple")

        url = reverse("client-list")
        response = client.get(f"{url}?is_active=True")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        assert len(results) == 2
        assert results[0]["name"] == "DS_TAX"

    def test_filter_by_name_icontains(self, client):
        j1 = ClientFactory(name="DS_TAX")
        j2 = ClientFactory(name="Apple")
        url = reverse("client-list")
        response = client.get(f"{url}?name__icontains=DS")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        assert len(results) == 1
        assert results[0]["name"] == "DS_TAX"
