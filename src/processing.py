from typing import List, Dict, Any

def filter_by_state(data:List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    # Функция фильтрации операций по статусу операций
    new_list_keys = []
    for items in data:
        if items.get("state") == state:
            new_list_keys.append(items)
    return new_list_keys


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    # Функция сортировки операций по датам
    new_list_dates = []
    for items in data:
        if items.get("date"):
            new_list_dates.append(items)
    sort_by_date = sorted(new_list_dates, key=lambda x: x["date"], reverse=reverse)
    return sort_by_date


# Проверка работы функций
print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
