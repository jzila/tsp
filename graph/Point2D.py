__author__ = 'jzila'
from graph.Vector2D import Vector2D

class Point2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        You can add a Vector to a Point, but not the other way around
        :param other: Vector2D
        :return: Point2D
        """
        if type(other) != Vector2D:
            raise TypeError("unsupported operand type(s) for +: '" + str(type(self)) + "' and '" + str(type(other)) + "'")

        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        You can subtract a Point from a Point to get a Vector, or you can subtract a Vector from a Point to get a Point
        :param other:
        :return:
        """
        if type(other) not in (Vector2D, Point2D):
            raise TypeError("unsupported operand type(s) for -: '" + str(type(self)) + "' and '" + str(type(other)) + "'")

        if type(other) == Vector2D:
            return Point2D(self.x - other.x, self.y - other.y)
        else:
            return Vector2D(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if type(other) != Point2D:
            raise TypeError("unsupported operand type(s) for ==: '" + str(type(self)) + "' and '" + str(type(other)) + "'")

        return self.x == other.x and self.y == other.y
