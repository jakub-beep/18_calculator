import logic
import pytest


@pytest.mark.parametrize("test_input,expected", [('+', '+'), ('-', '-'), ('*', '*'), ('/', '/')])
def test_add_to_calculation(test_input, expected):
    result = logic.calc.add_to_calculation(test_input)
    assert result == expected


def test_evaluate_calculation():
    result = logic.calc.evaluate_calculation()
    assert result == '45'


def test_clear_field():
    result = logic.calc.clear_field()
    assert result == ''


def test_estimate_function_sin():
    result_sin = logic.calc_sin.estimate_function()
    result_cos = logic.calc_cos.estimate_function()
    assert result_sin == '1.0' and result_cos == '0.0'
#
