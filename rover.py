#!/usr/bin/env python3

import click
import logic
import re


def line_to_string(line):
    """Convert line from a file into a usable Python string."""
    return line.strip().decode("utf-8").upper()


def assert_even(value):
    """Return True if the value is even, otherwise raise an Exception."""

    even = value % 2 == 0

    if not even:
        raise Exception("Invalid contents.")

    return True


def parse_grid_definition(line):

    string_list = line.split(" ")
    grid_limits = [int(value) for value in string_list]
    return tuple(grid_limits)


def parse_rover_start(line, grid_x, grid_y):

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

    pattern = re.compile("[LRM]*")  # any sequence of L, R and M
    if not pattern.match(line):
        raise ValueError("Bad rover command.")

    return list(line)


def simulate(grid_x, grid_y, start_x, start_y, start_orientation, rover_command):

    print(grid_x, grid_y, start_x, start_y, start_orientation, rover_command)


@click.command()
@click.argument("filename", type=click.File("rb"))
@click.argument("output", type=click.File("wb"))
def cli(filename, output):
    """Parse CLI input."""

    try:
        content = [line_to_string(line) for line in filename]

        grid_x, grid_y = parse_grid_definition(content.pop(0))

        assert_even(len(content))
        rover_count = len(content) // 2

        for roverid in range(rover_count):
            start_x, start_y, start_orientation = parse_rover_start(
                content.pop(0), grid_x, grid_y
            )
            rover_command = parse_rover_command(content.pop(0))
            simulate(grid_x, grid_y, start_x, start_y, start_orientation, rover_command)

    except Exception as e:
        print("There was a problem reading the rover file. %s" % e)
