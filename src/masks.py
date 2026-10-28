def get_mask_card_number(card_number: str) -> str:
    """Функция скрывающая часть номера карты"""
    card_string = str(card_number).replace(" ", "").replace("-", "")
    if len(card_string) != 16:
        raise ValueError("Номер карты должен содержать 16 символов")
    part1 = card_string[:4]
    part2 = card_string[4:6]
    part3 = card_string[-4:]
    return f"{part1} {part2}** **** {part3}"


def get_mask_account(account_number: str) -> str:
    """Функция скрывающая часть номера счета"""
    account_string = str(account_number)
    if len(account_string) < 4 or not account_string.isdigit():
        raise ValueError("Номер счета должен содержать не менее 4 символов")
    return f"** {account_string[-4:]}"
