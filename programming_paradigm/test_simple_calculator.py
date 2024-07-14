import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(4, 4), 8)
        self.assertEqual(self.calc.add(5, 2), 7)
        self.assertEqual(self.calc.add(8, 8), 16)
        self.assertEqual(self.calc.add(9, 9), 18)
        self.assertEqual(self.calc.add(10, 4), 14)
   
   # testing substraction
   
   def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2, 3), 1)
        self.assertEqual(self.calc.subtract(3, 1), 2)
        self.assertEqual(self.calc.subtract(4, 4), 0)
        self.assertEqual(self.calc.subtract(10,5 ), 5)
        self.assertEqual(self.calc.subtract(9,5 ), 4)
        self.assertEqual(self.calc.subtract(8,2 ), 6)
        self.assertEqual(self.calc.subtract(10,3 ), 7)

    # testing multiplication

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(1, 2), 2)
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(5, 6), 30)
        self.assertEqual(self.calc.multiply(6, 7), 42)
        self.assertEqual(self.calc.multiply(7, 8), 56)
    # testing division

    def test_division(self):
        self.assertEqual(self.calc.divide(2, 1), 2)
        self.assertEqual(self.calc.divide(2, 2), 1)
        self.assetEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.division(10, 2), 5)
        self.assertEqual(self.calc.division(81, 9), 9)
        self.assertEqual(self.calc.division(42, 7), 6)
        self.assertEqual(self.calc.division(56, 8), 7)

    if __name__ == "__main__":
        unittest.main()

