import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(self)

    def __str__(self):
        return "(" + str(self.x) + ":" + str(self.y) + ")"

    @property
    def X(self):
        return self.x

    @X.setter
    def X(self,number):
        self.x = number

class Line:
    def __init__(self,pointOne,pointTwo):
        self.pointOne = pointOne
        self.pointTwo = pointTwo

    def distance(self):
         xd = self.pointOne.x - self.pointTwo.x
         yd = self.pointOne.y = self.pointTwo.y

class Polygon:
    def __init__(self, *points):
        self.sides = []
        for point in points:
            self.sides.append(point)
    def __del__ (self):
        print('This Polygon is being destroyed')

    def __str__(self):
        return str(self.sides.__len__())

class Circle(Point):
    def __init__(self,point,radius):
        self._radius = radius
        super().__init__(self,point.x,point.y)

    def center(self):
        return super()


p = Point(1,2)
p2 = Point(2,3)
p3 = Point(3,4)

ply = Polygon(p,p2,p3)
print(ply)
ply = None


a = [1,2,3]
a.__len__()


c = Circle(p, 8)

center = c.center()

print(center)