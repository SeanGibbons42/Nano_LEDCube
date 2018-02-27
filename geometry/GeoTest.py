import geometry.GObject as gobj
import Cube.LEDCube as cube

#instantiate cube and geometry classes
mycube = cube([4,4,4])
myfactory = gobj.GFactory()

mysphere = myfactory.create_shape("Sphere", 1, [1,1,1])
mysphere.draw(mycube)
time.sleep(1)
mysphere.translate([2,2,2])
mysphere.draw(mycube)
time.sleep(1)
mysphere.translate([3,3,3])
mysphere.draw(mycube)
time.sleep(10)
