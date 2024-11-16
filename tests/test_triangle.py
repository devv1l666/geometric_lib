import unittest
from triangle import area, perimeter


class MyTestCase(unittest.TestCase):
    def test_triangle_perimeter_true(self):
        a = 5
        b = 3
        c = 3
        expected = a + b + c
        real = perimeter(a, b, c)
        self.assertEqual(expected, real)

    def test_triangle_area_true(self):
        a = 5
        b = 3
        c = 3
        s = (a + b + c) / 2
        expected = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        real = area(a, b, c)
        self.assertEqual(expected, real)

    def test_triangle_area_false(self):
        a = -1
        b = 0
        c = 1
        with self.assertRaises(ValueError):
            area(a, b, c)

    def test_triangle_perimeter_false(self):
        a = -1
        b = 0
        c = 1
        with self.assertRaises(ValueError):
            perimeter(a, b, c)


if __name__ == '__main__':
    unittest.main()
