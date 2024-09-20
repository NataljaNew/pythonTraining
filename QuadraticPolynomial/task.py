from math import sqrt

class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def d(self):
        return self.b ** 2 - 4 * self.a * self.c

    @property
    def x1(self):
        if self.d < 0:
            return None
        else:
            return (-self.b - sqrt(self.d)) / (2 * self.a)

    @property
    def x2(self):
        if self.d < 0:
            return None
        else:
            return (-self.b + sqrt(self.d)) / (2 * self.a)

    @property
    def view(self):
        return f'{self.a}x^2 + {self.b}x + {self.c}'.replace('+ -', '- ')

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, values):
        self.a, self.b, self.c = values

polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.x1)
print(polynom.x2)
print(polynom.view)
print(polynom.coefficients)
polynom.coefficients = (1,1,1)
print(polynom.coefficients)
print(polynom.view)