import factory
from factory.django import DjangoModelFactory

from apps.tax_compliance.models import (
    FilingFrequency,
    FilingType,
    Jurisdiction,
    JurisdictionLevel,
    PrepaymentMethod,
    TaxType,
)


class FilingFrequencyFactory(DjangoModelFactory):
    class Meta:
        model = FilingFrequency

    code = factory.Sequence(lambda n: f"FREQ_{n}")


class FilingTypeFactory(DjangoModelFactory):
    class Meta:
        model = FilingType

    name = factory.Sequence(lambda n: f"Filing Type {n}")


class JurisdictionLevelFactory(DjangoModelFactory):
    class Meta:
        model = JurisdictionLevel

    name = factory.Sequence(lambda n: f"Level {n}")


class JurisdictionFactory(DjangoModelFactory):
    class Meta:
        model = Jurisdiction

    name = factory.Sequence(lambda n: f"Jurisdiction {n}")
    level = factory.SubFactory(JurisdictionLevelFactory)


class PrepaymentMethodFactory(DjangoModelFactory):
    class Meta:
        model = PrepaymentMethod

    jurisdiction = factory.SubFactory(JurisdictionFactory)
    method_description = "Default Description"


class TaxTypeFactory(DjangoModelFactory):
    class Meta:
        model = TaxType

    name = factory.Sequence(lambda n: f"Tax Type {n}")
