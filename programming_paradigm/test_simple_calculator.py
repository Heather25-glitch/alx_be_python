import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Normal case
        self.assertEqual(self.calc.add(-1, 1), 0)  # Adding negative and positive
        self.assertEqual(self.calc.add(-2, -3), -5)  # Adding two negative numbers
        self.assertEqual(self.calc.add(0, 0), 0)  # Edge case: zero addition

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Normal case
        self.assertEqual(self.calc.subtract(3, 5), -2)  # Negative result
        self.assertEqual(self.calc.subtract(0, 0), 0)  # Edge case: zero subtraction
        self.assertEqual(self.calc.subtract(-5, -3), -2)  # Subtracting negative numbers

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(3, 4), 12)  # Normal case
        self.assertEqual(self.calc.multiply(-3, 4), -12)  # Negative times positive
        self.assertEqual(self.calc.multiply(-3, -4), 12)  # Negative times negative
        self.assertEqual(self.calc.multiply(0, 10), 0)  # Edge case: multiplication by zero

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)  # Normal case
        self.assertEqual(self.calc.divide(7, 3), 2.3333333333333335)  # Non-integer result
        self.assertEqual(self.calc.divide(-10, 2), -5)  # Negative division
        self.assertEqual(self.calc.divide(0, 5), 0)  # Edge case: zero numerator
        self.assertEqual(self.calc.divide(5, 0), None)  # Edge case: division by zero

if __name__ == "__main__":
    unittest.main()
