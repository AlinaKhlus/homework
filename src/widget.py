from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_account_number: str) -> str:
    """Функция скрывающая часть номера карты или счета"""
    card_type, card_number = card_account_number.rsplit(" ", 1)
    if len(card_number) < 16:
        return "Ошибка"
    elif "счет" in card_type.lower():
        masks = get_mask_account(card_number)
        return f"{card_type} {masks}"
    else:
        masks = get_mask_card_number(card_number)
        return f"{card_type} {masks}"


def get_date(date_time: str) -> str:
    """Функция которая принимает дату в формате 2024-03-11T02:26:18.671407 и возращающая формат дд.мм.гггг"""
    date_split = date_time.split("T")
    year, month, date = date_split[0].split("-")
    return f"{date}.{month}.{year}"


print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))
