from calculator.operations import add, multiply, subtract, divide

def test_addition():
    assert add(2,2) == 4

def test_subtraction():
    assert subtract(2,2) == 0

def test_multiplication():
    assert multiply(2,2) == 4

def test_division():
    assert divide(2,2) == 1