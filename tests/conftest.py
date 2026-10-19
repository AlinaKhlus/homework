import json
from typing import Any, Dict

import pytest


# Фикстуры для проверки карты в модуле masks.py
@pytest.fixture
def card_number():
    return "1234 56** **** 3456"


# Фикстура для проверки счета в модуле masks.py
@pytest.fixture
def account_number():
    return "** 4305"


# Фикстура для проверки  модуле widget.py test_mask_account_card_errors
@pytest.fixture
def card_mask():
    return "Ошибка"


# Фикстура для модуля widget.py функция проверки даты
@pytest.fixture
def transformation_date():
    return "11.03.2024"


# Фикстура с данными для теста generators.py
@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


# Фикстура для модуля utils.py и external_api


@pytest.fixture
def valid_rub_transaction() -> Dict[str, Any]:
    """Возвращает валидную транзакцию в рублях."""
    return {"id": 1, "operationAmount": {"amount": "500.50", "currency": {"code": "RUB"}}}


@pytest.fixture
def valid_usd_transaction() -> Dict[str, Any]:
    """Возвращает валидную транзакцию в долларах."""
    return {"id": 2, "operationAmount": {"amount": "10.5", "currency": {"code": "USD"}}}


@pytest.fixture
def valid_eur_transaction() -> Dict[str, Any]:
    """Возвращает валидную транзакцию в евро."""
    return {"id": 3, "operationAmount": {"amount": "5.5", "currency": {"code": "EUR"}}}


@pytest.fixture
def invalid_transaction_structure() -> Dict[str, Any]:
    """Возвращает невалидную транзакцию (пустой объект)."""
    return {}


@pytest.fixture
def temp_json_file() -> str:
    """
    Создает временный файл в текущей директории.
    Имя файла фиксированное, удаление происходит вручную в тесте.
    """
    file_name = "temp_test.json"
    data = [
        {"id": 1, "operationAmount": {"amount": "100", "currency": {"code": "RUB"}}},
        {},
        {"id": 2, "operationAmount": {"amount": "200", "currency": {"code": "USD"}}},
    ]

    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f)

    return file_name
