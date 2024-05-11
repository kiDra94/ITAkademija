import unittest
class Calculator:
    def add(self,a,b):
        return a + b

class TestCalculator(unittest.TestCase):
    def test_add(self):
        p1 = 2
        p2 = 3
        exp_result = 6
        instance = Calculator()
        result = instance.add(p1,p2)
        self.assertEqual(result,exp_result)
 

unittest.main()

