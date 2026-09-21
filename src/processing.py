def filter_by_state(state):
    new_list_key = []
    for items in state:
        if items.get("state") == "EXECUTED":
            new_list_key.append(items)
    return new_list_key

def sort_by_date(date):
    new_list_date = []
    for items in date:
        if items.get("date"):
            new_list_date.append(items)
    data_sorted = sorted(new_list_date, key=lambda x: x["date"], reverse=True)
    return data_sorted

print(filter_by_state(
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
print(sort_by_date(
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))