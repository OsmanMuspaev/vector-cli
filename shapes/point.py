from .shape import Shape

class Point(Shape):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def info(self):
        return f"Point ({self.x}, {self.y})"
    
    def update(self, params):
        if len(params) != 2:
            raise ValueError("Point needs 2 arguments: x y")
        self.x = float(params[0])
        self.y = float(params[1])