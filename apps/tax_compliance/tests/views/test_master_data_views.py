import pytest
from django.urls import reverse
from rest_framework import status

from ..factories import (
    FilingFrequencyFactory,
    FilingTypeFactory,
    JurisdictionFactory,
    JurisdictionLevelFactory,
    PrepaymentMethodFactory,
    TaxTypeFactory,
)


@pytest.mark.django_db
class TestMasterDataViewSets:
    @pytest.mark.parametrize(
        "url_name,factory_class,search_field,search_value",
        [
            ("filingfrequency-list", FilingFrequencyFactory, "code", "FREQ_X"),
            ("filingtype-list", FilingTypeFactory, "name", "Type X"),
            ("jurisdictionlevel-list", JurisdictionLevelFactory, "name", "Level X"),
            ("taxtype-list", TaxTypeFactory, "name", "Tax X"),
        ],
    )
    def test_master_data_list_and_filter(self, client, url_name, factory_class, search_field, search_value):
        # Create data
        factory_class.create(**{search_field: search_value})
        factory_class.create_batch(2)

        url = reverse(url_name)

        # Test List
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        assert len(results) >= 3

        # Test Filter icontains
        filter_url = f"{url}?{search_field}__icontains={search_value.lower()}"
        response = client.get(filter_url)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        assert len(results) == 1
        assert results[0][search_field] == search_value

        # Test Filter __in
        obj = factory_class.create()
        in_url = f"{url}?id__in={results[0]['id']},{obj.id}"
        response = client.get(in_url)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        assert len(results) == 2

    def test_prepayment_method_viewset(self, client):
        pm = PrepaymentMethodFactory(method_description="Visa Card")
        url = reverse("prepaymentmethod-list")

        # Test Filter
        response = client.get(f"{url}?method_description__icontains=visa")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        assert len(results) == 1
        assert results[0]["method_description"] == "Visa Card"

    @pytest.mark.parametrize(
        "url_name,factory_class,time",
        [
            ("filingfrequency-list", FilingFrequencyFactory, "2024-01-01T00:00:00Z"),
            ("filingtype-list", FilingTypeFactory, "2024-01-01T00:00:00Z"),
            ("jurisdictionlevel-list", JurisdictionLevelFactory, "2024-01-01T00:00:00Z"),
            ("taxtype-list", TaxTypeFactory, "2024-01-01T00:00:00Z"),
            ("jurisdiction-list", JurisdictionFactory, "2024-01-01T00:00:00Z"),
            ("prepaymentmethod-list", PrepaymentMethodFactory, "2024-01-01T00:00:00Z"),
        ],
    )
    def test_master_data_list_and_filter_created_at(self, client, url_name, factory_class, time):
        factory_class.create_batch(3)

        url = reverse(url_name)
        created_at_url = f"{url}?created_at__gt={time}"
        # Test List
        response = client.get(created_at_url)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        results = data.get("results") if isinstance(data, dict) and "results" in data else data
        assert len(results) >= 3


@pytest.mark.django_db
class TestPagination:
    @pytest.mark.parametrize(
        "url_name,factory_class",
        [
            ("filingfrequency-list", FilingFrequencyFactory),
            ("filingtype-list", FilingTypeFactory),
            ("jurisdictionlevel-list", JurisdictionLevelFactory),
            ("taxtype-list", TaxTypeFactory),
            ("prepaymentmethod-list", PrepaymentMethodFactory),
        ],
    )
    def test_pagination_default(self, client, url_name, factory_class):
        factory_class.create_batch(30)
        url = reverse(url_name)
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "count" in data
        assert "results" in data
        assert data["count"] == 30
        assert len(data["results"]) == 25

    @pytest.mark.parametrize(
        "url_name,factory_class",
        [
            ("filingfrequency-list", FilingFrequencyFactory),
            ("filingtype-list", FilingTypeFactory),
            ("jurisdictionlevel-list", JurisdictionLevelFactory),
            ("taxtype-list", TaxTypeFactory),
            ("prepaymentmethod-list", PrepaymentMethodFactory),
        ],
    )
    def test_pagination_custom_page_size(self, client, url_name, factory_class):
        factory_class.create_batch(30)
        url = reverse(url_name)
        response = client.get(f"{url}?page_size=10")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data["results"]) == 10
        assert data["count"] == 30

    @pytest.mark.parametrize(
        "url_name,factory_class",
        [
            ("filingfrequency-list", FilingFrequencyFactory),
            ("filingtype-list", FilingTypeFactory),
            ("jurisdictionlevel-list", JurisdictionLevelFactory),
            ("taxtype-list", TaxTypeFactory),
            ("prepaymentmethod-list", PrepaymentMethodFactory),
        ],
    )
    def test_pagination_max_page_size(self, client, url_name, factory_class):
        factory_class.create_batch(150)
        url = reverse(url_name)
        response = client.get(f"{url}?page_size=200")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data["results"]) == 100

    @pytest.mark.parametrize(
        "url_name,factory_class",
        [
            ("filingfrequency-list", FilingFrequencyFactory),
            ("filingtype-list", FilingTypeFactory),
            ("jurisdictionlevel-list", JurisdictionLevelFactory),
            ("taxtype-list", TaxTypeFactory),
            ("prepaymentmethod-list", PrepaymentMethodFactory),
        ],
    )
    def test_pagination_navigation(self, client, url_name, factory_class):
        factory_class.create_batch(50)
        url = reverse(url_name)
        response = client.get(f"{url}?page=2")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["previous"] is not None
        assert data["next"] is None
        assert len(data["results"]) == 25
