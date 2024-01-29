import unittest

from utils.my_calculations import Calculations
import sys
sys.path.append('../tests')
class MyTestCase(unittest.TestCase):

    def setup(self)-> None:
        self.calculation = Calculations(10, 0)

    def test_sum(self):
        pass

    @unittest.skip
    def test_quotient(self):
        self.assertEqual(self.calculation.get_quotient(), 4, "the quotient is wrong")

    def test_zero_quotient(self):
        self.assertRaises(
            [ZeroDivisionError],
            self.calculation.get_quotient(),
            "the quotient is wrong"
        )

if __name__ == '__main__':
    unittest.main()


