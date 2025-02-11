from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),  # Addition test
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),  # Subtraction test
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),  # Multiplication test
    (Decimal('10'), Decimal('2'), divide, Decimal('5')),  # Division test
    (Decimal('10.5'), Decimal('0.5'), add, Decimal('11.0')),  # Addition with decimals
    (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')),  # Subtraction with decimals
    (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),  # Multiplication with decimals
    (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),  # Division with decimals
])
def test_calculation_operations(a, b, operation, expected):
    """
    Test calculation operations with various scenarios.
    """
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_calculation_repr():
    """
    Test the string representation (__repr__) of the Calculation class.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert repr(calc) == expected_repr, "The __repr__ method output does not match the expected string."

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
