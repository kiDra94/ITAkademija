import unittest
from my_calculations import Calculations


class TestCalculations(unittest.TestCase):

    @classmethod # moze da bude i klasna metoda, na razliku od test3.py
    def setUpClass(cls):
        cls.calculation = Calculations(8, 2)

    def test_sum(cls):
        cls.assertEqual(cls.calculation.get_sum(), 10, 'The sum is wrong.')

    def test_diff(cls):
        cls.assertEqual(cls.calculation.get_difference(), 6, 'The difference is wrong.')

    def test_product(cls):
        cls.assertEqual(cls.calculation.get_product(), 16, 'The product is wrong.')

    def test_quotient(cls):
        cls.assertEqual(cls.calculation.get_quotient(), 4, 'The quotient is wrong.')


if __name__ == '__main__':
    unittest.main()