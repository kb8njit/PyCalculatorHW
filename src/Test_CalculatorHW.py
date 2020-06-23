import unittest
import math
from CalculatorHW import Calculator
from CSV_Reader import CSVReader

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        self.assertEqual(self.calculator.add(2.2, 2.2), 4.4)
        self.assertEqual(self.calculator.result, 4.4)
        test_data = CSVReader('/src/CSV_files/Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        test_data.clear()


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

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(8.8), float(math.sqrt(8.8)))
        self.assertEqual(self.calculator.result, float(math.sqrt(8.8)))

if __name__ == '__main__':
    unittest.main()
