## Test Automation Tasks

### Practical Automation Tasks

* **Develop a comprehensive suite of automated UI and API tests for the 'Projects' functionality of the `getontracks.org` service, in accordance with the functional requirements outlined in the description.**
* Provide results as a project in a `.zip` archive.
* **Ensure** that the created tests can be run using Pytest commands and that they produce clear output.

---

### Recommended Project Structure

```
getontracks-tests/
│
├── tests/
│   ├── api/                # API tests package
│   │   ├── conftest.py     # fixtures and API client setup
│   │   └── test_projects.py# CRUD tests for Projects
│   └── ui/                 # UI tests package
│       ├── conftest.py     # fixtures and WebDriver setup
│       └── test_projects_ui.py # UI tests for Projects (Selenium)
├── utils/                  # helper modules
│   └── api_client.py       # HTTP client for API tests
├── data/                   # test data files
│   └── project_payloads.json
├── requirements.txt        # pytest, httpx, selenium, pytest-html, etc.
└── docker-compose.yml      # to start getontracks.org service
```

### 1. Setup

1. Unzip the provided archive into `getontracks-tests/`.
2. Create and activate a Python 3.11 virtual environment:
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the SUT (System Under Test):
   ```bash
   docker compose up -d
   ```

### 2. Run API Tests

```bash
pytest tests/api -v
``` 

### 3. Run UI Tests

```bash
pytest tests/ui -v
``` 

### 4. Generate Reports (optional)

- Console output (detailed):
  ```bash
  pytest -v
  ```
- HTML report:
  ```bash
  pytest --html=report.html --self-contained-html
  ```

### 5. Package and Submit

1. Develop a comprehensive suite of automated UI and API tests for the 'Projects' functionality of the `getontracks.org` service, in accordance with the functional requirements outlined in the description.
2. Zip the `getontracks-tests/` directory (exclude `venv/`).
3. Submit the `.zip` archive as the deliverable.
