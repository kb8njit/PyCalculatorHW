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




if __name__ == '__main__':
    unittest.main()
