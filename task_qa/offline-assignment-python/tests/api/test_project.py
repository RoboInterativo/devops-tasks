import pytest
from datetime import datetime

class TestProjectsAPI:
    """API tests for Projects functionality."""

    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        self.client = api_client
        try:
            self.client.list_projects()
        except Exception as e:
            pytest.fail(f"API client is not properly authenticated: {str(e)}")

    def test_create_project(self):
        """Test project creation (FR-004, FR-005, FR-006, FR-007)."""
        project_name = f"Test Project {datetime.now().strftime('%Y%m%d%H%M%S')}"
        project_data = {
            'project': {
                'name': project_name,
                'description': 'Test description'
            }
        }

        response = self.client.create_project(project_data)
        assert 'project' in response
        assert response['project']['name'] == project_name

    def test_create_project_with_empty_name(self):
        """Test project creation with empty name (FR-005)."""
        project_data = {
            'project': {
                'name': '',
                'description': 'Test description'
            }
        }

        with pytest.raises(Exception):
            self.client.create_project(project_data)
