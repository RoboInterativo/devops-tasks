# tests/api/conftest.py
import pytest
import json
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def api_base_url():
    # Assuming getontracks.org runs on localhost:3000
    return "http://localhost:3000"

@pytest.fixture(scope="session")
def api_client(api_base_url):
    client = APIClient(api_base_url)
    yield client
    client.close()

@pytest.fixture(scope="session")
def project_payloads():
    with open("data/project_payloads.json", "r") as f:
        return json.load(f)

@pytest.fixture
def create_test_project(api_client, project_payloads):
    """Fixture to create a project before a test and clean it up afterwards."""
    new_project_data = project_payloads["new_project"]
    response = api_client.post("/projects", new_project_data)
    project_id = response.json()["id"] # Assuming the API returns the ID
    yield project_id
    # Teardown: Delete the created project
    try:
        api_client.delete(f"/projects/{project_id}")
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404: # Already deleted or not found
            pass
        else:
            raise