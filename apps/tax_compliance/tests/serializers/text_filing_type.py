import pytest

from apps.tax_compliance.models import FilingType
from apps.tax_compliance.serializers import FilingTypeSerializer


@pytest.mark.django_db
def test_filing_type_serializers():
    data = {
        "name": "Civil Complaint",
    }
    serializer = FilingTypeSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    instance = serializer.save()
    assert instance.name == "Civil Complaint"
    assert FilingType.objects.count() == 1
