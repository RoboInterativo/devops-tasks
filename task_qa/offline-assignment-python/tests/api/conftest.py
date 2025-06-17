import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    """Fixture that provides an authenticated API client."""
    client = APIClient()

    # Попытка аутентификации с обработкой ошибок
    try:
        client.login(username="admin", password="1234567890")
    except Exception as e:
        pytest.fail(f"Failed to authenticate: {str(e)}")

    yield client

    # Здесь можно добавить cleanup, если нужно
    # Например, выход из системы
    # Но для Tracks это обычно не требуется
