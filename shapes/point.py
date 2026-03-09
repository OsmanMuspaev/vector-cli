from .shape import Shape

class Point(Shape):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def info(self):
        return f"Point ({self.x}, {self.y})"