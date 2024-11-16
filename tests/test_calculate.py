import unittest
import math
from calculate import calc


class GeometricLibTestCase(unittest.TestCase):

    def test_calc_circle_perimeter(self):
        self.assertAlmostEqual(calc('circle', 'perimeter', [5]), 2 * math.pi * 5)

    def test_calc_circle_area(self):
        self.assertAlmostEqual(calc('circle', 'area', [5]), math.pi * 5**2)

    def test_calc_square_perimeter(self):
        self.assertEqual(calc('square', 'perimeter', [5]), 20)

    def test_calc_square_area(self):
        self.assertEqual(calc('square', 'area', [5]), 25)

    def test_calc_invalid_figure(self):
        with self.assertRaises(AssertionError):
            calc('triangle', 'perimeter', [5])

    def test_calc_invalid_function(self):
        with self.assertRaises(AssertionError):
            calc('circle', 'volume', [5])

    def test_calc_wrong_number_of_arguments(self):
        with self.assertRaises(TypeError):
            calc('circle', 'perimeter', [5, 5])


if __name__ == '__main__':
    unittest.main()
