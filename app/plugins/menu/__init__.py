import sys
import app.commands import Command

class MenuCommand(Command):
    def execute(self):
        print('Menu')