import unittest
from graph.algorithms import hull_from_points, tsp_from_points
from graph.structs import Point, GraphError, Edge


class HullTest(unittest.TestCase):
    def test_two_points(self):
        points = [
            Point(1, 1),
            Point(2, 2),
        ]
        try:
            hull_from_points(points)
            self.assertTrue(False)
        except GraphError:
            self.assertTrue(True)

    def test_triangle(self):
        points = [
            Point(1, 1),
            Point(2, 2),
            Point(3, 1),
        ]
        edges = set(hull_from_points(points))
        expected_edges = {
            Edge(Point(1, 1), Point(2, 2)),
            Edge(Point(2, 2), Point(3, 1)),
            Edge(Point(3, 1), Point(1, 1)),
        }
        self.assertEqual(expected_edges, edges)

    def test_square(self):
        points = [
            Point(1, 1),
            Point(1, 2),
            Point(2, 2),
            Point(2, 1),
        ]
        edges = set(hull_from_points(points))
        expected_edges = {
            Edge(Point(1, 1), Point(1, 2)),
            Edge(Point(1, 2), Point(2, 2)),
            Edge(Point(2, 2), Point(2, 1)),
            Edge(Point(2, 1), Point(1, 1)),
        }
        self.assertEqual(expected_edges, edges)

    def test_square_with_more_points(self):
        points = [
            Point(1.1, 1.5),
            Point(1, 1),
            Point(1.7, 1.3),
            Point(1, 2),
            Point(1.4, 1.99),
            Point(2, 2),
            Point(1.8, 1.01),
            Point(2, 1),
            Point(1.6, 1.6),
        ]
        edges = set(hull_from_points(points))
        expected_edges = {
            Edge(Point(1, 1), Point(1, 2)),
            Edge(Point(1, 2), Point(2, 2)),
            Edge(Point(2, 2), Point(2, 1)),
            Edge(Point(2, 1), Point(1, 1)),
        }
        self.assertEqual(expected_edges, edges)


class TSPTest(unittest.TestCase):
    def test_square(self):
        points = [
            Point(1, 1),
            Point(1, 2),
            Point(2, 2),
            Point(2, 1),
        ]
        edges = set(tsp_from_points(points))
        self.assertEqual(4, len(edges))
        expected_edges = {
            Edge(Point(1, 1), Point(1, 2)),
            Edge(Point(1, 2), Point(2, 2)),
            Edge(Point(2, 2), Point(2, 1)),
            Edge(Point(2, 1), Point(1, 1)),
        }
        self.assertEqual(expected_edges, edges)

    def test_square_with_more_points(self):
        points = [
            Point(1.1, 1.5),
            Point(1.9, 1.5),
            Point(1.5, 1.9),
            Point(1.5, 1.1),
            Point(1, 1),
            Point(1, 2),
            Point(2, 2),
            Point(2, 1),
        ]
        edges = set(tsp_from_points(points))
        self.assertEqual(8, len(edges))
        expected_edges = {
            Edge(Point(1, 1), Point(1.1, 1.5)),
            Edge(Point(1.1, 1.5), Point(1, 2)),
            Edge(Point(1, 2), Point(1.5, 1.9)),
            Edge(Point(1.5, 1.9), Point(2, 2)),
            Edge(Point(2, 2), Point(1.9, 1.5)),
            Edge(Point(1.9, 1.5), Point(2, 1)),
            Edge(Point(2, 1), Point(1.5, 1.1)),
            Edge(Point(1.5, 1.1), Point(1, 1)),
        }
        self.assertEqual(expected_edges, edges)


if __name__ == '__main__':
    unittest.main()
