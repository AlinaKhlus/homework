import pytest
from src.decorators import log


def test_log_to_console_success(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(5, 10)
    captured = capsys.readouterr()

    assert result == 15
    assert captured.out.strip() == "add ok"


def test_log_to_console_error(capsys):
    @log()
    def divide(a, b):
        return a / b

    result = divide(1, 0)
    captured = capsys.readouterr()

    assert result is None
    # Проверяем, что сообщение содержит имя функции, тип ошибки и входные данные
    assert "divide error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out


def test_log_to_file_success(tmp_path):
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def greet(name):
        return f"Hello, {name}"

    result = greet("World")

    # Проверяем, что файл создался и в нем есть нужная строка
    assert log_file.exists()
    content = log_file.read_text().strip()
    assert content == "greet ok"
    assert result == "Hello, World"


def test_log_to_file_error(tmp_path):
    log_file = tmp_path / "errors.log"

    @log(filename=str(log_file))
    def get_item(lst, index):
        return lst[index]

    result = get_item([1, 2], 5)

    assert result is None
    assert log_file.exists()
    content = log_file.read_text().strip()
    assert "get_item error: IndexError" in content
    assert "Inputs: ([1, 2], 5), {}" in content
