import pytest

from apps.tax_compliance.models import Jurisdiction, JurisdictionLevel, PrepaymentMethod
from apps.tax_compliance.serializers import PrepaymentMethodSerializer


@pytest.mark.django_db
def test_filing_type_serializers():
    level = JurisdictionLevel.objects.create(name="United States")
    jurisdiction = Jurisdiction.objects.create(name="California", level=level)
    data = {"method_description": "Credit Card - Visa", "jurisdiction_id": jurisdiction.id}
    serializer = PrepaymentMethodSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    instance = serializer.save()
    assert instance.method_description == "Credit Card - Visa"
    assert PrepaymentMethod.objects.count() == 1
