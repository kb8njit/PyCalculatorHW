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
        test_data = CSVReader('/src/CSV_files/Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        test_data.clear()

    def test_subtraction(self):
        test_data = CSVReader('/src/CSV_files/Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        test_data.clear()

    def test_multiply(self):
        test_data = CSVReader('/src/CSV_files/Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))
        test_data.clear()

    def test_division(self):
        test_data = CSVReader('/src/CSV_files/Division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, round(float(row['Result']), 9))
        test_data.clear()

    def test_square(self):
        test_data = CSVReader('/src/CSV_files/Square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        test_data.clear()

    def test_sqrt(self):
        test_data = CSVReader('src/CSV_files/SquareRoot.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.sqrt(int(row['Value 1'])), round(float(row['Result']), 9))
            self.assertEqual(self.calculator.result, round(float(row['Result']), 9))
        test_data.clear()

if __name__ == '__main__':
    unittest.main()
