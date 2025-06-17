# tests/api/test_projects.py
import pytest
import httpx

def test_create_project(api_client, project_payloads):
    """Test creating a new project."""
    new_project_data = project_payloads["new_project"]
    response = api_client.post("/projects", new_project_data)

    assert response.status_code == 200
    created_project = response.json()
    assert "id" in created_project
    assert created_project["name"] == new_project_data["name"]
    assert created_project["description"] == new_project_data["description"]

    # Clean up (optional, as create_test_project handles it for other tests)
    api_client.delete(f"/projects/{created_project['id']}")


def test_get_all_projects(api_client, create_test_project):
    """Test retrieving all projects."""
    # create_test_project ensures at least one project exists
    response = api_client.get("/projects")
    assert response.status_code == 200
    projects = response.json()
    assert isinstance(projects, list)
    assert len(projects) > 0
    assert any(p["id"] == create_test_project for p in projects) # Verify our created project is there

def test_get_single_project(api_client, create_test_project):
    """Test retrieving a single project by ID."""
    project_id = create_test_project
    response = api_client.get(f"/projects/{project_id}")
    assert response.status_code == 200
    project = response.json()
    assert project["id"] == project_id
    assert project["name"] == project_payloads["new_project"]["name"] # Assuming initial data

def test_update_project(api_client, project_payloads, create_test_project):
    """Test updating an existing project."""
    project_id = create_test_project
    updated_data = project_payloads["updated_project"]
    response = api_client.put(f"/projects/{project_id}", updated_data)
    assert response.status_code == 200
    updated_project = response.json()
    assert updated_project["id"] == project_id
    assert updated_project["name"] == updated_data["name"]
    assert updated_project["description"] == updated_data["description"]

def test_delete_project(api_client, create_test_project):
    """Test deleting a project."""
    project_id = create_test_project
    response = api_client.delete(f"/projects/{project_id}")
    assert response.status_code == 200 # Or 204 No Content, depending on API design
    # Verify it's gone
    with pytest.raises(httpx.HTTPStatusError) as excinfo:
        api_client.get(f"/projects/{project_id}")
    assert excinfo.value.response.status_code == 404 # Not Found