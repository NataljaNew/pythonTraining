class Color:

    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return  self._hexcode

    @hexcode.setter
    def hexcode(self, value):
        self.r, self.g, self.b = int(value[:2],16), int(value[2:4],16), int(value[4:],16)
        self._hexcode = value

color = Color('0000FF')

print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

color1 = Color('0000FF')

color1.hexcode = 'A782E3'
print(color1.hexcode)
print(color1.r)
print(color1.g)
print(color1.b)
