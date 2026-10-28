from typing import Dict
from typing import List

import pandas as pd


def read_financial_operations_from_csv(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла.

    Аргументы:
        file_path (str): Путь к файлу CSV.

    Возвращает:
        List[Dict]: Список словарей с транзакциями. Каждый словарь — одна операция.
    """
    try:
        df = pd.read_csv(file_path, dtype=str)

        return df.to_dict(orient="records")
    except Exception as e:
        raise RuntimeError(f"Ошибка чтения файла CSV: {e}")


def read_financial_operations_from_excel(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла (XLSX).

    Аргументы:
        file_path (str): Путь к файлу XLSX.

    Возвращает:
        List[Dict]: Список словарей с транзакциями. Каждый словарь — одна операция.
    """
    try:
        df = pd.read_excel(file_path, engine="openpyxl", dtype=str)

        return df.to_dict(orient="records")
    except Exception as e:
        raise RuntimeError(f"Ошибка чтения файла Excel: {e}")
