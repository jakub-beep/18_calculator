if __name__ == "__main__":
    import logic
    import charts
    import pytest

    def test_estimate_function():
        result = logic_2.calc_sin.estimate_function('sin')
        assert result == 0.5

# def adding(x, y):
#     return x+ y
#
# def test_adding():
#     result = adding(2, 5)
#     assert result == 6