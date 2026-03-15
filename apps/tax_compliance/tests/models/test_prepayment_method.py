import pytest

from ...models import Jurisdiction, JurisdictionLevel, PrepaymentMethod


class TestPrepaymentMethodModel:
    @pytest.mark.django_db
    def test_model_creation(self):
        level = JurisdictionLevel.objects.create(name="United States")
        jurisdiction = Jurisdiction.objects.create(name="California", level=level)
        prepayment_method = PrepaymentMethod.objects.create(
            jurisdiction=jurisdiction, method_description="Credit Card - Visa"
        )
        assert prepayment_method.method_description == "Credit Card - Visa"
        assert PrepaymentMethod.objects.count() == 1
