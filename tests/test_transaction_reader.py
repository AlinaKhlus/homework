from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

from src.transaction_reader import read_financial_operations_from_csv
from src.transaction_reader import read_financial_operations_from_excel


@pytest.fixture
def sample_data():
    """Пример структуры данных финансовой операции."""
    return [
        {"date": "2023-10-25", "amount": "-100", "category": "food"},
        {"date": "2023-10-27", "amount": "+500", "category": "salary"},
    ]


@patch("pandas.read_csv")
def test_read_csv(mock_read_csv, sample_data):
    """
    Проверяет функцию считывания CSV через мок.
    """
    mock_df = MagicMock()
    mock_df.to_dict.return_value = sample_data
    mock_read_csv.return_value = mock_df

    result = read_financial_operations_from_csv("/fake/path.csv")

    assert result == sample_data
    mock_read_csv.assert_called_once_with("/fake/path.csv", dtype=str)


@patch("pandas.read_excel")
def test_read_excel(mock_read_excel, sample_data):
    """
    Проверяет функцию считывания Excel через мок.
    """
    mock_df = MagicMock()
    mock_df.to_dict.return_value = sample_data
    mock_read_excel.return_value = mock_df

    result = read_financial_operations_from_excel("/fake/excel.xlsx")

    assert result == sample_data
    mock_read_excel.assert_called_once_with("/fake/excel.xlsx", engine="openpyxl", dtype=str)
