class Routines():
    def __init__(self, cb):
        self.cube = cb

    def state_switch(self, frames, time_interval, cycles):
        for i in range(cycles):
            for frame in frames:
                self.coordinate_transfer(self.cube, frame)
                time.sleep(time_interval)

    def checkerboard(self, led_frequency, num_cycles, time_interval=2):
        #it is simplest to assume the origin is located at
        #0,0,0. So we store the current origin and then set it
        #to 0,0,0
        first_origin = self.cube.getOrigin()
        self.cube.setOrigin([0, 0, 0])
        self.cube.clearAll
        #State of the first LED in the frame. Will toggle
        #each time thr frame changes to allow two different states
        first_led = True

        for i in range(num_cycles):
            is_on = first_led
            #iteration must happen in a serpentine pattern to yield
            #the pattern we want. Otherwise, each row and layer will
            #be identical
            for i in range(0,self.cube.dimensions[2],2):
                for j in range(0,self.cube.dimensions[1],2):
                    for k in range(self.cube.dimensions[0]):
                        self.cube.setPixel([i,j,k],is_on)
                        is_on = not is_on
                    j = j + 1
                    #The serpentine pattern moves down one row,
                    #then starts the next one at the same side that
                    #the previous row ended on
                    for k in range(self.cube.dimensions[0],0,-1):
                        self.cube.setPixel([i,j,k],is_on)
                        is_on = not is_on
                #Same thing
                for j in range(self.cube.dimensions[1],0,-2):
                    for k in range(self.cube.dimensions[0]):
                        self.cube.setPixel([i,j,k],is_on)
                        is_on = not is_on
                    j = j + 1
                    for k in range(self.cube.dimensions[0],0,-1):
                        self.cube.setPixel([i,j,k],is_on)
                        is_on = not is_on
            self.cube.sendStream()
            time.sleep(time_interval)
            first_led = not first_led
