import sys
from app.commands import Command

class MenuCommand(Command):
    """
    A command to print a menu of available operations.
    """
    def execute(self):
        print('Menu')  # No need for an f-string here