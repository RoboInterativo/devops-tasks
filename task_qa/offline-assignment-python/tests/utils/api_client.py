# utils/api_client.py
import httpx
import json

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.client = httpx.Client()

    def _get_url(self, path):
        return f"{self.base_url}/{path.lstrip('/')}"

    def post(self, path, payload, headers=None):
        url = self._get_url(path)
        response = self.client.post(url, json=payload, headers=headers)
        response.raise_for_status() # Raise an exception for bad status codes
        return response

    def get(self, path, params=None, headers=None):
        url = self._get_url(path)
        response = self.client.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response

    def put(self, path, payload, headers=None):
        url = self._get_url(path)
        response = self.client.put(url, json=payload, headers=headers)
        response.raise_for_status()
        return response

    def delete(self, path, headers=None):
        url = self._get_url(path)
        response = self.client.delete(url, headers=headers)
        response.raise_for_status()
        return response

    def close(self):
        self.client.close()

# Example of how to use it
if __name__ == "__main__":
    client = APIClient("http://localhost:8000") # Assuming getontracks runs on 8000
    try:
        # Example: Create a project
        new_project_data = {"name": "Example Project", "description": "A sample project."}
        create_response = client.post("/projects", new_project_data)
        print("Created Project:", create_response.json())

        # Example: Get all projects
        get_all_response = client.get("/projects")
        print("All Projects:", get_all_response.json())

    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()