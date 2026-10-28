import pytest

from src.processing import count_operations_by_categories
from src.processing import filter_by_state
from src.processing import sort_by_date


def test_sort_by_date():
    assert sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    ) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state():
    assert filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    ) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sample_data():
    """Возвращает тестовый набор данных для проверки подсчета категорий."""
    return [
        {"description": "Перевод с карты на карту"},
        {"description": "Открытие вклада"},
        {"description": "Оплата мобильной связи"},
        {"description": "перевод организации"},
        {"description": "Перевод между своими счетами"},
        {"description": "Оплата ЖКХ"},
        {"description": "Открытие накопительного счета"},
    ]


def test_count_categories_found(sample_data):
    """Проверяет корректный подсчет для всех заданных категорий."""
    categories = ["Перевод", "Открытие", "Оплата"]
    result = count_operations_by_categories(sample_data, categories)
    assert result == {"Перевод": 3, "Открытие": 2, "Оплата": 2}


def test_count_categories_partial(sample_data):
    """Проверяет, что категории с нулевым вхождением не попадают в результат."""
    categories = ["Перевод", "Кредит"]
    result = count_operations_by_categories(sample_data, categories)
    assert result == {"Перевод": 3}


def test_count_categories_empty(sample_data):
    """Проверяет поведение функции при пустом списке категорий."""
    result = count_operations_by_categories(sample_data, [])
    assert result == {}


def test_count_categories_no_match(sample_data):
    """Проверяет поведение, если ни одна категория не найдена в описаниях."""
    categories = ["Ипотека", "Налоги"]
    result = count_operations_by_categories(sample_data, categories)
    assert result == {}


def test_count_categories_case_insensitive(sample_data):
    """Проверяет, что поиск категорий регистронезависим."""
    categories = ["перевод", "оТкРыТиЕ"]
    result = count_operations_by_categories(sample_data, categories)
    # Функция возвращает ключи в том виде, в котором они пришли в аргументе
    assert result == {"перевод": 3, "оТкРыТиЕ": 2}
