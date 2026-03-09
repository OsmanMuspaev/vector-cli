from .shape import Shape

class Segment(Shape):

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def info(self):
        return f"Segment ({self.x1}, {self.y1}) -> ({self.x2}, {self.y2})"
    
    def update(self, params):
            if len(params) != 4:
                raise ValueError("Segment needs 4 arguments: x1 y1 x2 y2")
            x1 = float(params[0])
            y1 = float(params[1])
            x2 = float(params[2])
            y2 = float(params[3])