import pytest


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def api_url(base_url):
    return base_url+""

@pytest.fixture
def api_headers():
    return { 'Content-type': 'application/json; charset=UTF-8',  }