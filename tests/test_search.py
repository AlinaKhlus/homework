import pytest

from src.search import search_transactions_by_description


@pytest.fixture
def sample_data():
    return [
        {"id": 1, "description": "Перевод с карты на карту", "state": "EXECUTED"},
        {"id": 2, "description": "Открытие вклада", "state": "EXECUTED"},
        {"id": 3, "description": "Оплата мобильной связи", "state": "PENDING"},
        {"id": 4, "description": "перевод организации", "state": "EXECUTED"},
        {"id": 5, "description": "Перевод между своими счетами", "state": "EXECUTED"},
    ]


def test_search_found(sample_data):
    result = search_transactions_by_description(sample_data, "перевод")
    assert len(result) == 3
    assert all("перевод" in t["description"].lower() for t in result)


def test_search_case_insensitive(sample_data):
    result = search_transactions_by_description(sample_data, "ВКЛАДА")
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_search_not_found(sample_data):
    result = search_transactions_by_description(sample_data, "ипотека")
    assert result == []


def test_search_empty_string(sample_data):
    result = search_transactions_by_description(sample_data, "")
    assert result == sample_data
