import json
import os
from typing import Any, Dict, List


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
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if not content:
                return []

            data = json.loads(content)
            if not isinstance(data, list):
                return []

            # Фильтрация: оставляем только непустые словари
            return [item for item in data if isinstance(item, dict) and item]
    except (json.JSONDecodeError, OSError):
        return []
