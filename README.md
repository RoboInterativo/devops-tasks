# Исследует API
## Исследуем login_page
Для защиты формы испольхуется token
И если мы хотим отправим форму автоматически нам его надо извлечь.
```python
# Получаем HTML страницы
from bs4 import BeautifulSoup
import requests

# Получаем HTML страницы
response = requests.get('http://localhost:3000/login')
soup = BeautifulSoup(response.text, 'html.parser')

# Извлекаем токен
token_input = soup.find('input', {'name': 'authenticity_token'}).attrs
# token_input.get('value')
# if token_input:
authenticity_token = token_input.get('value')
```
