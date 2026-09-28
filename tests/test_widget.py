from src.widget import mask_account_card, get_date

def test_mask_account_card():
    assert mask_account_card("Maestro 1596837868705199")
    assert mask_account_card("Счет 64686473678894779589")
    assert mask_account_card("Visa Classic 6831982476737658")
    assert mask_account_card("Visa Platinum 8990922113665229")
    assert mask_account_card("Visa Gold 59994142284263535") == "Ошибка"

def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407")