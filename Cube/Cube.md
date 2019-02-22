# CoordinateSystem
```python
 class CoordinateSystem():
```

CoordinateSystem represents a 3d grid of discrete points. Each point in the grid contains a value, 1 or 0, representing the current state of a single LED in the LED cube. This class allows the state of the cube to be stored on the more powerful computer and reduce the processing load on the arduino.

```python
def __init__(orgn, dims):
```
##### Parameters:
* **orgn:** This class allows for coordinates to be relative to anywhere on the cube. The origin parameter (orgn) sets the absolute location of the point considered 0, 0, 0. A non-zero origin could be useful for a graphing calculator, where coordinates with negative components may need to be displayed.
* **dims:** List specifying the dimensions of the cube. Format [x, y, z]
___
&#10;

```python
def setOrigin(orgn):
```
##### Parameters:
* **orgn:** List containing the new point (in absolute coordinates) to be (0,0,0) in relative coordinates.
##### Returns:
* None
##### Description:
- To use an absolute coordinate system, just set the origin to (0,0,0).
___
&#10;

```python
def setDimensions(dims):
```
##### Parameters:
* **dims:** List containing the dimensions of the LED cube, in # of LED's. Format is [x, y, z]
##### Returns:
* None
##### Description:
- Sets the dimesions of the LED cube. When called, a new array will be generated, deleting the previously stored state.
___
&#10;

```python
def isInBounds(position):
```
##### Parameters:
* **postion:** List or Tuple describing a point. Format is [x, y, z] or (x, y, z)
##### Returns:
* **inbounds:** True if the point is contained within the cube, False if it it not.
##### Description:
- Checks to see whether a point is located within the cube's bounds.
___
&#10;

```python
def togglePixel(position):
```
##### Parameters:
* **postion:** List or Tuple describing a point. Format is [x, y, z] or (x, y, z)
##### Returns:
* None
##### Description:
- Inverts the state of a specific LED.
___
&#10;

```python
def setPixel(position, state):
```
##### Parameters:
* **postion:** List or Tuple describing a point. Format is [x, y, z] or (x, y, z)
* **state:** State of the LED. Valid values for ON: "On", "on", 1, "True". Valid values for OFF: "Off", "off", 0, False.
##### Returns:
* None
##### Description:
- Sets the value of an LED specified by **position** to the value set by **state**. The value of **state** can assume multiple types, including String, Boolean or Integer. The method will convert these values to an integer value for storage in CoordinateSystem.
___
&#10;

```python
def toggleRow(position, state):
```
##### Parameters:
* **postion:** List or Tuple describing a vertical row. Format is [x, y] or (x, y)
##### Returns:
* None
##### Description:
- Similar to togglePixel(), but used for switching an entire *vertical* row of LED'.
___
&#10;

```python
def setRow(position, state):
```
##### Parameters:
* **postion:** List or Tuple describing a vertical row. Format is [x, y] or (x, y)
* **state:** New state of the LED's. Valid values for ON: "On", "on", 1, "True". Valid values for OFF: "Off", "off", 0, False.
##### Returns:
* None
##### Description:
- Sets the value of a vertical column of LED's specified by **position** to the value set by **state**.
___
&#10;

```python
def togglePlane(position, axis):
```
##### Parameters:
* **axis:** Integer specifing the axis the plane is defined on. 0 = x, 1 = y, 2 = z
* **postion:** Integer describing the position along the axis of the target plane, starting from 0.
##### Returns:
* None
##### Description:
- Inverts the state of a 2d plane of LED's.
___
&#10;

```python
def setPlane(position, axis, state):
```
##### Parameters:
* **axis:** Integer specifing the axis the plane is defined on. 0 = x, 1 = y, 2 = z
* **postion:** Integer describing the position along the axis of the target plane, starting from 0.
* **state:** New state of the LED's. Valid values for ON: "On", "on", 1, "True". Valid values for OFF: "Off", "off", 0, False.
##### Returns:
* None
##### Description:
- Sets the state of a 2d plane of LED's to a specified value.
___
&#10;

```python
def setAll():
```
##### Parameters:
* **state:** New state of the LED's. Valid values for ON: "On", "on", 1, "True". Valid values for OFF: "Off", "off", 0, False.
##### Returns:
* None
##### Description:
- Sets the state of all LED's in the cube.
___
&#10;

##### Parameters:
* **state:** New state of the LED's. Valid values for ON: "On", "on", 1, "True". Valid values for OFF: "Off", "off", 0, False.
##### Returns:
* None
##### Description:
- Sets the state of all LED's in the cube.
___
&#10;

