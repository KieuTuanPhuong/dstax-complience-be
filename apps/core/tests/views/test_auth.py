import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()


@pytest.mark.django_db
class TestAuthAPI:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def user_data(self):
        return {
            "email": "test@example.com",
            "password": "testpassword123",
            "role": "DSTAX_ADMIN",
        }

    @pytest.fixture
    def created_user(self, user_data):
        user = User.objects.create_user(
            email=user_data["email"],
            username=user_data["email"],
            password=user_data["password"],
            role=user_data["role"],
        )
        return user

    def test_login_success(self, api_client, created_user, user_data):
        url = reverse("auth_login")
        response = api_client.post(
            url, {"email": user_data["email"], "password": user_data["password"]}
        )
        assert response.status_code == status.HTTP_200_OK
        assert "access" in response.data
        assert "refresh" in response.data

    def test_logout_success(self, api_client, created_user, user_data):
        # Login first
        login_url = reverse("auth_login")
        login_res = api_client.post(
            login_url, {"email": user_data["email"], "password": user_data["password"]}
        )
        refresh_token = login_res.data["refresh"]

        # Logout
        logout_url = reverse("auth_logout")
        response = api_client.post(logout_url, {"refresh": refresh_token})
        assert response.status_code == status.HTTP_200_OK

    def test_change_password_success(self, api_client, created_user, user_data):
        api_client.force_authenticate(user=created_user)
        url = reverse("auth_change_password")
        data = {
            "old_password": user_data["password"],
            "new_password": "newpassword123",
            "confirm_password": "newpassword123",
        }
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert created_user.check_password("newpassword123")

    def test_reset_password_request_success(self, api_client, created_user):
        url = reverse("auth_reset_password")
        response = api_client.post(url, {"email": created_user.email})
        assert response.status_code == status.HTTP_200_OK
        assert "Password reset email sent." in response.data["detail"]
