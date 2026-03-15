import pytest
from django.db.utils import IntegrityError

from apps.tax_compliance.models import FilingFrequency


class TestFilingFrequencyModel:
    @pytest.mark.django_db
    def test_model_creation(self):
        filing_type = FilingFrequency.objects.create(code="ANNUAL")
        assert filing_type.code == "ANNUAL"
        assert FilingFrequency.objects.count() == 1

    @pytest.mark.django_db
    def test_unique_code(self):
        FilingFrequency.objects.create(code="ANNUAL")
        with pytest.raises(IntegrityError):
            FilingFrequency.objects.create(code="ANNUAL")
