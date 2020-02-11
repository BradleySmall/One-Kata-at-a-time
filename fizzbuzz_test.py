"""Unit tests."""
import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizbuzz_1_return_1(self):
        self.assertEqual(fizzbuzz.fizzbuzz(1), 1)

    def test_fizbuzz_2_return_2(self):
        self.assertEqual(fizzbuzz.fizzbuzz(2), 2)
        
    def test_fizbuzz_3_return_fizz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(3), "Fizz")

    def test_fizbuzz_4_return_4(self):
        self.assertEqual(fizzbuzz.fizzbuzz(4), 4)

    def test_fizbuzz_5_return_buzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(5), "Buzz")
        
    def test_fizbuzz_6_return_fizz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(6), "Fizz")

    def test_fizbuzz_7_return_flugal(self):
        self.assertEqual(fizzbuzz.fizzbuzz(7), "Flugal")

    def test_fizbuzz_10_return_buzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(10), "Buzz")

    def test_fizbuzz_15_return_fizzbuzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(15), "FizzBuzz")
        
    def test_fizbuzz_45_return_fizzbuzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(45), "FizzBuzz")

    def test_fizzbuzz_fizzbuzzflugal(self):
        self.assertEqual(fizzbuzz.fizzbuzz(7*3*5), "FizzBuzzFlugal")

    def test_fizzbuzz_21_returnfizzflugal(self):
        self.assertEqual(fizzbuzz.fizzbuzz(21), "FizzFlugal")
    def test_fizzbuzz_35_returnbuzzflugal(self):
        self.assertEqual(fizzbuzz.fizzbuzz(35), "BuzzFlugal")

        
if __name__=='__main__':
    unittest.main(exit=False, verbosity=2)
