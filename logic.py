class Simulation:
    def __init__(self, grid_x, grid_y):

        self.max_x = grid_x
        self.max_y = grid_y
        self.start_x = None
        self.start_y = None
        self.start_o = None

    def set_rover_start(self, start_x, start_y, start_orientation):

        self.start_x = start_x
        self.start_y = start_y
        self.start_o = start_orientation

    def simulate(self, rover_command):

        print(
            self.max_x,
            self.max_y,
            self.start_x,
            self.start_y,
            self.start_o,
            rover_command,
        )
