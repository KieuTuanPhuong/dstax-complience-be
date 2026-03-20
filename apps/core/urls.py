from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.auth import (
    ChangePasswordView,
    LoginView,
    LogoutView,
    ResetPasswordConfirmView,
    ResetPasswordView,
)
from .views.client import ClientViewSet
from .views.legal_entity import LegalEntityViewSet
from .views.user import UserViewSet

router = DefaultRouter()
router.register(r"client", ClientViewSet)
router.register(r"legal_entity", LegalEntityViewSet, basename="legal_entity")
router.register(r"user", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/login/", LoginView.as_view(), name="auth_login"),
    path("auth/logout/", LogoutView.as_view(), name="auth_logout"),
    path("auth/change-password/", ChangePasswordView.as_view(), name="auth_change_password"),
    path("auth/reset-password/", ResetPasswordView.as_view(), name="auth_reset_password"),
    path(
        "auth/reset-password-confirm/",
        ResetPasswordConfirmView.as_view(),
        name="auth_reset_password_confirm",
    ),
]
