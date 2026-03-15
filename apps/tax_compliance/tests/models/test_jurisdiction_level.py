import pytest
from django.db.utils import IntegrityError

from apps.tax_compliance.models import JurisdictionLevel


class TestJurisdictionLevelModel:
    @pytest.mark.django_db
    def test_model_creation(self):
        level = JurisdictionLevel.objects.create(name="Country")
        assert level.name == "Country"
        assert JurisdictionLevel.objects.count() == 1

    @pytest.mark.django_db
    def test_unique_name(self):
        JurisdictionLevel.objects.create(name="City")
        with pytest.raises(IntegrityError):
            JurisdictionLevel.objects.create(name="City")
