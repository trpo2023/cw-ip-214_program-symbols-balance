from src.modules.balance_checker import BalanceChecker

import pytest


@pytest.fixture
def balance_checker():
    return BalanceChecker()


def test_balanced_brackets(balance_checker):
    input_str = "{[()]}"
    result = balance_checker.check_partial(input_str)
    assert not result.error


def test_unmatched_closing_bracket(balance_checker):
    input_str = "{[()]}}"
    result = balance_checker.check_partial(input_str)
    assert result.error == "Unmatched closing bracket"
    assert result.bracket_index == 6


def test_mismatched_closing_bracket(balance_checker):
    input_str = "{[(])}"
    result = balance_checker.check_partial(input_str)
    assert result.error == "Mismatched closing bracket"
    assert result.bracket_index == 3


def test_unmatched_opening_bracket(balance_checker):
    input_str = "{[()]"
    result = balance_checker.check_partial(input_str)
    assert result.error == "Unmatched opening bracket"
    assert result.bracket_index == 0


def test_no_errors(balance_checker):
    input_str = "#include \"stdio.h\"\n\r int a = 5;\t\t\tint b = 3;"
    result = balance_checker.check_partial(input_str)
    assert not result.error
