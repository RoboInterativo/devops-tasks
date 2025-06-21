# utils/api_client.py
# This module provides a client to interact with the Tracks API.

import httpx
import json

class ApiClient:
    """A client for interacting with the Tracks API."""

    def __init__(self, base_url, username, password):
        """
        Initializes the API client.

        Args:
            base_url (str): The base URL of the Tracks instance.
            username (str): The username for authentication.
            password (str): The password for authentication.
        """
        self.base_url = base_url
        self.auth = (username, password)
        self.client = httpx.Client(base_url=self.base_url, auth=self.auth)
        self.token = self._get_auth_token()
        # Re-initialize client with token auth for subsequent requests
        if self.token:
             self.client = httpx.Client(
                base_url=self.base_url,
                auth=(self.username, self.token)
            )


    def _get_auth_token(self):
        """
        Retrieves an authentication token from the Tracks API.
        Note: The Tracks API uses the user's password as the token.
        This method is kept for clarity and potential future API changes.
        """
        # For Tracks, the API token is the user's password.
        # However, we can make a test request to ensure credentials are valid.
        try:
            response = self.client.get("/me.xml")
            response.raise_for_status()
            # In a real scenario with token-based auth, we would parse the token here.
            # For Tracks, we just use the password as the token.
            return self.auth[1]
        except httpx.HTTPStatusError as e:
            print(f"Authentication failed: {e}")
            return None


    def create_project(self, project_data):
        """
        Creates a new project.

        Args:
            project_data (dict): The data for the new project.

        Returns:
            httpx.Response: The response from the API.
        """
        headers = {'Content-Type': 'application/xml'}
        # Tracks API expects XML for project creation
        xml_payload = f"<project><name>{project_data['name']}</name><description>{project_data['description']}</description></project>"
        return self.client.post("/projects.xml", content=xml_payload.encode('utf-8'), headers=headers)

    def get_project(self, project_id):
        """
        Retrieves a specific project by its ID.

        Args:
            project_id (int): The ID of the project to retrieve.

        Returns:
            httpx.Response: The response from the API.
        """
        return self.client.get(f"/projects/{project_id}.xml")

    def update_project(self, project_id, project_data):
        """
        Updates an existing project.

        Args:
            project_id (int): The ID of the project to update.
            project_data (dict): The new data for the project.

        Returns:
            httpx.Response: The response from the API.
        """
        headers = {'Content-Type': 'application/xml'}
        xml_payload = f"<project><name>{project_data['name']}</name><description>{project_data['description']}</description></project>"
        return self.client.put(f"/projects/{project_id}.xml", content=xml_payload.encode('utf-8'), headers=headers)

    def delete_project(self, project_id):
        """
        Deletes a project.

        Args:
            project_id (int): The ID of the project to delete.

        Returns:
            httpx.Response: The response from the API.
        """
        return self.client.delete(f"/projects/{project_id}.xml")

    def get_all_projects(self):
        """
        Retrieves all projects.

        Returns:
            httpx.Response: The response from the API.
        """
        return self.client.get("/projects.xml")
