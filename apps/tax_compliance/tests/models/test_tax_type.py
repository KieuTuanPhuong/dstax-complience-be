import pytest
from django.db.utils import IntegrityError

from ...models import TaxType


class TestTaxTypeModel:
    @pytest.mark.django_db
    def test_model_creation(self):
        tax_type = TaxType.objects.create(name="Credit Card - Visa")
        assert tax_type.name == "Credit Card - Visa"
        assert TaxType.objects.count() == 1

    @pytest.mark.django_db
    def test_unique_name(self):
        TaxType.objects.create(name="Credit Card - Visa")
        with pytest.raises(IntegrityError):
            TaxType.objects.create(name="Credit Card - Visa")
