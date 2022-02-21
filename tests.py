import logic_2
import charts
import pytest

def test_estimate_function():
    result = logic_2.calc_sin.estimate_function('sin')
    assert result == 0.5


