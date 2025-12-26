class Calculator:
    def __init__(self, a, b, operation):
        self.a = float(a)
        self.b = float(b)
        self.op = operation.lower()

    def calculate(self):
        if self.op == "+":
            return self.a + self.b
        elif self.op == "-":
            return self.a - self.b
        elif self.op == "*":
            return self.a * self.b
        elif self.op == "/":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Cannot divide by zero"
        else:
            return "Invalid operation"
if __name__== "__main__":
    a = input("Enter first number (a): ")
    b = input("Enter second number (b): ")
    op = input("Enter operation (+,-,*,/): ")

    calc = Calculator(a, b, op)
    print("Result:", calc.calculate())