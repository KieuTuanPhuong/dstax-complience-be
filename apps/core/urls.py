from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ClientViewSet,
    LegalEntityViewSet,
    UserViewSet,
)

router = DefaultRouter()
router.register(r"client", ClientViewSet)
router.register(r"legal_entity", LegalEntityViewSet, basename="legal_entity")
router.register(r"user", UserViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
