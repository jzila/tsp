__author__ = 'john'

import unittest
from graph.Point2D import Point2D
from graph.Vector2D import Vector2D


class PointTest(unittest.TestCase):
    def test_sub_points(self):
        a = Point2D(1, 2)
        b = Point2D(3, 4)

        c = b - a
        self.assertEqual(Vector2D(2, 2), c)

    def test_add_points(self):
        a = Point2D(1, 2)
        b = Point2D(3, 4)

        try:
            a + b
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)

    def test_add_vector_to_point(self):
        a = Point2D(1, 2)
        b = Vector2D(3, 4)

        c = a + b
        self.assertEqual(c, Point2D(4, 6))

    def test_sub_vector_from_point(self):
        a = Point2D(1, 2)
        b = Vector2D(3, 4)

        c = a - b
        self.assertEqual(c, Point2D(-2, -2))

    def test_bad_equality(self):
        a = Point2D(1, 2)
        b = Vector2D(1, 2)

        try:
            a == b
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)


class VectorTest(unittest.TestCase):
    def test_add_vectors(self):
        a = Vector2D(1, 2)
        b = Vector2D(3, 4)

        c = b + a
        self.assertEqual(Vector2D(4, 6), c)

    def test_add_point_to_vector(self):
        a = Vector2D(1, 2)
        b = Point2D(3, 4)

        try:
            a + b
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)

    def test_sub_point_from_vector(self):
        a = Vector2D(1, 2)
        b = Point2D(3, 4)

        try:
            a - b
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)

    def test_bad_equality(self):
        a = Vector2D(1, 2)
        b = Point2D(1, 2)

        try:
            a == b
            self.assertTrue(False)
        except TypeError:
            self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
