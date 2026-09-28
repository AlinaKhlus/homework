def get_mask_card_number(card_number: str) -> str:
    """Функция скрывающая часть номера карты"""
    card_string = str(card_number)
    if len(card_string) < 16:
        return "Ошибка"
    else:
        part1 = card_string[:4]
        part2 = card_string[4:6]
        part3 = card_string[-4:]
        return f"{part1} {part2}** **** {part3}"


def get_mask_account(account_number: str) -> str:
    """Функция скрывающая часть номера счета"""
    account_string = str(account_number)
    if len(account_string) < 4:
        return "Ошибка"
    else:
        return f"** {account_string[-4:]}"
