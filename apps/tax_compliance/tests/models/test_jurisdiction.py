import pytest
from django.db.models import ProtectedError

from apps.tax_compliance.models import Jurisdiction

from ..factories import JurisdictionFactory, JurisdictionLevelFactory


@pytest.mark.django_db
class TestJurisdictionModel:
    def test_create_jurisdiction(self):
        level = JurisdictionLevelFactory(name="United States")
        jurisdiction = JurisdictionFactory(name="California", level=level)
        assert jurisdiction.name == "California"
        assert jurisdiction.level == level
        assert Jurisdiction.objects.count() == 1

    def test_delete_level_protected(self):
        level = JurisdictionLevelFactory()
        JurisdictionFactory(level=level)
        # Should raise ProtectedError because Jurisdiction uses on_delete=models.PROTECT
        with pytest.raises(ProtectedError):
            level.delete()
