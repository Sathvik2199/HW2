from decimal import Decimal

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a, b):
    if b == Decimal('0'):
        raise ValueError("Cannot divide by zero")
    return a / b


