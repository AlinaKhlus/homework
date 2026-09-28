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
