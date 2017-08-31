from LEDCube import LEDCube
from Routines import Routines


cube = LEDCube([4,4,4])
r_list = Routines(cube)
r_list.rain(100)
#r_list.checkerboard(10,0.25)

#cube.pulseAll(0.01)
