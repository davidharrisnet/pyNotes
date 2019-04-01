import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ":" + str(self.y) + ")"

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

    def __str__(self):
        return str(self.sides)


p = Point(1,2)
p2 = Point(2,3)
p3 = Point(3,4)

ply = Polygon(p,p2,p3)
print(ply)