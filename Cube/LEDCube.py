from Cube.CoordinateSystem import CoordinateSystem
from Cube.Arduino import Arduino
import time
class LEDCube(CoordinateSystem):
    """
    Class LEDCube:
    Description:
        -Controller class for the CoordinateSystem and Arduino models.
        Instantiate this class to initialize a connection to a cube
        and begin communicating.
    Extends:
        -CoordinateSystem
    Instance Attributes:
        -self.arduino > Instance of the arduino class
    Class Methods:
        -self.sendStream
        -self.pulseAll
        -self.pulseRows
        -self.pulseLayers
        -self.clearAll
        -self.toggleAll
        -self.equationFrame > TODO - Not implemented yet
    Intended Use Case:
        -Application imports and creates an instance of LEDCube, passing in the
        cube's dimensions.
        -Application utilizes the methods present in both CoordinateSystem and
        LEDCube to create a static display.
        -Application sends the model's current state to the Arduino by calling
        LEDCube.sendStream
        -Application assembles the next frame
        -Application sends the new frame using sendStream
        -And so on ...
    """
    def __init__(self,size):
        #constructor: initialize system component classes and set the initial size
        #the origin will initialize to 0,0,0. The ardi

        super().__init__([0, 0, 0], size)
        self.arduino = Arduino(9600) #add ard

    def sendStream(self):
        #Function sendStream: Sends a bytestream to a target device
        #Takes into account
        stream = self.exportGrid("Stream")
        frame = self.arduino.sendFrame(stream)

    def pulseAll(self, time_interval=0.02):
        #Function pulseAll: iterates through all LED's and turns them on then off
        for x in range(self.bounds[5],self.bounds[4]+1):
            for y in range(self.bounds[3],self.bounds[2]+1):
                for z in range(self.bounds[1],self.bounds[0]+1):
                    self.setPixel([x,y,z],1);
                    self.sendStream()
                    time.sleep(time_interval)
                    self.setPixel([x,y,z],0)
                    self.sendStream()
                    time.sleep(time_interval)
                    #print(str(x)+", "+str(y)+", "+str(z))
    def pulseRows(self):
        #Function pulseRows: goes through and turns on each vertical row one at a time
        for x in range(self.bounds[5],self.bounds[4]+1):
            for y in range(self.bounds[3],self.bounds[2]+1):
                self.setRow([x,y],1)
                self.sendStream()
                time.sleep(0.05)
                self.setRow([x,y],0)
                self.sendStream()
                time.sleep(0.05)
    def pulseLayers(self):
        #Function pulseLayer: goes through and turns on each layer
        for z in range(self.bounds[5],self.bounds[4]+1):
            self.setPlane(z,2,1)
            self.sendStream()
            time.sleep(0.1)
            self.setPlane(z,2,0)
            self.sendStream()
            time.sleep(0.1)
    def equationFrame(self,equation):
        #displays a parsed expression on the cube
        #NOT IMPLEMENTED IN 1.0! -- We need an equation parser for this to work!!
        return

    def clearAll(self):
        #Function clearAll: turns off every LED in the cube
        for x in range(self.bounds[5],self.bounds[4]+1):
            for y in range(self.bounds[3],self.bounds[2]+1):
                for z in range(self.bounds[1],self.bounds[0]+1):
                    self.setPixel([x,y,z],0);
        self.sendStream()

    def toggleAll(self):
        #Function toggleAll: switches the value of each LED in the array
        for x in range(self.bounds[5],self.bounds[4]+1):
            for y in range(self.bounds[3],self.bounds[2]+1):
                for z in range(self.bounds[1],self.bounds[0]+1):
                    self.togglePixel([x,y,z]);

        self.sendStream()
