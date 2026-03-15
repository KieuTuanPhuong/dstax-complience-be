import pytest
from django.urls import reverse
from rest_framework import status

from ..factories import (
    FilingFrequencyFactory,
    FilingTypeFactory,
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
