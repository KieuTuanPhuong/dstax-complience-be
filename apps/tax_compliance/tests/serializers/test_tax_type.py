import pytest

from apps.tax_compliance.models import TaxType
from apps.tax_compliance.serializers import TaxTypeSerializer


@pytest.mark.django_db
def test_tax_type_serializers():
    data = {
        "name": "Credit Card - Visa",
    }
    serializer = TaxTypeSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    instance = serializer.save()
    assert instance.name == "Credit Card - Visa"
    assert TaxType.objects.count() == 1
