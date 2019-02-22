from .GObject import GObject

class Sphere(GObject):
    def __init__(self, radius, pos):
        GObject.__init__(self, [radius, radius, radius], [2*radius+1, 2*radius+1, 2*radius+1], pos)
        self.radius = radius
        self.generate()

    def generate(self):
        self.iterate(self.set_if_in_sphere)

    def set_if_in_sphere(self, pt):
        r = (pt[0]**2 + pt[1]**2 + pt[2]**2)**0.5
        print("Next point:", pt)
        if r<=self.radius:
            print("\tAdding pt")
            self.points.append(pt)

    def set_radius(self, nr):
        sf = nr/self.radius
        self.radius = nr
        self.dilate(sf)

class Rectangle(GObject):
    def __init__(self, dims, position, center = "Corner"):
        if center == "Corner":
            orgn = [0,0,0]
        elif center == "Center":
            orgn = [dims[0]/2, dims[1]/2, dims[2]/2]
        else:
            raise ValueError("Invalid Center Specifier. center can be defined as" +
                             "corner or Center. When setting the origin to center" +
                             "ensure that the rectangle dimensions are odd.")

        GObject.__init__(orgn, dims)
        self.generate()

    def generate(self):
        self.save()
        self.iterate(self.set_pixel, 1)
        self.add()

    def set_width(self, nw):
        self.setDimensions([self.dims[0], nw, self.dims[2]])
        self.generate()

    def set_length(self, nl):
        self.setDimensions(nl, self.dims[1], self.dims[2])
        self.generate()

    def set_height(self):
        self.setDimensions(self.dims[0], self.dims[1], nh)
        self.generate()

class Letter(GObject):
    def __init__(self):
        pass

class Circle(GObject):
    def __init__(self, radius, axis):
        self.radius = radius
        self.axis = axis

        d = [2*radius+1,2*radius+1, 2*radius+1]
        d[axis] = 1
        GObject.__init__([radius, radius , radius], d)

    def generate(self):
        self.iterate(self.set_if_in_radius, self.axis)

    def set_if_in_radius(self, pt, axis):
        r = 0
        for i in range(len(pt)):
            if not i == axis:
                r += pt[i]**2
        r = r**0.5

        if r <= self.radius:
            self.setPixel(pt, 1)

    def set_radius(self, nr):
        sf = nr/self.radius
        self.radius = nr
        self.dilate(sf)

class Cylinder(GObject):
    def __init__(self, radius, axis, height, center="Bottom"):
        orgn = [radius, radius, radius]
        d = [2*radius+1, 2*radius+1, 2*radius+1]

        #set the origin to the bottom or centroid of the cylinder
        if center == "Bottom":
            orgn[axis] = 0
        elif center == "Center" and not height%2 == 0:
            orgn[axis] = height-1/2
        else:
            raise ValueError("Invalid Center Specifier. center can be defined as" +
                             "Bottom or Center. When setting the origin to center" +
                             "ensure that the height is odd.")
        d[axis] = height

        GObject.__init__(orgn, d)
        self.generate()

    def generate(self, axis):
        self.iterate(self.set_if_in_shape, axis)

    def set_if_in_shape(self, pt, axis):
        center = self.getOrigin().copy()
        center[axis] = pt[axis]
        r = 0
        for i in range(3):
            r += (pt[i] - origin[i])**2
        r = r**0.5

        if r<radius:
            self.setPixel(pt, 1)


class Triangle(GObject):
    def __init__(self, base):
        pass

def Pyramid(GObject):
    def __init(self):
        pass
