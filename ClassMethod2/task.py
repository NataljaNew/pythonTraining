class Rectangle:
    def __init__(self, length: int|float, width: int|float):
        self.length = length
        self.width = width

    @classmethod
    def square(cls, side):
        return cls(side,side)


rectangle = Rectangle(4, 5)

print(rectangle.length)
print(rectangle.width)
rectangle = rectangle.square(5)
print(rectangle.length)
print(rectangle.width)