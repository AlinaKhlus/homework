from unittest.mock import patch

import pytest

from src.external_api import convert_to_rub


@patch("src.external_api.requests.get")
def test_convert_usd_new_structure(mock_get, valid_usd_transaction, monkeypatch):
    monkeypatch.setenv("EXCHANGERATE_API_KEY", "test_key")
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"rates": {"RUB": 91.0}}

    result = convert_to_rub(valid_usd_transaction)

    mock_get.assert_called_once()
    assert result == 955.5  # 10.5 * 91.0


def test_convert_rub_new_structure(valid_rub_transaction):
    assert convert_to_rub(valid_rub_transaction) == 500.50


@patch("src.external_api.requests.get")
def test_convert_eur_new_structure(mock_get, valid_eur_transaction, monkeypatch):
    monkeypatch.setenv("EXCHANGERATE_API_KEY", "test_key")
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"rates": {"RUB": 100.0}}

    result = convert_to_rub(valid_eur_transaction)

    mock_get.assert_called_once()
    assert result == 550.0


def test_convert_invalid_transaction_structure(invalid_transaction_structure):
    with pytest.raises(ValueError, match="Invalid transaction structure"):
        convert_to_rub(invalid_transaction_structure)


def test_missing_api_key(monkeypatch):
    """Проверяет ошибку, если переменная окружения не установлена."""
    # Убеждаемся, что переменной точно нет
    monkeypatch.delenv("EXCHANGERATE_API_KEY", raising=False)

    with pytest.raises(RuntimeError, match="EXCHANGERATE_API_KEY is not set"):
        convert_to_rub({"operationAmount": {"amount": "10", "currency": {"code": "USD"}}})


def test_unsupported_currency():
    """Проверяет ошибку при передаче GBP или другой валюты."""
    with pytest.raises(ValueError, match="Unsupported currency"):
        convert_to_rub({"operationAmount": {"amount": "10", "currency": {"code": "GBP"}}})


# --- Тесты на валидацию структуры словаря ---


def test_invalid_transaction_structure():
    with pytest.raises(ValueError, match="Invalid transaction structure"):
        convert_to_rub({})  # Пустой словарь


def test_invalid_operation_amount_not_dict():
    with pytest.raises(ValueError, match="Invalid operationAmount structure"):
        convert_to_rub({"operationAmount": "string_instead_of_dict"})


def test_invalid_amount_not_string():
    with pytest.raises(ValueError, match="Invalid amount format"):
        convert_to_rub({"operationAmount": {"amount": 123, "currency": {"code": "RUB"}}})  # int вместо str


def test_invalid_currency_not_dict():
    with pytest.raises(ValueError, match="Invalid currency structure"):
        convert_to_rub({"operationAmount": {"amount": "10", "currency": "string_instead_of_dict"}})


@patch("src.external_api.requests.get")
def test_api_invalid_response_structure(mock_get, monkeypatch):
    """Проверяет, что будет, если API вернет JSON без нужных ключей."""
    monkeypatch.setenv("EXCHANGERATE_API_KEY", "test_key")
    mock_get.return_value.status_code = 200
    # Возвращаем JSON, в котором нет 'rates' -> 'RUB'
    mock_get.return_value.json.return_value = {"something": "else"}

    with pytest.raises(RuntimeError, match="Invalid response structure"):
        convert_to_rub({"operationAmount": {"amount": "10", "currency": {"code": "USD"}}})
