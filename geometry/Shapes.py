class Sphere(GObject):
    def __init__(self, radius, pos):
        GObject.__init__(pos)
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
    def __init__(self):
        pass

    def generate(self):
        self.iterate(self.set_pixel, 1)

    def set_width(self):
        pass

    def set_length(self):
        pass

    def set_height(self):
        pass

    def center_origin(self):
        pass

    def zero_origin(self):
        pass
