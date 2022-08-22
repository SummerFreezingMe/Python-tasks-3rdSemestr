import math


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s,%s)" % (self.x, self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def square_triangle(self, second, third):
        p = (self.distance(second) + self.distance(third) + second.distance(third)) / 2
        return math.sqrt(p * (p - self.distance(second)) * (p - self.distance(third)) * (p - second.distance(third)))
