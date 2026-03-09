from .shape import Shape


class Circle(Shape):

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def info(self):
        return f"Circle center({self.x},{self.y}) r={self.r}"