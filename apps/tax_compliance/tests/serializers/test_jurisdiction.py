import pytest

from apps.tax_compliance.models import Jurisdiction, JurisdictionLevel
from apps.tax_compliance.serializers import JurisdictionSerializer


@pytest.mark.django_db
@pytest.mark.parametrize(
    "name",
    [
        "California",
        "Texas",
    ],
)
def test_jurisdiction_serializers(name):
    level = JurisdictionLevel.objects.create(name="Country")
    data = {"name": f"{name}", "level": level.id, "due_date_time": "2026-03-11T10:00:00Z"}
    serializer = JurisdictionSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    assert serializer.validated_data["name"] == name
    instance = serializer.save()
    assert instance.name == name
    assert Jurisdiction.objects.count() == 1
