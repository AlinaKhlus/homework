import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Извлекает данные из вложенного объекта 'operationAmount'.
    Если валюта RUB, возвращает исходную сумму.
    Если валюта USD или EUR, запрашивает курс через API и возвращает сконвертированную сумму.

    :param transaction: Словарь с данными транзакции.
    :return: Сумма транзакции в рублях.
    :raises ValueError: Если структура транзакции невалидна, сумма не число или валюта не поддерживается.
    :raises RuntimeError: Если не найден API-ключ или произошла ошибка запроса к API.
    """
    if not transaction or "operationAmount" not in transaction:
        raise ValueError("Invalid transaction structure: missing 'operationAmount'")

    op_amount = transaction["operationAmount"]
    if not isinstance(op_amount, dict):
        raise ValueError("Invalid operationAmount structure: not a dict")

    amount_str = op_amount.get("amount")
    currency_info = op_amount.get("currency")

    if not isinstance(amount_str, str) or not isinstance(currency_info, dict):
        raise ValueError("Invalid operationAmount structure: missing 'amount' or 'currency'")

    try:
        amount = float(amount_str)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid amount format: {amount_str}")

    currency_code = currency_info.get("code")
    if not isinstance(currency_code, str):
        raise ValueError("Invalid currency structure: missing 'code'")

    currency = currency_code.upper()

    if currency == "RUB":
        return amount

    if currency not in ["USD", "EUR"]:
        raise ValueError(f"Unsupported currency: {currency}")

    # Читаем ключ здесь, чтобы тесты могли подменить env через monkeypatch после импорта модуля
    api_key = os.getenv("EXCHANGERATE_API_KEY")
    if not api_key:
        raise RuntimeError("EXCHANGERATE_API_KEY is not set in environment variables")

    params = {"base": currency, "symbols": "RUB"}
    headers = {"apikey": api_key}

    try:
        response = requests.get(BASE_URL, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        rate = data["rates"]["RUB"]
        return round(amount * rate, 2)
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch exchange rate: {e}")
    except (KeyError, TypeError) as e:
        raise RuntimeError(f"Invalid response structure from API: {e}")
