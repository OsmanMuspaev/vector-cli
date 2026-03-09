from .shape import Shape


class Square(Shape):

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def info(self):
        return f"Square ({self.x},{self.y}) size={self.size}"