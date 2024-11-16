import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_circle_perimeter_true(self):
        r = 5
        expected = 2 * math.pi * r
        real = perimeter(r)
        self.assertEqual(expected, real)

    def test_circle_area_true(self):
        r = 5
        expected = math.pi * r * r
        real = area(r)
        self.assertEqual(expected, real)

    def test_circle_area_false(self):
        r = -1
        with self.assertRaises(ValueError):
            area(r)

    def test_circle_perimeter_false(self):
        r = -1
        with self.assertRaises(ValueError):
            perimeter(r)


if __name__ == '__main__':
    unittest.main()
