import requests
import xmltodict
from typing import Dict, Any
import os
from dotenv import load_dotenv

load_dotenv()

class APIClient:
    def __init__(self):
        self.base_url = os.getenv('BASE_URL', 'http://localhost:3000')
        self.session = requests.Session()
        # Для работы с формами установим заголовок по умолчанию
        self.session.headers.update({
            'Content-Type': 'application/x-www-form-urlencoded'
        })

    def _convert_to_xml(self, data: Dict[str, Any]) -> str:
        """Convert dictionary to XML string."""
        return xmltodict.unparse({'request': data}, pretty=True)

    def _convert_from_xml(self, xml_str: str) -> Dict[str, Any]:
        """Convert XML response to dictionary."""
        return xmltodict.parse(xml_str)

    def login(self, username: str, password: str) -> None:
        """Authenticate user using form data."""
        login_url = f"{self.base_url}/login"
        # Формируем данные для формы в формате application/x-www-form-urlencoded
        form_data = {
            'user_login': username,
            'user_password': password,
            'commit': 'Login'  # Часто требуется кнопка submit
        }
        response = self.session.post(login_url, data=form_data)

        # Проверяем успешность аутентификации
        if response.status_code != 200:
            raise Exception(f"Login failed with status {response.status_code}")

        # Дополнительная проверка для Tracks - можно искать определенный текст в ответе
        if "Invalid username or password" in response.text:
            raise Exception("Invalid credentials provided")

    # Остальные методы остаются без изменений
    def create_project(self, project_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new project."""
        url = f"{self.base_url}/projects"
        # Для XML-запросов временно меняем заголовок
        self.session.headers.update({'Content-Type': 'application/xml'})
        xml_data = self._convert_to_xml(project_data)
        response = self.session.post(url, data=xml_data)
        # Возвращаем заголовок для форм
        self.session.headers.update({
            'Content-Type': 'application/x-www-form-urlencoded'
        })
        response.raise_for_status()
        return self._convert_from_xml(response.text)

    # ... остальные методы класса ...
