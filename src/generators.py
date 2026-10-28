from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    # Функиция поочередно выдает транзакции, где валюта операции соответствует заданной
    for transaction in transactions:
        currency_info = transaction.get("operationAmount", {}).get("currency", {})
        trans_currency = currency_info.get("code")
        if trans_currency == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    # Функиция возвращает описание каждой операции по очереди.
    for transaction in transactions:
        yield transaction.get("description") or ""


def card_number_generator(start_number: int, end_number: int) -> Iterator[str]:
    # Функция генерирует номер карты в заданном диапазоне
    total_length = 16
    part_number = 4
    for number in range(start_number, end_number + 1):
        number_string = str(number).zfill(total_length)
        complete_number = []
        for i in range(0, total_length, part_number):
            complete_number.append(number_string[i : i + part_number])
        yield " ".join(complete_number)
