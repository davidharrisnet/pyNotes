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

         return math.sqrt(math.pow(xd,2) + math.pow(yd,2))

p1 = Point(1,2)
p2 = Point(2,30)

l = Line(p1,p2)

print(l.distance())