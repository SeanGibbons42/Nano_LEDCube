import numpy
'''
Class CoordinateSystem: Represents a 3d coordinate system. The origin can be defined at any point
      in the 3d space, and the axis max/mins are set relative to the origin and cube dimensions.
      provides functions to perform mass-manipulation of pixels.
Author: Sean Gibbons
Version: 1
'''
#TEST COMMENT!!!!!! HELLO WORLD
class CoordinateSystem(object):
    def __init__(self,orgn,dims):
        #constructor: initialize a coordinate system with an origin (list, [x,y,z])
        #and outer dimensions (list, [x size,y size,z size])

        #the origin will serve as a relative '0,0,0' point. This may be set anywhere
        self.origin = orgn
        #the dimensions are the physical dimensions of the cube. (i.e.: 8x8x8)
        self.dimensions = dims
        #the bounds serve to provide value limits for each axis. This array has 6 elements,
        #with pairs serving as the max and min values for each axis.
        #order: [X max, X min, Y max, Y min, Z max, Z min]
        self.bounds=[0, 0, 0, 0, 0, 0]

        #assign the bounds of the coordinate system relative to the origin.
        self.setBounds()

        #initialize the coordinate system array.
        self.coordArray=numpy.zeros([dims[0],dims[1],dims[2]])

    #####################################################################################
    #####################################################################################
    #                             'Setter' functions                                    #
    #####################################################################################
    #####################################################################################
    def setOrigin(self,orgn):
        #sets the pixel that will be defined as the 'origin' of the cube
        self.origin=orgn
        self.setBounds()

    def setDimensions(self,dims):
        #function set dimensions of the cube. Resets the coordinate system by calling setBounds
        self.coordArray = numpy.zeros(dims[0],dims[1],dims[2])
        self.setBounds()

    def setBounds(self):
        #function setBounds sets the numerical limits on each coordinate system axis.
        #this bounds the coordinate system to a physical system, while allowing the origin to be moved.
        #You can do stuff like relative coordinates, or center the origin an a physical cube.
        j = 0
        for i in range(0, 3):
            # axis maximum is the cube dimension minus the origin point
            self.bounds[j] = self.dimensions[i] - self.origin[i] - 1
            j += 1
            # axis minimum (bounds[j]) is the cube dimension subtracted from the axis maximum.
            self.bounds[j] = self.bounds[j - 1] - self.dimensions[i] + 1
            j += 1

    def mapToCube(self,position):
        #function mapPixel will map a pixel from the defined coordinate space to the actual cube
        cubePosition = []
        for i in range(0,3):
            cubePosition.append(position[i]+self.origin[i])
        return cubePosition

    def mapToCoordSys(self,cubePosition):
        #function mapToCoordSys: takes in an absolute point on the coordinate system and
        #maps it to the defined coordinate system.
        position = []
        for i in range(0,3):
            position.append(cubePosition[i]-self.origin[i])
        return position

    def stateParser(self,state):
        #takes in a variety of input styles that could represent states, and outputs a more
        #standard convention (1 = on, 0 = off)
        if state == 'On' or state == 'on' or state == True or state == 1:
            return 1
        elif state == 'Off' or state == 'off' or state == False or state == 0:
            return 0

    def isInBounds(self,position):
        #function isInBounds will return true if a given position is acceptable according to
        #the current grid states.

        x,y,z = position[0],position[1],position[2]
        #if any axis coordinate is out of bounds, return false. Else, return true.
        if x>self.bounds[0] or x<self.bounds[1]:
            return False
        elif y>self.bounds[2] or y<self.bounds[3]:
            return False
        elif z>self.bounds[4] or z<self.bounds[5]:
            return False
        else:
            return True
    def isIsolated(self, position):


    def togglePixel(self,position):
        #function togglePixel: changes the value of a specific pixel, indicated by a list containing
        #the x, y, and z position
        testCoord = position
        if self.getPixel(position) == 1:
            self.setPixel(position,0)
        elif self.getPixel(position) == 0:
            self.setPixel(position,1)


    def setPixel(self,position,state):
        #function setPixel will set the value of a single pixel.
        #State may be indicated as 'On'/'Off', 'on'/'off', 1/0, True/False
        #RETURNS: exit code: 0 -- state set, successful
        #                   -1 -- state not set, out of bounds

        #parse the state to a standard value (1 or 0)
        state = self.stateParser(state)

        #if the index is out of bounds, return -1.
        #if not(self.isInBounds(position)):
        #    return -1

        #else, continue on and map the coordinate position to its cube position:
        cubePos = self.mapToCube(position)

        #set the led to its indicated state
        self.coordArray[cubePos[2]][cubePos[1]][cubePos[0]] = state
        #return positive exit code, indicating successful execution


    def toggleRow(self,xyPos):
        #iteratively toggle each led in a row
        spCoord = [xyPos[0],xyPos[1],0]

        for i in range(self.bounds[3],self.bounds[4]+1):
            self.togglePixel([xyPos[0],xyPos[1],i])

    def setRow(self,xyPos,state):
        #iteratively set the value of each led in a vertical row to a specified state.
        #Inputs: xyPos - the (x,y) position of the vertical row
        #        state - the state of the LED's in specified row (on or off)?
        spCoord = [xyPos[0], xyPos[1], 0]
        spCube = self.mapToCube(spCoord)

        for i in range(0, self.dimensions[2]):
            self.setPixel([spCube[0], spCube[1], i],state)

    def setAll(self, state):
        
        for z in range(self.bounds[1],self.bounds[0]):
            for y in range(self.bounds[3],self.bounds[2]):
                for x in range(self.bounds[5],self.bounds[4]):
                    setPixel([x,y,z], state)


    def togglePlane(self,pos, axis):
        #function togglePlane will switch the value of every LED in a plane.

        #we plan to hit every point on the grid. Thus cubePos is a point on the cube, not
        #a coordinate point.
        cubePos = [self.bounds[1], self.bounds[3], self.bounds[5]]
        print("Bounds:", self.bounds)
        print("Starting Position:",cubePos)
        # iterate through the cube array.
        for z in range(self.bounds[5], self.bounds[4]+1):
            for y in range(self.bounds[3], self.bounds[2]+1):
                for x in range(self.bounds[1], self.bounds[0]+1):
                    cubePos = [x, y, z]
                    # if the current position lies in the plane, set it to the specified value
                    print(cubePos)
                    if cubePos[axis] == pos:
                        #it's important to make sure the point is mapped to the coordinate system
                        self.togglePixel(cubePos)

    def setPlane(self,pos,axis,state):
        #sets the value of an entire plane
        cubePos = [self.bounds[1], self.bounds[3], self.bounds[5]]
        # iterate through the cube array.
        for z in range(self.bounds[5], self.bounds[4] + 1):
            for y in range(self.bounds[3], self.bounds[2] + 1):
                for x in range(self.bounds[1], self.bounds[0] + 1):
                    cubePos = [x, y, z]
                    # if the current position lies in the plane, set it to the specified value
                    if cubePos[axis] == pos:
                        # it's important to make sure the point is mapped to the coordinate system
                        self.setPixel(cubePos,state)

    def invertAllPixels(self):
        #function invertAllPixels will flip each pixel in the coordinate system
        for x in range(0, self.dimensions[0]):
            for y in range(0, self.dimensions[1]):
                for z in range(0, self.dimensions[2]):
                    self.togglePixel([x,y,z])

    #####################################################################################
    #####################################################################################
    #                             'Getter' functions                                    #
    #####################################################################################
    #####################################################################################
    def getBounds(self):
        #returns the coordinate system bounds (relative to the origin)
        return self.bounds

    def getOrigin(self):
        return self.origin

    def getDimensions(self):
        #returns the length, width, and height of the coordinate system.
        return self.dimensions

    def getPixel(self,pos,map_pixel=True):
        """
        getPixel will return the value of a single LED.
        the origin must be at 0,0,0 for the correct value to
        be returned (no negatives). If the grid is already mapped
        to 0,0,0 then set map_pixel to false in order to prevent
        double mapping
        """
        if map_pixel:
            pos = self.mapToCube(pos)

        try:
            return self.coordArray[pos[2]][pos[1]][pos[0]]
        except:
            return -1

    def count_neighbors(self,pos):
        """
        Examines the six points directly next to
        the current point. Counts the number of neighboring
        LED's that are on and the number that are off.

        !!Does not count diagonal neighbors!! Use the diagonal
        version of this method to do that!

        TODO: This is a brute-force algorithm and I am not proud
        of it. If someone can find a more elegant solution,
        that'd be great.
        """
        pos = self.mapToCube(pos)
        neighbors = []
        #append the six neighboring points to a list
        neighbors.append([pos[0]+1,pos[1],pos[2]])
        neighbors.append([pos[0]-1,pos[1],pos[2]])
        neighbors.append([pos[0],pos[1]+1,pos[2]])
        neighbors.append([pos[0],pos[1]-1,pos[2]])
        neighbors.append([pos[0],pos[1],pos[2]+1])
        neighbors.append([pos[0],pos[1],pos[2]-1])
        #declare counters
        on = off = 0
        #iterate through the point list and get count the
        #number that are on.
        for led in neighbors:
            if self.getPixel(led, map_pixel=False) == 1:
                on += 1
            else:
                off += 1

        return on, off


    def count_neighbors_diagonal(self, pos):
        pos = self.mapToCube(pos)
        on = off = 0
        #Iterate through a cube around the point of interest
        for i in range(pos[2]-1,pos[2]+1):
            for j in range(pos[1]-1, pos[1]+1):
                for k in range(pos[0]-1, pos[0]+1):
                    #if the current point equals the original point, ignore
                    if [i, j, k] == pos:
                        pass
                    #if the point is on, count it as such
                elif self.getPixel([i, j, k], map=False) == 1:
                        on += 1
                    #if the point is off or is outside the cube,
                    #count it as off
                    else:
                        off += 1
        return on, off

                     ########################################
                     ###########Export functions#############
                     ########################################
    def serializeGrid(self):
        #function serialize grid will convert the numpy array to a 1d python list
        serialList = []
        pos = [0,0,0]
        #for i,j,k in self.coordArray:
        for i in range(0, self.dimensions[2]):
            for j in range(0, self.dimensions[1]):
                for k in range(0, self.dimensions[0]):
                    pos = [i,j,k]
                    serialList.append(self.coordArray[i][j][k])

        return serialList
        #<triple for loop to extract stream of data from array>

    def exportGrid(self,format="Array"):
        #function exportGrid will return the coordinate grid. Another format could be specified.
        #returns the numpy array if no format is specfied. Also returns a list containing dimensions
        if format=="Array":
            #return the numpy array
            return self.dimensions, self.coordArray

        elif format=="Stream":
            #return a serialized (one at a time) array of values. useful for serial communication
            return self.dimensions, self.serializeGrid()
