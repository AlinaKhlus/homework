import builtins
from unittest.mock import patch

from src.main import main


def test_main_flow_json(monkeypatch, capsys):
    inputs = iter(["1", "tests/data.json", "EXECUTED", "нет", "нет", "нет"])

    monkeypatch.setattr(builtins, "input", lambda prompt="": next(inputs))

    def fake_read(path):
        return [
            {
                "id": 1,
                "description": "Тест",
                "state": "EXECUTED",
                "date": "2020-01-01T00:00:00.000000",
                "operationAmount": {"amount": "100", "currency": {"code": "RUB"}},
                "to": "Счет 1234",
            }
        ]

    # Исправленный путь для patch
    with patch("src.main.read_json_file", side_effect=fake_read):
        main()

    captured = capsys.readouterr()

    assert "Распечатываю итоговый список транзакций" in captured.out
    assert "Тест" in captured.out
    assert "Всего банковских операций в выборке: 1" in captured.out


def test_main_invalid_status(monkeypatch, capsys):
    inputs = iter(["1", "tests/data.json", "WRONG", "EXECUTED", "нет", "нет", "нет"])

    monkeypatch.setattr(builtins, "input", lambda prompt="": next(inputs))

    def fake_read(path):
        return [
            {
                "id": 1,
                "description": "Тест",
                "state": "EXECUTED",
                "date": "2020-01-01T00:00:00.000000",
                "operationAmount": {"amount": "100", "currency": {"code": "RUB"}},
                "to": "Счет 1234",
            }
        ]

    with patch("src.main.read_json_file", side_effect=fake_read):
        main()

    captured = capsys.readouterr()

    assert 'Статус операции "WRONG" недоступен.' in captured.out
    assert "Операции отфильтрованы по статусу" in captured.out
