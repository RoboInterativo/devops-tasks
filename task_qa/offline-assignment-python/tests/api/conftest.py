import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    """Fixture that provides an authenticated API client."""
    client = APIClient()

    # Authenticate with test credentials
    try:
        client.login(username="admin", password="password")
    except Exception as e:
        pytest.fail(f"Authentication failed: {str(e)}")

    yield client

    # Cleanup - delete any test projects
    projects = client.get_projects()
    for project in projects:
        if project['name'].startswith(("Test Project", "Unique Project", "Delete Test")):
            client.delete_project(project['url'])
