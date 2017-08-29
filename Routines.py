class Routines():
    def __init__(self, cb):
        self.cube = cb

    def state_switch(self, frames, time_interval, cycles):
        for i in range(cycles):
            for frame in frames:
                self.coordinate_transfer(self.cube, frame)
                time.sleep(time_interval)

    def checkerboard(self, num_cycles, time_interval):
        first_led = True
        prev_origin = self.cube.getOrigin()
        self.cube.setOrigin([0,0,0])
        led_num = 1
        for i in range(num_cycles):
            #set the or second LED on (based on the cycle #)
            if first_led:
                self.cube.setPixel([0,0,0],"On")
            else:
                self.cube.setPixel([1,0,0],"On")
            first_led = not first_led
            #Iterate through the entire cube. If a given LED does not have
            #a neighboring LED that is on, turn it on
            for z in range(self.cube.dimensions[2]):
                for y in range(self.cube.dimensions[1]):
                    for x in range(self.cube.dimensions[0]):
                        #count how many LEDs around the current LED are on or off
                        n_on, n_off = count_neighbors([x,y,z])
                        #The first two LED's are taken care of.
                        #ignore them.
                        if led_num == 1 or led_num == 2:
                            pass
                        elif n_on == 0:
                            self.cube.setPixel([x, y, z],"On")
                        else:
                            self.cube.setPixel([x,y,z],"Off")
                        led_num += 1
            time.sleep(time_interval)
