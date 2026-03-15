import pytest

from apps.tax_compliance.models import JurisdictionLevel
from apps.tax_compliance.serializers import JurisdictionLevelSerializer


@pytest.mark.django_db
def test_tax_type_serializers():
    data = {
        "name": "Country",
    }
    serializer = JurisdictionLevelSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    instance = serializer.save()
    assert instance.name == "Country"
    assert JurisdictionLevel.objects.count() == 1
