# Часть 3: Фронтенд-тестирование (Демо-сайт)

## Задача:
 Протестируйте форму регистрации на демо-сайте [SauceDemo](https://www.saucedemo.com/).
 
#### 3. Автотесты на Python:
   
  - Напишите 2 теста через pytest + requests:
    * Успешное создание поста.
    * Успешное изменение поста.
    * Успешное удаление поста.



## SauceDemo UI Automation Test Project
#### This project provides automated UI tests for the SauceDemo website using Python, Selenium, and Pytest with Page Object Model pattern.

### Project Structure
```
sauce-demo-tests/
├── pages/                  # Page Object classes
│   ├── login_page.py
│   └── inventory_page.py
├── tests/                  # Test cases
│   ├── test_login.py
│   └── test_logout.py
├── conftest.py             # Pytest fixtures
├── requirements.txt        # Dependencies
└── README.md
```

### Prerequisites
* Python 3.8+
* Chrome browser
* ChromeDriver (automatically installed by webdriver-manager)

### Installation
1. Clone the repository:

```bash

git clone https://github.com/istrybuk/Test-task/Patres.git
```
2. Install dependencies:

```python

pip install -r requirements.txt
```

### Running Tests
1. Run all tests
```python
pytest tests/ -v
```
2. Run specific test file

```python
pytest tests/test_login.py -v
```

3. Run tests in parallel (using pytest-xdist)
```python
pytest tests/ -n auto  # Uses all available CPU cores
```
