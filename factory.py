from shapes.point import Point
from shapes.segment import Segment
from shapes.circle import Circle
from shapes.square import Square

class ShapeFactory:

    @staticmethod
    def create(parts):

        shape_type = parts[1]

        if shape_type == "point":
            x = float(parts[2])
            y = float(parts[3])
            return Point(x, y)
        
        elif shape_type == "segment":
            x1 = float(parts[2])
            y1 = float(parts[3])
            x2 = float(parts[4])
            y2 = float(parts[5])
            return Segment(x1, y1, x2, y2)
        
        elif shape_type == "circle":
            x = float(parts[2])
            y = float(parts[3])
            r = float(parts[4])
            return Circle(x, y, r)
        
        elif shape_type == "square":
            x = float(parts[2])
            y = float(parts[3])
            size = float(parts[4])
            return Square(x, y, size)
        
        else:
            raise ValueError("Unknown shape type")