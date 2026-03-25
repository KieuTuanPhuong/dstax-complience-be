import pytest
from django.urls import reverse
from rest_framework import status

from ..factories import JurisdictionFactory, JurisdictionLevelFactory


@pytest.mark.django_db
class TestJurisdictionViewSet:
    def test_list_jurisdictions(self, client):
        JurisdictionFactory.create_batch(3)
        url = reverse("jurisdiction-list")
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        # Check if we have results (handling potential pagination)
        data = response.json()
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        assert len(results) >= 3

    def test_filter_by_id_in(self, client):
        j1 = JurisdictionFactory(name="California")
        j2 = JurisdictionFactory(name="Texas")
        JurisdictionFactory(name="New York")

        url = reverse("jurisdiction-list")
        response = client.get(f"{url}?id__in={j1.id},{j2.id}")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        assert len(results) == 2
        names = [item["name"] for item in results]
        assert "California" in names
        assert "Texas" in names
        assert "New York" not in names

    def test_filter_by_name_icontains(self, client):
        JurisdictionFactory(name="California")
        JurisdictionFactory(name="Texas")

        url = reverse("jurisdiction-list")
        response = client.get(f"{url}?name__icontains=cali")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        assert len(results) == 1
        assert results[0]["name"] == "California"

    def test_filter_by_level_in(self, client):
        l1 = JurisdictionLevelFactory(name="Level 1")
        l2 = JurisdictionLevelFactory(name="Level 2")
        l3 = JurisdictionLevelFactory(name="Level 3")
        JurisdictionFactory(level=l1)
        JurisdictionFactory(level=l2)
        JurisdictionFactory(level=l3)

        url = reverse("jurisdiction-list")
        response = client.get(f"{url}?level__in={l1.id},{l2.id}")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        assert len(results) == 2

    def test_create_jurisdiction_invalid_data(self, client):
        url = reverse("jurisdiction-list")
        # Missing required 'level'
        data = {"name": "Invalid Jurisdiction"}
        response = client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

        # Standardized errors format
        error_data = response.json()
        assert error_data["type"] == "validation_error"
        errors = [err["attr"] for err in error_data["errors"]]
        assert "level" in errors


@pytest.mark.django_db
class TestPagination:
    def test_default_pagination(self, client):
        level = JurisdictionLevelFactory(name="Country")
        for i in range(30):
            JurisdictionFactory(name=f"Jurisdiction {i}", level=level)

        url = reverse("jurisdiction-list")
        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        assert "count" in data
        assert "results" in data
        assert data["count"] == 30
        assert len(data["results"]) == 25

    def test_custom_page_size(self, client):
        level = JurisdictionLevelFactory(name="Country")
        for i in range(30):
            JurisdictionFactory(name=f"Jurisdiction {i}", level=level)

        url = reverse("jurisdiction-list")
        response = client.get(f"{url}?page_size=10")

        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        assert len(data["results"]) == 10
        assert data["count"] == 30

    def test_page_size_beyond_max(self, client):
        level = JurisdictionLevelFactory(name="Country")
        for i in range(150):
            JurisdictionFactory(name=f"Jurisdiction {i}", level=level)

        url = reverse("jurisdiction-list")
        response = client.get(f"{url}?page_size=200")

        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        assert len(data["results"]) == 100

    def test_pagination_navigation(self, client):
        level = JurisdictionLevelFactory(name="Country")
        for i in range(50):
            JurisdictionFactory(name=f"Jurisdiction {i}", level=level)

        url = reverse("jurisdiction-list")
        response = client.get(f"{url}?page=2")

        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        assert data["previous"] is not None
        assert data["next"] is None
        assert len(data["results"]) == 25

    def test_first_page_no_previous(self, client):
        level = JurisdictionLevelFactory(name="Country")
        for i in range(30):
            JurisdictionFactory(name=f"Jurisdiction {i}", level=level)

        url = reverse("jurisdiction-list")
        response = client.get(f"{url}?page=1")

        assert response.status_code == status.HTTP_200_OK
        data = response.json()

        assert data["previous"] is None
        assert data["next"] is not None

    def test_invalid_page_returns_404(self, client):
        level = JurisdictionLevelFactory(name="Country")
        for i in range(30):
            JurisdictionFactory(name=f"Jurisdiction {i}", level=level)

        url = reverse("jurisdiction-list")
        response = client.get(f"{url}?page=999")

        assert response.status_code == status.HTTP_404_NOT_FOUND
