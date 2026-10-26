import json
import os

from src.utils import read_json_file


def test_read_valid_json_with_empty_objects(temp_json_file: str):
    """
    Проверяет чтение валидного файла с пустым объектом внутри.
    """
    result = read_json_file(temp_json_file)
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 2

    # Обязательно удаляем файл после теста
    if os.path.exists(temp_json_file):
        os.remove(temp_json_file)


def test_read_json_with_missing_operation_amount(temp_json_file: str):
    """
    Проверяет чтение файла, где у части объектов нет operationAmount.
    """
    result = read_json_file(temp_json_file)
    assert len(result) == 2
    if os.path.exists(temp_json_file):
        os.remove(temp_json_file)


# Тесты на обработку ошибок (создаем файлы вручную)


def test_read_empty_file():
    file_name = "empty_test.json"
    open(file_name, "w").close()  # Создаем пустой файл

    try:
        result = read_json_file(file_name)
        assert result == []
    finally:
        if os.path.exists(file_name):
            os.remove(file_name)


def test_read_not_a_list():
    file_name = "dict_test.json"
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump({"id": 1}, f)

    try:
        result = read_json_file(file_name)
        assert result == []
    finally:
        if os.path.exists(file_name):
            os.remove(file_name)


def test_read_invalid_json():
    file_name = "broken_test.json"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("{ invalid json")

    try:
        result = read_json_file(file_name)
        assert result == []
    finally:
        if os.path.exists(file_name):
            os.remove(file_name)


def test_read_non_existent_file():
    assert read_json_file("definitely_not_exist_123.json") == []
