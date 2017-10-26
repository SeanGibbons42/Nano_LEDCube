import serial
import time
class Arduino(object):
    def __init__(self,br=9600):
        #constructor: initializes an arduino object with a specific baud rate.
        #the baud rate (br) must equal the baud rate set in the arduino code.
        #9600 is a very standard value, but we can go higher if we need to.
        self.baud = br

        #open the serial port
        self.ardPort = self.openPort(self.baud)

        time.sleep(3)

    def openPort(self,br):
        #Function openPort: opens a USB serial port with a given name.
        #TODO: Make the program search for arduinos, also add exception for port not found.

        #initialize a serial port object and return it
        return serial.Serial("COM3",br)

    def sendFrame(self,dataStream):
        #function SendFrame: sends a stream of data a byte array.
        #In the cube project, we will pass the serialized cube frame to this function

        #convert the raw bytestream into a series of bytes.
        byteStream = self.serializeFrame(dataStream[1])
        #iterate through the bytestream, sending each byte
        for byte in byteStream:
            self.sendByte(byte)

    def sendByte(self,data):
        #encodes the data as an ascii binary char (data format for pyserial)
        # and then writes a byte to the board
        dataChar = chr(data).encode('utf-8')
        dataByte = data.to_bytes(1,'big',signed=False)

        self.ardPort.write(dataByte)

    def getByte(self):
        #Reads a byte from the serial port.

        #data arrives in a binary (fairly unusable) format!
        #we need to decode it to a char and then in this case, convert it to an integer

        numBytes = 0

        while(numBytes==0):
            numBytes = self.ardPort.inWaiting()
        time.sleep(0.1)
        numBytes = self.ardPort.inWaiting()

        b = self.ardPort.read(numBytes)

        self.ardPort.flush()
        return ord(b.decode('utf-8'))
        #return 'hi'
    def goodbye(self):
        #sharing is caring. Close the port so others can use it!
        self.ardPort.close()

    def serializeFrame(self,array):
        #takes a 3d coordinate array and converts it to a sendable bytestream
        pos = 0
        #the bytestream is a series of values that are sendable using pyserial.
        #each byte can represent a series of 8 LED's
        bytestream = []
        #We will iterate through the array in 8 bit increments.
        for i in range(0,int(len(array)/8)):
            #store the current byte as a string. It has to be created as a list first
            #since lists are mutable but strings are not.
            currentByte = []
            currentByteStr = ''
            #iterate through the next byteframe (next 8 bits) and construct a byte
            for j in range(0,8):
                currentByte.append(str(int(array[pos])))
                pos += 1
            #join will convert an array of strings into one big happy string.
            currentByteStr = currentByteStr.join(currentByte)
            #the string is binary and consists of 1's and 0's. We can convert this to
            #a normal python integer by typecasting the binary string as integers.
            #the second arguement, 2, specifies the base of the target string (binary = base 2)
            #example: let str = '101'
            #         typecast str: newInt = int(str,2)
            #         now, str is converted to a decimal int: newInt = 10
            bytestream.append(int(currentByteStr,2))

        return bytestream
