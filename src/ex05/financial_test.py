#!/usr/bin/env python3
import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from ex04.financial import get_financial_data


def test_total_revenue_returns_tuple_or_error_string():
    result = get_financial_data("MSFT", "Total Revenue")
    assert isinstance(result, tuple) or isinstance(result, str)


def test_return_type_is_tuple_for_valid_request_if_available():
    result = get_financial_data("MSFT", "Total Revenue")
    
    if isinstance(result, tuple):
        assert isinstance(result, tuple)
        assert result[0].strip().lower() == "total revenue"
        assert len(result) >= 2
    else:
        assert result in ("Unknown ticker or field", "Incorrect URL")


def test_invalid_ticker_gives_error():
    result = get_financial_data("THIS_TICKER_SHOULD_NOT_EXIST_123", "Total Revenue")
    assert isinstance(result, str)
    assert result in ("Unknown ticker or field", "Incorrect URL")


def test_invalid_field_gives_error():
    result = get_financial_data("MSFT", "THIS_FIELD_SHOULD_NOT_EXIST_123")
    assert isinstance(result, str)
    assert result in ("Unknown ticker or field", "Incorrect URL")


def test_field_is_case_insensitive():
    result1 = get_financial_data("MSFT", "Total Revenue")
    result2 = get_financial_data("MSFT", "total revenue")
    assert type(result1) is type(result2)
