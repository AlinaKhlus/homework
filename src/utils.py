import json
import logging
import os
from typing import Any
from typing import Dict
from typing import Final
from typing import List

from src.logging_config import setup_logger

LOG_FILE_UTILS: Final[str] = "logs/utils.log"
logger: Final[logging.Logger] = setup_logger("utils", LOG_FILE_UTILS)


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список валидных словарей с данными о транзакциях.

    Функция обрабатывает специфическую структуру данных:
    - Поле 'amount' приходит строкой и конвертируется в float (ответственность вызывающего кода).
    - Пустые объекты ({}) и невалидные элементы пропускаются.
    - Если файл не найден, пуст или содержит не список, возвращается пустой список.

    :param file_path: Путь к JSON-файлу.
    :return: Список словарей с транзакциями.
    """
    if not os.path.exists(file_path):
        logger.warning(f"Файл не найден: {file_path}. Возвращается пустой список.")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if not content:
                logger.info(f"Файл пуст: {file_path}. Возвращается пустой список.")
                return []

            data = json.loads(content)
            if not isinstance(data, list):
                logger.error(f"Ожидался список в файле {file_path}, но получен тип {type(data)}.")
                return []

            valid_items = [item for item in data if isinstance(item, dict) and item]
            logger.info(f"Файл {file_path} успешно прочитан. Найдено валидных записей: {len(valid_items)}.")
            return valid_items
    except (json.JSONDecodeError, OSError) as e:
        logger.error(f"Ошибка чтения или парсинга файла {file_path}: {e}", exc_info=True)
        return []
