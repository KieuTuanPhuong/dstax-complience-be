import pytest

from apps.tax_compliance.models import FilingFrequency
from apps.tax_compliance.serializers import FilingFrequencySerializer


@pytest.mark.django_db
def test_filing_type_serializers():
    data = {
        "code": "ANNUAL",
    }
    serializer = FilingFrequencySerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    instance = serializer.save()
    assert instance.code == "ANNUAL"
    assert FilingFrequency.objects.count() == 1
