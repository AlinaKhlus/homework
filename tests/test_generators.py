import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions


# тесты для функции filter_by_currency
def test_filter_by_currency_usd_found(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 3


#  тесты для функции transaction_descriptions
def test_transaction_descriptions_order(sample_transactions):
    result = list(transaction_descriptions(sample_transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert result == expected


# тесты для фцнкции card_number_generator
@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (10, 11, ["0000 0000 0000 0010", "0000 0000 0000 0011"]),
        (9999, 10000, ["0000 0000 0000 9999", "0000 0000 0001 0000"]),
    ],
)
def test_card_number_generator_range(start, end, expected):
    result = list(card_number_generator(start, end))
    assert result == expected


def test_card_number_generator_format():
    result = next(card_number_generator(1, 1))
    parts = result.split(" ")
    assert len(parts) == 4
    assert all(len(part) == 4 for part in parts)


def test_card_number_generator_start_greater_than_end():
    result = list(card_number_generator(10, 5))
    assert result == []
