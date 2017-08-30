class Conway3d():
    def __init__(self, cs, rules):
        self.grid = cs


    def random_start(self, num_living):
        """
            function random_start creates a random starting
            config.
        """
        #clear off the grid
        self.grid.clearAll()

        start_points = []
        #get the grid dimensions
        x_size,y_size,z_size = [self.grid.dimensions]
        for i in range(num_living):
            next_point = []
            while True:
                next_point = [random.randint(0,x_size),random.randint(0,y_size),random.randint(0,z_size)]
                if not next_point in start_points:
                    start_points.append(next_point)
                    break
                else:
                    pass
        for point in start_points:
            self.grid.setPixel(point,"On")

    def generation(self):
        """
        Description:
            method generation simulates a single CGoL generation.
            Examines each pixel and uses the live_or_die function
            to determine whether each pixel is turned on or off.
        """
        for z in range(self.grid.dimensions[2]):
            for y in range(self.grid.dimensions[1]):
                for x in range(self.grid.dimensions[0]):
                    self.grid.setPixel([x,y,z],live_or_die([x,y,z]))


    def live_or_die(self, pos):
        """
        Description:
            method live_or_die will determine whether
            a pixel deserves to live, based on the game rules
        CGoL 3d Rules:
            A pixel is Born if and only if it has 4 neighbors
            A pixel dies if it has 3 or less neighbors
            A pixel dies if it has 5 or more neighbors
            A pixel Lives if it has exactly 4 neighbors
        In other words:
            LED = on, if and only if neighbors = 4
            LED = off, if neighbors > 4 or neighbors < 4
        """
        on, off = self.grid.count_neighbors(pos)
        return rules.check_live(on)

class ConwayRules():
    def __init__(pass, birth, overpop, underpop):
        if type(birth) is int:
            self.birth_conditions = [birth]
        else:
            self.birth_conditions = birth

        self.overpop_threshold = overpop
        self.underpop_threshold = underpop

    def check_live(self, state,num_nei):
        if num_neighbors in birth_conditions:
            return True
        elif state == 1 and num_nei > self.underpop_threshold and num_nei < self.overpop_threshold:
            return True
        else:
            return False

    def get_birth(self):
        return self.birth_conditions

    def get_overpop(self):
        return self.overpop_threshold

    def get_underpop(self):
        return self.underpop_threshold
