import math


class Point(object):

    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return "(%s,%s)" % (self.X, self.Y)

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return math.sqrt(dx ** 2 + dy ** 2)

    def square_triangle(self, second, third):
        p = (self.distance(second) + self.distance(third) + second.distance(third)) / 2
        return math.sqrt(p * (p - self.distance(second)) * (p - self.distance(third)) * (p - second.distance(third)))
