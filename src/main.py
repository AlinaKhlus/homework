from typing import Any
from typing import Dict
from typing import List

from src.generators import filter_by_currency
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.search import search_transactions_by_description
from src.transaction_reader import read_financial_operations_from_csv
from src.transaction_reader import read_financial_operations_from_excel
from src.utils import read_json_file
from src.widget import get_date
from src.widget import mask_account_card


def print_transaction(t: Dict[str, Any]) -> None:
    """Выводит одну транзакцию в формате, указанном в задании."""
    # Форматируем дату
    date_str = get_date(t.get("date", ""))
    description = t.get("description", "")

    # Маскируем счета и карты
    account_info = mask_account_card(t.get("to", "") or t.get("from", ""))

    # Формируем строку суммы
    amount_info = t.get("operationAmount", {})
    amount = amount_info.get("amount", "")
    currency = amount_info.get("currency", {}).get("code", "")

    print(f"\n{date_str} {description}")
    print(f"{account_info}")
    print(f"Сумма: {amount} {currency}")


def ask_yes_no(question: str) -> bool:
    """Задает вопрос Да/Нет и возвращает булево значение."""
    while True:
        answer = input(f"{question} Да/Нет\n").lower()
        if answer == "да":
            return True
        if answer == "нет":
            return False
        print('Пожалуйста, ответьте "Да" или "Нет".')


def ask_choice(question: str, options: List[str]) -> str:
    """Задает вопрос с выбором из вариантов."""
    options_str = "/".join(options)
    while True:
        answer = input(f"{question} {options_str}\n").lower()
        if answer in options:
            return answer
        print(f'Вариант "{answer}" недоступен.')


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input()
    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        path = input("Введите путь к файлу: ")
        data = read_json_file(path)
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        path = input("Введите путь к файлу: ")
        data = read_financial_operations_from_csv(path)
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        path = input("Введите путь к файлу: ")
        data = read_financial_operations_from_excel(path)
    else:
        print("Неверный выбор. Попробуйте снова.")
        return

    if not data:
        print("Не удалось загрузить данные или файл пуст.")
        return

    valid_states = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        state_input = input(
            "Введите статус, по которому необходимо выполнить фильтрацию."
            "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        )
        state_normalized = state_input.upper()
        if state_normalized in valid_states:
            data = filter_by_state(data, state_normalized)
            print(f'Операции отфильтрованы по статусу "{state_normalized}"')
            break
        else:
            print(f'Статус операции "{state_input}" недоступен.')

    if not data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    if ask_yes_no("Отсортировать операции по дате?"):
        order = ask_choice("Отсортировать по возрастанию или по убыванию?", ["по возрастанию", "по убыванию"])
        reverse = not (order == "по возрастанию")
        data = sort_by_date(data, reverse=reverse)

    if ask_yes_no("Выводить только рублевые транзакции?"):
        data = list(filter_by_currency(data, "RUB"))

    if ask_yes_no("Отфильтровать список транзакций по определенному слову в описании?"):
        word = input("Введите слово для поиска: ")
        data = search_transactions_by_description(data, word)

    if not data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("\nРаспечатываю итоговый список транзакций...")
    print(f"\nВсего банковских операций в выборке: {len(data)}\n")

    for t in data:
        print_transaction(t)
        if __name__ == "__main__":
            main()
