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
        turtle.write(str(f"({self.x}, {self.y})"))
    
    def scale(self, constant):
    #     self.x = self.x*constant
    #     self.y = self.y*constant
        x = self.x*constant
        y = self.y*constant
        new_point = Point(x, y)
        return new_point

    # def sheer(self, multx, multy):
    #     self.x = self.x*multx
    #     self.y = self.y*multy
    # def shift(self, constantx=0, constanty=0):
    #     self.x = self.x + constantx
    #     self.y = self.y + constanty


point1 = Point(0,0)
point2 = Point(100,0)
point3 = Point(100,100)
point4 = Point(0,100)

point3.draw()
scaled_point3 = point3.scale(2)
scaled_point3.draw()
scaled_point3 = scaled_point3.scale(-2)
scaled_point3.draw()





turtle.exitonclick()