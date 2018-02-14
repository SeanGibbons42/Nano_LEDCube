class Sphere(GObject):
    def __init__(self, radius, pos):
        GObject.__init__([radius-1, radius-1, radius-1], [radius, radius, radius])
        self.radius = radius
        self.generate()

    def generate(self):
        self.iterate(self.set_if_in_sphere)

    def set_if_in_sphere(self, pt):
        r = ((pt[0] - self.origin[0])**2 + (pt[1] - self.origin[1])**2
            + (pt[2]-self.origin[2])**2)**0.5

        if r<=self.radius:
            self.set_pixel(pt, 1)

    def set_radius(self, nr):
        sf = nr/self.radius
        self.radius = nr
        self.dilate(sf)

class Rectangle(GObject):
    def __init__(self, dims, position):
        GObject.__init__([0,0,0], dims)
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
