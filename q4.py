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

point1 = Point(0,0)
point2 = Point(100,0)
point3 = Point(100,100)
point4 = Point(0,100)

print(point1)
print(point2)
print(point3)
print(point4)

point1.draw()
point2.draw()
point3.draw()
point4.draw()

turtle.exitonclick()