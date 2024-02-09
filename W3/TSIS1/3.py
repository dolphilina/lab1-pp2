class Shape():
    def area(self):
        return 0
    

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.width * self.length)


rect1 = Rectangle(2, 3)
print(rect1.length, rect1.width)
rect1.area()