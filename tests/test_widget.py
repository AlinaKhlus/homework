import pytest
from src.widget import mask_account_card, get_date


# Параметризация функции test_mask_card
@pytest.mark.parametrize(
    "type_of_card, numder",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Счет 64686473678894779589", "Счет ** 9589"),
        ("Счет 46438673482008746705", "Счет ** 6705"),
    ],
)
def test_mark_card(type_of_card, numder):
    assert mask_account_card(type_of_card) == numder


# Проверка функци если неправильно введена длинна номера карты или пришла пустая строка
def test_mask_account_card_errors(card_mask):
    assert mask_account_card("Visa Gold 59994142284263535") == card_mask
    assert mask_account_card(" ") == card_mask


# Проверка функции get_date
def test_get_date(transformation_date):
    assert get_date("2024-03-11T02:26:18.671407") == transformation_date


with pytest.raises(ValueError) as exc_info3:
    get_date("22.04.2021")

with pytest.raises(ValueError) as exc_info4:
    get_date("")
