from Conway import Conway3d
from Conway import ConwayRules

class Routines():
    def __init__(self, cb):
        self.cube = cb

    def state_switch(self, frames, time_interval, cycles):
        for i in range(cycles):
            for frame in frames:
                self.coordinate_transfer(self.cube, frame)
                time.sleep(time_interval)

    def checkerboard(self, num_cycles, time_interval):
        """
        Description: Displays a checkerboard pattern on the cube.
        Algorithm based on the fact that adjacent LED's always have
        different states in checkerboard pattern.
        """
        prev_origin = self.cube.getOrigin()
        self.cube.setOrigin([0,0,0])
        first_led = True
        #set the or second LED on (based on the cycle #)
        self.cube.setPixel([0,0,0],"On")
        #
        for z in range(self.cube.dimensions[2]):
            for y in range(self.cube.dimensions[1]):
                for x in range(self.cube.dimensions[0]):
                    #count how many LEDs around the current LED are on or off
                    n_on, n_off = count_neighbors([x,y,z])
                    #The first run is taken care of. Skip it:
                    if first_led:
                        pass
                    #if no neighbors are on, toggle it
                    elif n_on == 0:
                        self.cube.setPixel([x, y, z],"On")
                    else:
                        self.cube.setPixel([x,y,z],"Off")
        time.sleep(time_interval)
        #we already did 1 cycle, so subtract 1 from the total:
        for i in range(num_cycles-1):
            #from here on out, just flip-flop all the LED's:
            self.cube.toggleAll()
            time.sleep(time_interval)

    def conwaygame(self, num_gen, time_interval, birth, overpop, underpop):
        """
        Description: conwaygame constructs a Conway's Game of life give
        a rule set and the number of generations to run the game.
        """

        #instantiate classes for the game itself
        game_rules = ConwayRules(birth, overpop, underpop)
        game = Conway3d(self.cube, game_rules)

        #set up a game
        game.random_start(20)
        self.cube.sendStream()
        time.sleep(time_interval)

        #advance the simulation for the specified number of generations
        for i in range(num_gen):
            self.game.generation()
            self.cube.sendStream()
            time.sleep(time_interval)
