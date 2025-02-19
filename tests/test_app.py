import pytest
from app.commands import CommandHandler
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand


def test_register_and_execute_multiply_command(capsys):
    handler = CommandHandler()
    multiply_command = MultiplyCommand(6, 7)

    # Register the multiply command
    handler.register_command("multiply", multiply_command)

    # Execute the multiply command
    result = handler.execute_command("multiply")

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the output is correct
    assert captured.out == "MultiplyCommand: 6 * 7 = 42\n"
    assert result == 42

def test_register_and_execute_divide_command(capsys):
    handler = CommandHandler()
    divide_command = DivideCommand(10, 2)

    # Register the divide command
    handler.register_command("divide", divide_command)

    # Execute the divide command
    result = handler.execute_command("divide")

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the output is correct
    assert captured.out == "DivideCommand: 10 / 2 = 5.0\n"
    assert result == 5.0

def test_divide_by_zero():
    handler = CommandHandler()
    divide_command = DivideCommand(10, 0)

    # Register the divide command
    handler.register_command("divide_zero", divide_command)

    # Check that dividing by zero raises the appropriate error
    with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed."):
        handler.execute_command("divide_zero")

def test_register_and_execute_add_command(capsys):
    handler = CommandHandler()
    add_command = AddCommand(2, 3)

    # Register the add command
    handler.register_command("add", add_command)

    # Execute the add command
    result = handler.execute_command("add")

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the output is correct
    assert captured.out == "AddCommand: 2 + 3 = 5\n"
    assert result == 5

def test_register_and_execute_subtract_command(capsys):
    handler = CommandHandler()
    subtract_command = SubtractCommand(5, 2)

    # Register the subtract command
    handler.register_command("subtract", subtract_command)

    # Execute the subtract command
    result = handler.execute_command("subtract")

    # Capture printed output
    captured = capsys.readouterr()

    # Assert that the output is correct
    assert captured.out == "SubtractCommand: 5 - 2 = 3\n"
    assert result == 3

def test_execute_nonexistent_command():
    handler = CommandHandler()

    # Try executing a command that doesn't exist
    result = handler.execute_command("nonexistent")

    # Assert that the result is None (no command executed)
    assert result is None