import pytest
from django.db.utils import IntegrityError

from apps.tax_compliance.models import FilingType


class TestFilingTypeModel:
    @pytest.mark.django_db
    def test_model_creation(self):
        filing_type = FilingType.objects.create(name="Civil Complaint")
        assert filing_type.name == "Civil Complaint"
        assert FilingType.objects.count() == 1

    @pytest.mark.django_db
    def test_unique_name(self):
        FilingType.objects.create(name="Civil Complaint")
        with pytest.raises(IntegrityError):
            FilingType.objects.create(name="Civil Complaint")
