from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    FilingFrequencyViewSet,
    FilingTypeViewSet,
    JurisdictionLevelViewSet,
    JurisdictionViewSet,
    PrepaymentMethodViewSet,
    TaxTypeViewSet,
)

router = DefaultRouter()
router.register(r"prepayment_methods", PrepaymentMethodViewSet)
router.register(r"jurisdiction_level", JurisdictionLevelViewSet)
router.register(r"filing_frequency", FilingFrequencyViewSet)
router.register(r"filing_type", FilingTypeViewSet)
router.register(r"jurisdiction", JurisdictionViewSet)
router.register(r"tax_type", TaxTypeViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
