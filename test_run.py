import logic
import pytest
from unittest.mock import Mock
import math
import tkinter as tk


@pytest.mark.parametrize("test_input,expected", [('+', '+'), ('-', '-'), ('*', '*'), ('/', '/')])
def test_add_to_calculation(test_input, expected):
    calc_test = logic.Calculation(Mock())
    calc_test.add_to_calculation(test_input)
    assert calc_test.calculation == expected


@pytest.mark.parametrize("test_input,expected", [('2+2', '4')])
def test_evaluate_calculation(test_input, expected):
    calc_test = logic.Calculation('Mock()')
    calc_test.calculation = test_input
    calc_test.evaluate_calculation()
    assert calc_test.calculation == expected
