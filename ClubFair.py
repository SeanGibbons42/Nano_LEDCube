from Routines import Routines
from LEDCube import LEDCube
import time

cube = LEDCube([4,4,4])
r_list = Routines(cube)
r_list.snake(4,10000,0.01)

cube.setPixel([0,0,0],1)
cube.sendStream()
"""
while True:
    r_list.checkerboard(50,0.2)
    cube.pulseAll(0.03)
    r_list.rain(100)
    cube.pulseAll(0.3)
    for i in range(3):
        cube.pulseRows()
    for i in range(4):
        cube.pulseLayers()

    for i in range(20):
        cube.toggleAll()
        time.sleep(0.25)
    cube.clearAll()
"""
