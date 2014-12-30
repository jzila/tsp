import math
from graph.structs import Point, Vector

import unittest


class PointTest(unittest.TestCase):
    def test_sub_points(self):
        a = Point(1, 2)
        b = Point(3, 4)

        c = b - a
        self.assertEqual(Vector(2, 2), c)

    def test_add_points(self):
        a = Point(1, 2)
        b = Point(3, 4)

        try:
            a + b
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)

    def test_add_vector_to_point(self):
        a = Point(1, 2)
        b = Vector(3, 4)

        c = a + b
        self.assertEqual(c, Point(4, 6))

    def test_sub_vector_from_point(self):
        a = Point(1, 2)
        b = Vector(3, 4)

        c = a - b
        self.assertEqual(c, Point(-2, -2))

    def test_bad_equality(self):
        a = Point(1, 2)
        b = Vector(1, 2)

        try:
            a == b
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)


class VectorTest(unittest.TestCase):
    def test_add_vectors(self):
        a = Vector(1, 2)
        b = Vector(3, 4)

        c = b + a
        self.assertEqual(Vector(4, 6), c)

    def test_add_point_to_vector(self):
        a = Vector(1, 2)
        b = Point(3, 4)

        try:
            a + b
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)

    def test_sub_point_from_vector(self):
        a = Vector(1, 2)
        b = Point(3, 4)

        try:
            a - b
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)

    def test_bad_equality(self):
        a = Vector(1, 2)
        b = Point(1, 2)

        try:
            a == b
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)

    def test_angle(self):
        a = Vector(0, 1)
        b = Vector(1, 0)
        c = Vector(-1, 0)

        angle = a.angle(b)
        self.assertAlmostEqual(angle, -math.pi/2)
        angle = b.angle(a)
        self.assertAlmostEqual(angle, math.pi/2)
        angle = b.angle(c)
        self.assertAlmostEqual(angle, math.pi)
        angle = c.angle(b)
        self.assertAlmostEqual(angle, math.pi)

if __name__ == '__main__':
    unittest.main()
