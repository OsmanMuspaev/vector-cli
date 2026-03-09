from .shape import Shape


class Circle(Shape):

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def info(self):
        return f"Circle center({self.x},{self.y}) r={self.r}"
    
    def update(self, params):
        if len(params) != 3:
            raise ValueError("Circle needs 3 arguments: x y r")
        x = float(params[0])
        y = float(params[0])
        r = float(params[0])