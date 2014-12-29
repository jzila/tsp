__author__ = 'jzila'

class Vector2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if type(other) != Vector2D:
            raise TypeError("unsupported operand type(s) for +: '" + str(type(self)) + "' and '" + str(type(other)) + "'")

        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if type(other) != Vector2D:
            raise TypeError("unsupported operand type(s) for -: '" + str(type(self)) + "' and '" + str(type(other)) + "'")

        return Vector2D(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if type(other) != Vector2D:
            raise TypeError("unsupported operand type(s) for ==: '" + str(type(self)) + "' and '" + str(type(other)) + "'")

        return self.x == other.x and self.y == other.y
