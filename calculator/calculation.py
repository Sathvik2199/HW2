class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation  

    def get_result(self):
        return self.operation(self.a, self.b)

    def perform(self):
        return self.get_result()

    def __repr__(self):
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"

    @classmethod
    def create(cls, a, b, operation):
        return cls(a, b, operation)
