from . import Shapes

class GFactory():
    def __init__(self):
        self.shapes = []

    def create_shape(self, stype, name, *args, **kwargs):
        if stype == "Sphere":
            #Sphere accepts radius
            nshape = Shapes.Sphere(args[0], args[1])
        elif stype == "Circle":
            nshape = Shapes.Circle(args[0], args[1])
        elif stype == "Rectangle":
            nshape = Shapes.Rectangle(args[0], args[0], kwargs[0])
        elif stype == "Cylinder":
            nshape = Shapes.Cylinder(args[0], args[1], args[2], kwargs[0])
        else:
            raise ValueError("Invalid Shape Specifier. Call GFactory.get_valid_shapes()"
                             " for valid specifiers.")

        self.shapes.append(nshape)
        return nshape

    def get_shape(self, name):
        for shape in self.shapes:
            if shape.get_name() == name:
                return shape
        return None

    def remove_shape(self, name):
        for i in range(len(self.shapes)):
            if shape[i].get_name() == name:
                del shape[i]

    def get_valid_shapes(self):
        return "Circle, Sphere, Rectangle (=Rectangular Prism), Cylinder"
