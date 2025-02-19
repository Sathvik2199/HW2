class App:
    def __init__(self):  # Corrected constructor name (_init -> _init_)
        self.command_handler = CommandHandler()

    def start(self):
        # Register commands here
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", MenuCommand())

        print("Type 'exit' to exit.")
        while True:  # REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").strip())