

class Man:
    def __init__(self):
        self.name = "Man"
    def __str__(self):
        return self.name

class Super(Man):
    def __init__(self):
        self.description = "Super"
        super().__init__()
    def __str__(self):
        return self.name + " " + self.description

class Bat(Super,Man):
    def __init__(self):
        self.type = "Bat"
        Super.__init__(self)
        Man.__init__(self)
    def __str__(self):
        return self.type + "" + self.name + " " + self.description


m = Man()
# print(m)


s = Super()
# print(s)

b = Bat()
# print(b)


# once again

class Ball:
    def __init__(self):
        pass

    def setName(self,name):
        self.name = name

    def __str__(self):
        return self.name

b = Ball()
b.setName("Ball")
print(b)
class BasketBall(Ball):
    def __init__(self):
        pass

bb = BasketBall()
bb.setName("BB")
print(bb)