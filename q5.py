import turtle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def draw(self):
        turtle.up()
        turtle.goto(self.x, self.y)
        turtle.dot()
    def add(self, another_point):
        self.x = self.x + another_point.x
        print(self.x)
        self.y = self.y + another_point.y
        print(self.y)
    def scale(self, constant):
        self.x = self.x*constant
        self.y = self.y*constant
    def sheer(self, multx, multy):
        self.x = self.x*multx
        self.y = self.y*multy
    def shift(self, constantx=0, constanty=0):
        self.x = self.x + constantx
        self.y = self.y + constanty


point1 = Point(0,0)
point2 = Point(100,0)
point3 = Point(100,100)
point4 = Point(0,100)

point3.draw()
point3.scale(1.5)
point3.draw()


point3.sheer(2, -2.5)
point3.draw()


point3.shift(-100, 300)
point3.draw()

turtle.exitonclick()