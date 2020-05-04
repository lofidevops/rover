class Simulation:
    """Stores environment values, initial values and executes rover instructions."""

    def __init__(self, grid_x, grid_y):
        """Set the maximum coordinates of the quadrant. The intended start position and current rover position are
        undefined."""

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
        """Set the intended start position of the rover. The current rover position is undefined."""

        self.start_x = start_x
        self.start_y = start_y
        self.start_o = start_orientation
        self.curr_x = None
        self.curr_y = None
        self.curr_o = None

    def _set_rover_current_to_start(self):
        """Move the current rover to its start position."""

        self.curr_x = self.start_x
        self.curr_y = self.start_y
        self.curr_o = self.start_o

    def rotate(self, direction):
        """Rotate 90 degrees in given direction."""

        leftward = {"N": "W", "S": "E", "E": "N", "W": "S"}
        rightward = {"N": "E", "S": "W", "E": "S", "W": "N"}
        rotate = {"left": leftward, "right": rightward}

        self.curr_o = rotate[direction][self.curr_o]

    def move(self):
        """Increment one step in current orientation, unless that moves out of bounds."""

        if self.curr_o == "N":
            self.curr_y = min(self.curr_y + 1, self.max_y)
        elif self.curr_o == "S":
            self.curr_y = max(self.curr_y - 1, 0)
        elif self.curr_o == "E":
            self.curr_x = min(self.curr_x + 1, self.max_x)
        elif self.curr_o == "W":
            self.curr_x = max(self.curr_x - 1, 0)

    def print_state(self, instruction):
        """Print the state of the current rover, with the instruction that achieved it."""

        print("%s: %s %s %s" % (instruction, self.curr_x, self.curr_y, self.curr_o))

    def simulate(self, rover_command):
        """Follow the given commands to simulate rover movement."""

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
