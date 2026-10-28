import re
from typing import Any
from typing import Dict
from typing import List


def search_transactions_by_description(data: List[Dict[str, Any]], search_str: str) -> List[Dict[str, Any]]:
    """
    Ищет транзакции, в описании которых встречается заданное слово целиком (без учета регистра).

    :param data: Список словарей с транзакциями.
    :param search_str: Слово для поиска в поле 'description'.
    :return: Список словарей, подходящих под условие поиска.
    """
    if not search_str:
        return data

    # \b обозначает границу слова. Это исключит нахождение "порт" внутри "транспорт".
    # re.IGNORECASE делает поиск регистронезависимым.
    pattern = re.compile(rf"\b{re.escape(search_str)}\b", re.IGNORECASE)

    return [item for item in data if item.get("description") and pattern.search(item["description"])]
