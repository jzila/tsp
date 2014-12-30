from json import JSONEncoder
import math


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        You can add a Vector to a Point, but not the other way around
        :param other: Vector
        :return: Point
        """
        if type(other) != Vector:
            raise TypeError("unsupported operand type(s) for +: '" + str(type(self)) + "' and '" + str(type(other)) + "'")

        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        You can subtract a Point from a Point to get a Vector, or you can subtract a Vector from a Point to get a Point
        :param other:
        :return:
        """
        if type(other) not in (Vector, Point):
            raise TypeError("unsupported operand type(s) for -: '" + str(type(self)) + "' and '" + str(type(other)) + "'")

        if type(other) == Vector:
            return Point(self.x - other.x, self.y - other.y)
        else:
            return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if type(other) != Point:
            raise TypeError("unsupported operand type(s) for ==: '" + str(type(self)) + "' and '" + str(type(other)) + "'")

        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((Point.__name__, self.x, self.y))


class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if type(other) != Vector:
            raise TypeError("unsupported operand type(s) for +: '" + str(type(self)) + "' and '" + str(type(other)) + "'")

        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if type(other) != Vector:
            raise TypeError("unsupported operand type(s) for -: '" + str(type(self)) + "' and '" + str(type(other)) + "'")

        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if type(other) != Vector:
            raise TypeError("unsupported operand type(s) for ==: '" + str(type(self)) + "' and '" + str(type(other)) + "'")

        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((Vector.__name__, self.x, self.y))

    def mag(self):
        return (self.x**2 + self.y**2)**.5

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y)

    def cross(self, other):
        return (self.x * other.y) - (self.y * other.x)

    def angle(self, other):
        x = self.cross(other)
        cosA = min(1, max(-1, self.dot(other) / (self.mag() * other.mag())))
        angle = math.acos(cosA)
        if x < 0:
            return -angle
        else:
            return angle


class Edge(object):
    def __init__(self, p, v):
        if type(p) != Point or type(v) not in (Vector, Point):
            raise TypeError("unsupported operand type(s) for Edge(): '" + str(type(p)) + "' and '" + str(type(v)) + "'")

        self.p = p
        if type(v) == Vector:
            self.v = v
        elif type(v) == Point:
            self.v = v - p

    def __hash__(self):
        return hash((Edge.__name__, self.p, self.v))

    def __eq__(self, other):
        return self.p == other.p and self.v == other.v

    def endP(self):
        return self.p + self.v

    def angle(self, other):
        if type(other) != Edge:
            raise TypeError("unsupported operand type(s) for angle() '" + str(type(self)) + "' and '" + str(type(other)) + "'")
        return self.v.angle(other.v)

    def mag(self):
        return self.v.mag()

class StructEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class GraphError(Exception):
    pass

