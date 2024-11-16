import unittest
from square import area, perimeter


class MyTestCase(unittest.TestCase):
    def test_square_perimeter_true(self):
        a = 5
        expected = 4 * a
        real = perimeter(a)
        self.assertEqual(expected, real)

    def test_square_area_true(self):
        a = 5
        expected = a ** 2
        real = area(a)
        self.assertEqual(expected, real)

    def test_square_area_false(self):
        a = -1
        with self.assertRaises(ValueError):
            area(a)

    def test_square_perimeter_false(self):
        a = -1
        with self.assertRaises(ValueError):
            perimeter(a)


if __name__ == '__main__':
    unittest.main()
