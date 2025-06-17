import pytest
from datetime import datetime

class TestProjectsAPI:
    """API tests for Projects functionality."""

    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        self.client = api_client
        # Проверяем, что клиент аутентифицирован
        # Можно сделать тестовый запрос, например, получить список проектов
        try:
            self.client.list_projects()
        except Exception as e:
            pytest.fail(f"API client is not properly authenticated: {str(e)}")
