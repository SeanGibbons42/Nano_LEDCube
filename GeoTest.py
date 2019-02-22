from Cube.geometry.GFactory import GFactory
from Cube.LEDCube import LEDCube
import time

#instantiate cube and geometry classes
mycube = LEDCube([4,4,4])
myfactory = GFactory()

#create a sphere
mysphere = myfactory.create_shape("Sphere", "mysphere", 1, [1, 1, 1])
mysphere.draw(mycube)
time.sleep(1)

#move the sphere around a bit
mysphere.translate([2,2,2])
mysphere.draw(mycube)
time.sleep(1)
mysphere.translate([3,3,3])
mysphere.draw(mycube)
time.sleep(10)
"""
mycube.setPixel([1,1,1], "Off")
mycube.sendStream()
time.sleep(1)
"""
