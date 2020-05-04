#!/usr/bin/env python3

import click
from logic import Simulation
import re


def line_to_string(line):
    """Convert line from a file into a usable Python string."""

    return line.strip().upper()


def assert_even(value):
    """Return True if the value is even, otherwise raise an Exception."""

    even = value % 2 == 0

    if not even:
        raise ValueError("Bad number of lines.")

    return True


def parse_grid_definition(line):
    """Parse string `GX GY` and return grid limits."""

    string_list = line.split(" ")

    if len(string_list) != 2:
        raise ValueError("Bad grid definition.")

    grid = [int(value) for value in string_list]

    return grid[0], grid[1]


def parse_rover_start(line, grid_x, grid_y):
    """Parse string `RX RY RO` and return start position and orientation of rover."""

    string_list = line.split(" ")

    start_x = int(string_list[0])
    if start_x > grid_x:
        raise ValueError("Rover out of bounds.")

    start_y = int(string_list[1])
    if start_y > grid_y:
        raise ValueError("Rover out of bounds.")

    start_orientation = string_list[2]
    if start_orientation not in ["N", "S", "E", "W"]:
        raise ValueError("Invalid start orientation.")

    return start_x, start_y, start_orientation


def parse_rover_command(line):
    """Parse string `III...` and return list of rover commands."""

    pattern = re.compile("[LRM]*")  # any sequence of L, R and M
    other = re.sub(pattern, "", line)
    if len(other) > 0:
        raise ValueError("Bad rover command.")

    return list(line)


@click.command()
@click.argument("filename", type=click.File("r"))
@click.argument("output", type=click.File("w"))
@click.option(
    "--verbose",
    is_flag=True,
    help="Show the rover state at every step of the simulation.",
)
def cli(filename, output, verbose):
    """Run a rover simulation. Parse input and generate output in specified location."""

    try:
        # initialise input and output variables
        content = [line_to_string(line) for line in filename]
        results = []

        # initialise simulation with grid limits
        grid_x, grid_y = parse_grid_definition(content.pop(0))
        sim = Simulation(grid_x, grid_y)
        sim.verbose = verbose

        # validate remaining content
        assert_even(len(content))
        rover_count = len(content) // 2

        for roverid in range(rover_count):

            # initialise values for current rover
            start_x, start_y, start_orientation = parse_rover_start(
                content.pop(0), grid_x, grid_y
            )
            sim.set_rover_start(start_x, start_y, start_orientation)

            # execute instructions for current rover
            rover_command = parse_rover_command(content.pop(0))
            sim.simulate(rover_command)

            # store results
            results.append("%s %s %s" % (sim.curr_x, sim.curr_y, sim.curr_o))

        # write results for all rovers
        output_string = "\n".join(results) + "\n"
        output.write(output_string)

    except Exception as e:
        print("There was a problem reading the rover file. %s" % e)
