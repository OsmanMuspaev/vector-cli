from shapes.point import Point
from shapes.segment import Segment
from shapes.circle import Circle
from shapes.square import Square

class ShapeFactory:

    @staticmethod
    def create(parts):

        shape_type = parts[1]

        if shape_type == "point":
            if len(parts) != 4:
                raise ValueError("Point needs 2 arguments: x y")
            x = float(parts[2])
            y = float(parts[3])
            return Point(x, y)
        
        elif shape_type == "segment":
            if len(parts) != 6:
                raise ValueError("Segment needs 4 arguments: x1 y1 x2 y2")
            x1 = float(parts[2])
            y1 = float(parts[3])
            x2 = float(parts[4])
            y2 = float(parts[5])
            return Segment(x1, y1, x2, y2)
        
        elif shape_type == "circle":
            if len(parts) != 5:
                raise ValueError("Circle needs 3 arguments: x y r")
            x = float(parts[2])
            y = float(parts[3])
            r = float(parts[4])
            return Circle(x, y, r)
        
        elif shape_type == "square":
            if len(parts) != 5:
                raise ValueError("Square needs 3 arguments: x y size")
            x = float(parts[2])
            y = float(parts[3])
            size = float(parts[4])
            return Square(x, y, size)
        
        else:
            raise ValueError("Unknown shape type")