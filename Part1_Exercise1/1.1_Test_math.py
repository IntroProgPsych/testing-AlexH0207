
import unittest
from mathexercise import add

    # TODO:
    # - Write tests for:
    #   * adding two positive numbers
    #   * adding two negative numbers
    #   * adding a positive and a negative number
    # - Use assertEqual to check the results.
    # - Use clear method names, e.g. test_add_positive_numbers, etc.

    # write your tests here:
   
class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1,2),3)
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1,-2),-3)
    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1,2),1)
    pass

if __name__ == "__main__":
    unittest.main()
