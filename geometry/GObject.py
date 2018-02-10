class GObject(CoordinateSystem):
    def __init__(self, pos):
        self.origin = pos
        self.points = []
        self.oldpoints = []

    def translate(self, new_pos):
        """
        Function translate moves the shape to a new location.
        """
        self.save()
        self.origin = new_pos
        self.add()

    def mirror(self, axis, positiion):
        """
        Function mirror will reflect an object across a mirror plane
        Accepts: axis - axis of the mirror plane (0 = x, 1 = y, 2 = z)
                 position - position of the mirror plane on the axis.
        """
        self.save()

        if axis == 0:
            chg_dim = 1

        elif axis == 1:
            chg_dim = 0

        elif axis == 2:
            chg_dim = 2

        else:
            pass

        for point in self.points:
            dist = point[chg_dim] - position
            point[chg_dim] -= 2*chg_dim

        self.erase()
        self.add()

    def rotate(self, axis, angle):
        """
        Function rotate will rotate an object around a specified axis in quarter rotations
        axis: 0 = x axis, 1 = y, 2 = z.
        """
        self.save()
        r = np.array([[np.cos(angle), -np.sin(angle)],
                         [np.sin(angle), np.cos(angle)]])
        pmatrix = numpy.array(self.points)

        pmatrix2d = np.delete(pmatrix.copy(), axis, 1)
        amatrix = pmatrix[:,axis]

        pmatrix2d = np.transpose(pmatrix2d)
        pmatrix2d = np.matmul(r, pmatrix2d)
        pmatrix2d = np.transpose(pmatrix2d)

        pmatrix[:,axis] = amatrix

        self.points = pmatrix.tolist()
        self.add()

    def scale(self, sf):
        """
        Function scale will dilate an object by a scale factor.
        """
        self.save()
        #scale each point
        for point in self.points:
            #scale each dimesion by the scale factor
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
        for point in self.points:
            self.setPixel("On")

    def draw(self, cube):
        self.add()
        cube.sendStream()

    def kill(self, seq):
        pass
