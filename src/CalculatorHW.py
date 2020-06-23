import math


def add(x, y):
    return float(x + y)


def subtract(x, y):
    return float(x - y)


def multiply(x, y):
    return float(x * y)


def divide(x, y):
    return round(float(x / y), 9)


def square(x):
    return round(float(x * x), 9)


def sqrt(x):
    return float(math.sqrt(x))


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, x, y):
        self.result = add(x, y)
        return self.result

    def subtract(self, x, y):
        self.result = subtract(x, y)
        return self.result

    def multiply(self, x, y):
        self.result = multiply(x, y)
        return self.result

    def divide(self, x, y):
        self.result = divide(x, y)
        return self.result

    def square(self, x):
        self.result = square(x)
        return self.result

    def sqrt(self, x):
        self.result = sqrt(x)
        return self.result