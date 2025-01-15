import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        # set up the SimpleCalculator instance before each test
        self.calc = SimpleCalculator()
        
    def test_add(self):
        #test the add method
        self.assertEqual(self.calc.add(2, 3),5 )
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(1, -1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
    
    def test_subtract(self):
        #test the subtract method
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(2, 0), 2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -2), 1)
        self.assertAlmostEqual(self.calc.subtract(10000.0, 9999.9), 0.1)
        
    def test_multiply(self):
        #test the multiply method
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertEqual(self.calc.multiply(0, 2), 0)
        self.assertEqual(self.calc.multiply(1, -1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        
    def test_divide(self):
        #test the divide method
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(-4, -2), 2)
        self.assertEqual(self.calc.divide(-4, 2), -2)
        self.assertEqual(self.calc.divide(4, 0), None)
        self.assertAlmostEqual(self.calc.divide(4.0, 2.0), 2.0)