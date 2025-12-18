import unittest
from divide import safe_divide


    # TODO:
    # - Write tests for:
    #   * safe_divide(10, 2) -> 5.0
    #   * safe_divide(0.5, 0.1) (use assertAlmostEqual)
    #   * safe_divide(5, 0) raises ValueError
    # - Use assertRaises to test the exception.
    # - Use clear method names, e.g. test_division_integers, etc.
    #
    # write your tests here

class TestSafeDivide(unittest.TestCase):
    def test_division_integers(self):
        self.assertEqual(safe_divide(10, 2), 5.0)

    def test_division_float(self):
        self.assertAlmostEqual(safe_divide(0.5, 0.1), 5.0)

    def test_division_with_null(self):
        with self.assertRaises(ValueError):
            safe_divide(5, 0)


if __name__ == "__main__":
    unittest.main()
