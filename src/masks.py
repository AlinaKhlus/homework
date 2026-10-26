import logging
from typing import Final

from logging_config import setup_logger

# Пути к логам
LOG_FILE_MASKS: Final[str] = "logs/masks.log"
logger: Final[logging.Logger] = setup_logger("masks", LOG_FILE_MASKS)


def get_mask_card_number(card_number: str) -> str:
    """Функция скрывающая часть номера карты"""
    try:
        card_string = str(card_number).replace(" ", "").replace("-", "")
        if len(card_string) != 16:
            error_msg = "Номер карты должен содержать 16 символов"
            logger.error(f"Ошибка маскирования карты: {error_msg}. Входные данные: {card_number}")
            raise ValueError(error_msg)

        part1 = card_string[:4]
        part2 = card_string[4:6]
        part3 = card_string[-4:]
        result = f"{part1} {part2}** **** {part3}"

        logger.info(f"Карта успешно замаскирована. Вход: {card_number}, Выход: {result}")
        return result
    except Exception as e:
        logger.error(f"Необработанная ошибка в get_mask_card_number для '{card_number}': {e}", exc_info=True)
        raise


def get_mask_account(account_number: str) -> str:
    """Функция скрывающая часть номера счета"""
    try:
        account_string = str(account_number)
        if len(account_string) < 4 or not account_string.isdigit():
            error_msg = "Номер счета должен содержать не менее 4 символов"
            logger.error(f"Ошибка маскирования счета: {error_msg}. Входные данные: {account_number}")
            raise ValueError(error_msg)

        result = f"** {account_string[-4:]}"

        logger.info(f"Счет успешно замаскирован. Вход: {account_number}, Выход: {result}")
        return result
    except Exception as e:
        logger.error(f"Необработанная ошибка в get_mask_account для '{account_number}': {e}", exc_info=True)
        raise
