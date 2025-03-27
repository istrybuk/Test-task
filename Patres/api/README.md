# Часть 1: Тестирование REST API

## Задача:

 Протестируйте публичное API [JSONPlaceholder](https://jsonplaceholder.typicode.com/) (фейковый REST API для тестирования).
 #### Эндпоинты:
* GET /posts — получить список постов.
* POST /posts — создать пост.
* DELETE /posts/1 — удалить пост.

#### 3. Автотесты на Python:
* Напишите 2 теста через pytest + requests:
  * Успешное создание поста.
  * Успешное изменение поста.
  * Успешное удаление поста.

## Описание проекта для GitHub: Тестирование REST API JSONPlaceholder
#### Название проекта
REST API Testing with JSONPlaceholder (Python, pytest)

#### Описание
Этот проект содержит набор автотестов для проверки работы публичного REST API сервиса JSONPlaceholder. Тесты написаны на Python с использованием библиотек ```pytest``` и ```requests```, а также инструмента ```allure``` для создания отчетов.

#### Особенности
- Использование фикстур pytest для организации тестового кода
- Поддержка генерации отчетов Allure
- Чистая и модульная структура проекта
- Подробные проверки статус-кодов и структуры ответов

#### Технологии
- Python 3.x
- pytest (для тестового фреймворка)
- requests (для HTTP-запросов)
- allure-python-commons (для отчетов)
- JSONPlaceholder (фейковый REST API для тестирования)

### Структура проекта
```
api/
├── tests/
│   ├── api/
│   │   ├── fixtures_api.py    # Фикстуры для API тестов
│   │   └── test_api.py        # Тестовые сценарии
│   └── conftest.py            # Конфигурация pytest
├── requirements.txt           # Зависимости Python
└── README.md                  # Документация
```

### Установка и запуск

#### 1. Клонировать репозиторий:
```bash
git clone https://github.com/istrybuk/Test-task/Patres.git
```

#### 2. Установить зависимости:
```bash
pip install -r requirements.txt
```

#### 3. Запустить тесты:
```bash
pytest tests/api/test_api.py -v
```

#### 4. (Опционально) Сгенерировать отчет Allure:
```bash
pytest --alluredir=allure-results
allure serve allure-results
```
