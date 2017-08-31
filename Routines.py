from Conway import Conway3d
from Conway import ConwayRules
import time
import random
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
        print("Starting Checkerboard")
        for z in range(self.cube.dimensions[2]):
            for y in range(self.cube.dimensions[1]):
                for x in range(self.cube.dimensions[0]):
                    #count how many LEDs around the current LED are on or off
                    n_on, n_off = self.cube.count_neighbors([x,y,z])
                    #The first run is taken care of. Skip it:
                    if first_led:
                        first_led = False
                    #if no neighbors are on, toggle it
                    elif n_on == 0:
                        self.cube.setPixel([x, y, z],"On")
                    else:
                        self.cube.setPixel([x,y,z],"Off")
        print("Setup Complete")
        self.cube.sendStream()
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

    def rain(self,numdrops):
            currentdrops = []  # Array that holds all current drops
            maxdim = self.cube.dimensions[0]-1
            for i in range(numdrops):
                currentdrops.append(raindrop(maxdim, random.randint(0, maxdim), random.randint(0, maxdim)))  # Create a new drop
                # update the cube
                self.cube.clearAll()
                for drop in currentdrops:
                    x,y,z = drop.givecoords()
                    print(x,y,z)
                    if (x >= 0):
                        self.cube.setPixel([x,y,z], "On")
                    else:
                        currentdrops.remove(drop)
                    drop.drop()  # drop the drops
                    # remove any drop that is out of the cube

                self.cube.sendStream()  # Push to arduino
                time.sleep(0.4)

    def snake(self):
        segments = []
        head = snakesegment()
        segments.append(head)
        for i in range(3):
            segment = snakesegment(segments[i],[0,0,i])

        



class raindrop:
    xpos = 0
    ypos = 0
    zpos = 0

    def __init__(self, x, y, z):
        self.xpos = x
        self.ypos = y
        self.zpos = z

    def drop(self):
        self.xpos -= 1

    def givecoords(self):
        return self.xpos, self.ypos, self.zpos

    def checkalive(self):
        if self.xpos == -4:
            return True
        return False

class snakesegment:
    prevlink = None

    def __init__(self,prev,pos):

        prevlink = prev
        xpos = pos[0]
        ypos = pos[1]
        zpos = pos[2]

    def givepos():
        return xpos,ypos,zpos

    def advance():
        pos = prevlink.givepos()
        xpos = pos[0]
        ypos = pos[1]
        zpos = pos[2]
