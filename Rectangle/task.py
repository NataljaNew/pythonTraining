class Rectangle:
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def get_perimeter(self):
        return (self.width + self.length) * 2

    def get_area(self):
        return self.length*self.width

    perimeter = property(get_perimeter)
    area = property(get_area)

rectangle = Rectangle(4, 5)

rectangle.length = 2
rectangle.width = 3
print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)