
from ..CoordinateSystem import CoordinateSystem

class GObject(CoordinateSystem):
    def __init__(self, orgn, dims, pos):
        CoordinateSystem.__init__(self, orgn, dims)
        print("Generating Shape")
        print("\tOrigin is:", orgn)
        print("\tDimensions are:", dims)
        self.points = []
        self.oldpoints = []
        self.position = pos

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
        self.oldpoints = self.points.copy()

    def erase(self, cube = None):
        """
        erase will remove the current representation of the object and paint
        a new one.
        """
        for point in self.oldpoints:
            self.setPixel(point, "Off")

        if cube is not None:
            self.map(cube)

    def add(self, cube = None):
        self.erase(cube = cube)
        for point in self.points:
            self.setPixel(point, "On")
        if cube is not None:
            self.map(cube)

    def map_pt(self, point, cube):
        n_pt = [point[0], point[1], point[2]]
        for i in range(3):
            b_pt[0] += self.position[0]
        if point in self.points:
            cube.setPixel(n_pt, "On")
        else:
            cube.setPixel(n_pt, "Off")

    def map(self, cube):
        self.iterate(self.map_pt, cube)

    def draw(self, cube):
        self.add(cube = cube)
        print(self.points)
        cube.sendStream()

    def kill(self, seq):
        pass
