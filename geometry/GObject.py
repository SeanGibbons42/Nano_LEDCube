class GObject(CoordinateSystem):
    def __init__(self, orgn, dims):
        CoordinateSystem.__init__(orgn, dims)
        self.points = []
        self.oldpoints = []

    def translate(self, new_pos):
        """
        Function translate moves the shape to a new location.
        """
        self.save()
        self.origin = new_pos
        self.add()

    def mirror(self, axis, position):
        """
        Function mirror will reflect an object across a mirror plane
        Accepts: axis - axis of the mirror plane (0 = x, 1 = y, 2 = z)
                 position - position of the mirror plane on the axis.
        """
        self.save()                  #Save previous points so they can be erased

        for point in self.point():        #map position to be reflected over axis
            point[axis] -= position

        r = transforms.rotmat(axis)

        pmatrix = np.array(self.points)
        pmatrix = np.transpose(pmatrix)
        pmatrix = np.matmul(r,pmatrix)
        pmatrix = np.transpose(pmatrix)
        self.points = pmatrix.tolist()

        for point in self.points:         #map position back, as if it was reflected
            point[axis] += position       #accross the specified plane.

        self.add()

    def rotate(self, axis, angle):
        """
        Function rotate will rotate an object around a specified axis in quarter rotations
        axis: 0 = x axis, 1 = y, 2 = z.
        """

        self.save()
        r = transforms.rotmat(angle, axis)
        pmatrix = numpy.array(self.points)

        pmatrix= np.transpose(pmatrix)
        pmatrix = np.matmul(r, pmatrix)
        pmatrix = np.transpose(pmatrix)

        self.points = pmatrix.tolist()
        self.add()


    def scale(self, sf):
        """
        Function scale will dilate an object by a scale factor.
        """
        self.save()
        #scale the object dimensions
        d = sf*np.array(self.dims())
        self.setDimensions(d.tolist())
        #scale each point
        for point in self.points:
            for dim in point:
                dim *= sf

        self.add()

    def save(self):
        self.oldpoints = self.points

    def erase(self):
        """
        erase will remove the current representation of the object and paint
        a new one.
        """
        for point in self.oldpoints():
            self.setPixel("Off")

    def add(self):
        self.erase()
        for point in self.points:
            self.setPixel("On")

    def draw(self, cube):
        self.add()
        cube.sendStream()

    def kill(self, seq):
        pass
