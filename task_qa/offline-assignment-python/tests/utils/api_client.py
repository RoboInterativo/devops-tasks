import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import re

class APIClient:
    def __init__(self):
        self.base_url = "http://localhost:3000"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0',
            'Accept': 'text/html,application/xhtml+xml',
        })

    def _get_authenticity_token(self, html_content):
        """Extract CSRF token from HTML"""
        soup = BeautifulSoup(html_content, 'html.parser')
        token = soup.find('input', {'name': 'authenticity_token'})
        return token['content'] if token else None

    def login(self, username, password):
        """Authenticate using form submission"""
        # First get login page to extract CSRF token
        login_page = self.session.get(f"{self.base_url}/login")
        token = self._get_authenticity_token(login_page.text)

        if not token:
            raise Exception("CSRF token not found")

        # Prepare form data
        form_data = {
            'utf8': '✓',
            'authenticity_token': token,
            'user_login': username,
            'user_password': password,
            'commit': 'Login'
        }

        # Submit login form
        response = self.session.post(
            f"{self.base_url}/login",
            data=form_data,
            allow_redirects=False
        )

        # Check for successful login (302 redirect)
        if response.status_code != 302:
            raise Exception(f"Login failed with status {response.status_code}")

        # Verify we're actually logged in
        projects_page = self.session.get(f"{self.base_url}/projects")
        if "Logout" not in projects_page.text:
            raise Exception("Login verification failed")

    def create_project(self, name, description=""):
        """Create new project via form submission"""
        # Get projects page to extract CSRF token
        projects_page = self.session.get(f"{self.base_url}/projects")
        token = self._get_authenticity_token(projects_page.text)

        if not token:
            raise Exception("CSRF token not found")

        # Prepare form data
        form_data = {
            'utf8': '✓',
            'authenticity_token': token,
            'project[name]': name,
            'project[description]': description,
            'commit': 'Add Project'
        }

        # Submit project form
        response = self.session.post(
            f"{self.base_url}/projects",
            data=form_data,
            allow_redirects=False
        )

        # Check for successful creation (302 redirect)
        if response.status_code != 302:
            raise Exception(f"Project creation failed with status {response.status_code}")

        return True

    def get_projects(self):
        """Get list of projects"""
        response = self.session.get(f"{self.base_url}/projects")
        soup = BeautifulSoup(response.text, 'html.parser')

        projects = []
        project_elements = soup.select('#list-active-projects .project_description a')

        for project in project_elements:
            projects.append({
                'name': project.text.strip(),
                'url': project['href']
            })

        return projects

    def delete_project(self, project_url):
        """Delete project"""
        # Get delete confirmation page
        delete_page = self.session.get(f"{self.base_url}{project_url}")
        token = self._get_authenticity_token(delete_page.text)

        if not token:
            raise Exception("CSRF token not found")

        # Extract project ID from URL
        project_id = re.search(r'/projects/(\d+)', project_url).group(1)

        # Prepare form data
        form_data = {
            'utf8': '✓',
            'authenticity_token': token,
            '_method': 'delete',
            'commit': 'Delete'
        }

        # Submit delete form
        response = self.session.post(
            f"{self.base_url}/projects/{project_id}",
            data=form_data,
            allow_redirects=False
        )

        return response.status_code == 302