# Arduino
``` python
class Arduino(br = 9600):
```
The Arduino class provides a simple interface to facilitate communication between the LEDCube class and the physical LED Cube. Controls data formatting and transmission using a USB port.

This class utilizes the PySerial library to handle USB communication.

```python
def __init__():
```
##### Parameters:
* **br = 9600:** Baud rate, which defines the data transmission speed in bits/second. Defaults to 9600, which is a common default data rate for Arduino. 115200 is the maximum safe value for the Arduino Uno. (Anything faster may result in corrupted data.)

___
&#10;

```python
def openPort(br):
```
##### Parameters
* **br** Baud Rate, in bits per second. Max value for the Arduino Uno is 115200

##### Returns
* None

___
&#10;

```python
def findPort(vendorid=9025, productid=1):
```

##### Parameters
* **vendorid:** the vendor id is a unique identifier that is assigned to the manufacturer of the UART (USB) chip on the Arduino.
* **productid** Together with the vendor id, the product id serves to identify the specific UART chip on the Arduino. Both these values are stored on the chip and can be checked using the PySerial library.
##### Returns
* **device:** String identifying the serial port the Arduino is connected to
##### Description
* findPort accepts a vendorid and productid and will scan through all devices connected to the computer to find one with matching ID's. Will return an PySerial device object if a matching device is found, and None if it is not.

___
&#10;

```python
def sendFrame():
```
##### Parameters
* **dataStream:** 1D Array or list containing led states as integers with values 0 (off) or 1 (on).
##### Returns
* None
##### Description
* Calls serializeFrame() to efficiently package the data before sending it byte-by-byte using sendByte()

___
&#10;

```python
def sendByte():
```
##### Parameters
* **data:** Integer between 0 and 255, representing a single byte of Data.
##### Returns
* None
##### Description
* Sends a single byte of data to the cube using the PySerial library. Encodes data as an ACSCII character before calling serial.write(data).

___
&#10;

```python
def serializeFrame():
```
##### Parameters
* **array:** 1D Array or list containing led states as integers with values 0 (off) or 1 (on).
##### Returns
* ** bytestream ** Array of bytes where each byte contains the state of 8 LED's in binary form.
##### Description
* Function to compress the LED cube state array by a factor of 8. Groups of 8 states (1 or 0) are converted into decimal integers between 0 and 255. (1 byte) Example: [1,0,0,1,0,1,1,0] -> 10010110 -> 150.

___
&#10;

# LED Cube
```python
 class LEDCube():
```
The LEDCube class provides an interface between your application and an LEDCube. Extends the CoordnateSystem class, and implements additional methods for communicating with an Arduino via a serial USB connection and hardware debugging

```python
def __init__(size, testmode = False):
```

##### Parameters:

* **size:** List of length 3 specifying the dimensions of the cube. Format [x, y, z]
* **testmode:** If set to true, the library will start in emulation mode. Does not connect to a physical cube.
    * testmode is implemented yet!!


```python
def sendStream():
```
##### Parameters:
* None
##### Returns:
* None
##### Description:
- When the SendStream method is called, the current state of the cube stored in the CoordinateSystem class is sent to the physical LED cube, or to the emulator if the software was booted in test mode.
___
&#10;

```python
def toggleAll():
```
##### Parameters:
* None
##### Returns:
* None
##### Description:
- ToggleAll will swap the state of all LED's on the cube simulatneously. Includes call to sendStream().

___
&#10;

```python
def clearAll():
```
##### Parameters:
* None
##### Returns:
* None
##### Description:

- clearAll will turn off all LED's in the cube. Includes call to sendStream()

___
&#10;

```python
def pulseAll(time_interval = 0.02):
```
##### Parameters:
* **time_interval:** time delay between frames, in seconds.
##### Returns:
* None
##### Description:

- Turns each led in the cube on and off again in sequence. Useful for hardware/emulator debugging.
___
&#10;

```python
def pulseRows(time_interval = 0.05):
```
##### Parameters:
* **time_interval:** time delay between frames, in seconds.
##### Returns:
* None
##### Description:

- Turns each vertical row in the cube on and off again in sequence.
___
&#10;

```python
def pulseLayers(time_interval = 0.1):
```
##### Parameters:
* **time_interval:** time delay between frames, in seconds.
##### Returns:
* None
##### Description:

- Turns each flat layer (2d set of LED's) in the cube on and off again in sequence.
___
&#10;
