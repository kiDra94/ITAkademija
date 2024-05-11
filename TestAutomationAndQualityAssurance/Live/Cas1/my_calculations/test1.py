# project/test1.py

import unittest
#from code.my_calculations import Calculations
from my_calculations import Calculations


class TestCalculations(unittest.TestCase): #TestCase je roditeljska klasa

    def test_sum(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_sum(), 10, 'The sum is wrong.')


if __name__ == '__main__':
    unittest.main()
