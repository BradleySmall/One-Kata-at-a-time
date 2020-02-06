import factor


"""Unit tests."""
import unittest
class TestPrimeFactorization(unittest.TestCase):

    def test_factor_zero_return_empty_list(self):
        self.assertEqual(factor.factor(0), [])

    def test_factor_one_return_empty_list(self):
        self.assertEqual(factor.factor(1), [])

    def test_factor_two_return_2_in_list(self):
        self.assertEqual(factor.factor(2), [2])

    def test_factor_three_return_3_in_list(self):
        self.assertEqual(factor.factor(3), [3])

    def test_factor_four_return_2_2_in_list(self):
        self.assertEqual(factor.factor(4), [2, 2])

    def test_factor_5_return_5_in_list(self):
        self.assertEqual(factor.factor(5), [5])

    def test_factor_6_return_2_3_in_list(self):
        self.assertEqual(factor.factor(6), [2, 3])

    def test_factor_7_return_7_in_list(self):
        self.assertEqual(factor.factor(7), [7])

    def test_factor_8_return_2_2_2_in_list(self):
        self.assertEqual(factor.factor(8), [2, 2, 2])

    def test_factor_9_return_3_3_in_list(self):
        self.assertEqual(factor.factor(9), [3, 3])

    def test_factor_big_return_correct_in_list(self):
        self.assertEqual(factor.factor(2*2*3*5*5*7*11*17*19), [2,2,3,5,5,7,11,17,19])

    def test_factor_big2_return_correct_in_list(self):
        self.assertEqual(factor.factor(5993), [13, 461])

if __name__=='__main__':
    unittest.main(exit=False, verbosity=2)
    print(factor.factor(100099705986730467308999))