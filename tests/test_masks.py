import pytest
from src.masks import get_mask_account, get_mask_card_number

def test_get_mask_card_number():
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"
    assert get_mask_card_number("1234 5678 9012 3456") == "1234 56** **** 3456"



with pytest.raises(ValueError) as exc_info:
    get_mask_card_number("94847857894789083")


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "** 4305"

with pytest.raises(ValueError) as exc_info2:
    get_mask_account("654")

