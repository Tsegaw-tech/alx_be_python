import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Addition Tests ---
    def test_addition(self):
        """Test the add method with positive, negative, and zero values."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)

    # --- Subtraction Tests ---
    def test_subtraction(self):
        """Test the subtract method with various values."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    # --- Multiplication Tests ---
    def test_multiplication(self):
        """Test the multiply method with positive, negative, and zero values."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        self.assertEqual(self.calc.multiply(0, 10), 0)

    # --- Division Tests ---
    def test_division(self):
        """Test the divide method with normal values."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

    def test_division_by_zero(self):
        """Test that dividing by zero returns None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

# Run tests when file is executed directly
if __name__ == "__main__":
    unittest.main()
