import unittest
from CalculatorHW import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        self.assertEqual(self.calculator.add(2.2, 2.2), 4.4)
        self.assertEqual(self.calculator.result, 4.4)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(4.4, 2.2), 2.2)
        self.assertEqual(self.calculator.result, 2.2)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2.1, 2.1), 4.41)
        self.assertEqual(self.calculator.result, 4.41)

    def test_division(self):
        self.assertEqual(self.calculator.divide(6.0, 2.0), 3.0)
        self.assertEqual(self.calculator.result, 3.0)

    def test_square(self):
        self.assertEqual(self.calculator.square(2.2), 4.84)
        self.assertEqual(self.calculator.result, 4.84)



if __name__ == '__main__':
    unittest.main()
