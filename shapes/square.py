from .shape import Shape


class Square(Shape):

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def info(self):
        return f"Square ({self.x},{self.y}) size={self.size}"
    
    def update(self, params):
        if len(params) != 3:
            raise ValueError("Square needs 3 arguments: x y size")
        x = float(params[0])
        y = float(params[1])
        size = float(params[2])