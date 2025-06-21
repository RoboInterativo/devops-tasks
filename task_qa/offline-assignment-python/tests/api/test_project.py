import pytest
from datetime import datetime

class TestProjectsAPI:
    """API tests for Projects functionality."""

    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        self.client = api_client

    def test_login_success(self):
        """Test successful authentication"""
        # Verify we can access projects page
        projects = self.client.get_projects()
        assert isinstance(projects, list)

    # def test_create_project(self):
    #     """Test project creation (FR-004, FR-005, FR-006, FR-007)"""
    #     project_name = f"Test Project {datetime.now().strftime('%Y%m%d%H%M%S')}"
    #
    #     # Create project
    #     assert self.client.create_project(project_name)
    #
    #     # Verify project appears in list
    #     projects = self.client.get_projects()
    #     assert any(p['name'] == project_name for p in projects)
    #
    # def test_create_project_with_empty_name(self):
    #     """Test project creation with empty name (FR-005)"""
    #     with pytest.raises(Exception):
    #         self.client.create_project("")
    #
    # def test_project_name_uniqueness(self):
    #     """Test project name uniqueness (FR-008)"""
    #     project_name = f"Unique Project {datetime.now().strftime('%Y%m%d%H%M%S')}"
    #
    #     # First creation should succeed
    #     assert self.client.create_project(project_name)
    #
    #     # Second attempt should fail
    #     with pytest.raises(Exception):
    #         self.client.create_project(project_name)
    #
    # def test_delete_project(self):
    #     """Test project deletion (FR-016, FR-017, FR-018)"""
    #     # Create project first
    #     project_name = f"Delete Test {datetime.now().strftime('%Y%m%d%H%M%S')}"
    #     assert self.client.create_project(project_name)
    #
    #     # Get project URL
    #     projects = self.client.get_projects()
    #     project = next(p for p in projects if p['name'] == project_name)
    #
    #     # Delete project
    #     assert self.client.delete_project(project['url'])
    #
    #     # Verify project is deleted
    #     projects = self.client.get_projects()
    #     assert not any(p['name'] == project_name for p in projects)
