import pytest
from contextlib import nullcontext as does_not_raise
from pytest_1.src.app import Calculator

@pytest.mark.parametrize('a, b, res, expected', [
    (20, 10, {'plus': 30, 'minus': 10, 'divide': 2, 'multiply': 200}, does_not_raise()),
    (5, 'a', None, pytest.raises(TypeError)),
])

def test_app(a, b, res, expected):
    calc = Calculator()
    with expected:
        assert calc.plus(a, b) == res['plus']
        assert calc.minus(a, b) == res['minus']
        assert calc.divide(a, b) == res['divide']
        assert calc.multiply(a, b) == res['multiply']

