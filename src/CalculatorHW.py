import math


def add(x, y):
    x = float(x)
    y = float(y)
    return x + y


def subtract(x, y):
    x = int(x)
    y = int(y)
    return y - x


def multiply(x, y):
    x = int(x)
    y = int(y)
    return x * y


def divide(x, y):
    x = int(x)
    y = int(y)
    return round((y / x), 9)


def square(x):
    x = int(x)
    return round((x * x), 9)


def sqrt(x):
    x = float(x)
    return round(math.sqrt(x), 9)


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