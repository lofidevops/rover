class Simulation:
    def __init__(self, grid_x, grid_y):

        self.max_x = grid_x
        self.max_y = grid_y
        self.start_x = None
        self.start_y = None
        self.start_o = None
        self.curr_x = None
        self.curr_y = None
        self.curr_o = None
        self.verbose = False

    def set_rover_start(self, start_x, start_y, start_orientation):

        self.start_x = start_x
        self.start_y = start_y
        self.start_o = start_orientation
        self.curr_x = None
        self.curr_y = None
        self.curr_o = None

    def _set_rover_current_to_start(self):

        self.curr_x = self.start_x
        self.curr_y = self.start_y
        self.curr_o = self.start_o

    def rotate(self, direction):

        leftward = {"N": "W", "S": "E", "E": "N", "W": "S"}
        rightward = {"N": "E", "S": "W", "E": "S", "W": "N"}
        rotate = {"left": leftward, "right": rightward}

        self.curr_o = rotate[direction][self.curr_o]

    def move(self):

        pass

    def print_state(self, instruction):

        print("%s: %s %s %s" % (instruction, self.curr_x, self.curr_y, self.curr_o))

    def simulate(self, rover_command):

        self._set_rover_current_to_start()

        if self.verbose:
            self.print_state("-")

        for instruction in rover_command:
            if instruction == "L":
                self.rotate("left")
            elif instruction == "R":
                self.rotate("right")
            elif instruction == "M":
                self.move()
            else:
                raise ValueError("Unknown rover command.")

            if self.verbose:
                self.print_state(instruction)
