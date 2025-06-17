import pytest
import requests
from urllib.parse import urljoin

class TestProtectedAPI:
    BASE_URL = "http://172.16.1.247"
    USERS_WITH_GROUPS_ENDPOINT = "/api/ctrl/version"
    USERS_WITH_GROUPS_ENDPOINT = "/api/realms/master/users-with-groups"

    @pytest.fixture
    def valid_token(self):
        """Получение валидного токена"""
        token_url = urljoin(self.BASE_URL, "/api/realms/master/protocol/openid-connect/token")
        data = {
            "grant_type": "password",
            "client_id": "public_client",
            "username": "user01",
            "password": "bitnami1",
            "scope": "openid groups",
        }
        response = requests.post(token_url, data=data)
        return response.json()["access_token"]


    def test_groups(self, valid_token):
        """Тест на налищие поля groups"""
        url = urljoin(self.BASE_URL, self.USERS_WITH_GROUPS_ENDPOINT)
        headers = {"Authorization": f"Bearer {valid_token}"}

        response = requests.get(url, headers=headers)

        assert response.status_code == 200
        for item in response.json():
            assert "groups" in item  # Проверяем наличие ожидаемого поля в ответе

    def test_access_with_valid_token(self, valid_token):
        """Тест доступа с валидным токеном"""
        url = urljoin(self.BASE_URL, self.USERS_WITH_GROUPS_ENDPOINT)
        headers = {"Authorization": f"Bearer {valid_token}"}

        response = requests.get(url, headers=headers)

        assert response.status_code == 200
        assert "groups" in response.json()[0]  # Проверяем наличие ожидаемого поля в ответе

    def test_access_with_invalid_token(self):
        """Тест доступа с невалидным токеном"""
        url = urljoin(self.BASE_URL, self.USERS_WITH_GROUPS_ENDPOINT)
        headers = {"Authorization": "Bearer invalid_token_here"}

        response = requests.get(url, headers=headers)

        assert response.status_code == 401
        assert "error" in response.json()
        assert response.json()["error"] == "Authorization token required"

    def test_access_without_token(self):
        """Тест доступа без токена"""
        url = urljoin(self.BASE_URL, self.USERS_WITH_GROUPS_ENDPOINT)

        response = requests.get(url)

        assert response.status_code == 401
        assert "error" in response.json()
        assert response.json()["error"] == "Authorization token required"
