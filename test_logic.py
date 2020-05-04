import pytest

from logic import Simulation


def test_simulation_init():

    s = Simulation(3, 4)

    assert s.max_x == 3
    assert s.max_y == 4
    assert s.start_x is None
    assert s.start_y is None
    assert s.start_o is None
    assert s.curr_x is None
    assert s.curr_y is None
    assert s.curr_o is None


def test_set_rover_start():

    s = Simulation(3, 4)
    s.set_rover_start(1, 2, "N")

    assert s.max_x == 3
    assert s.max_y == 4
    assert s.start_x == 1
    assert s.start_y == 2
    assert s.start_o == "N"
    assert s.curr_x is None
    assert s.curr_y is None
    assert s.curr_o is None


@pytest.mark.parametrize(
    "start_orientation,rotate_direction,new_orientation",
    [
        ("N", "left", "W"),
        ("N", "right", "E"),
        ("E", "left", "N"),
        ("E", "right", "S"),
        ("S", "left", "E"),
        ("S", "right", "W"),
        ("W", "left", "S"),
        ("W", "right", "N"),
    ],
)
def test_rotation(start_orientation, rotate_direction, new_orientation):

    s = Simulation(3, 4)
    s.set_rover_start(1, 2, start_orientation)
    s._set_rover_current_to_start()
    s.rotate(rotate_direction)
    assert s.curr_o == new_orientation


@pytest.mark.parametrize(
    "start_x,start_y,start_orientation,new_x,new_y",
    [
        (1, 1, "N", 1, 2),  # north from center
        (1, 1, "S", 1, 0),  # south from center
        (1, 1, "E", 2, 1),  # east from center
        (1, 1, "W", 0, 1),  # west from center
        (0, 0, "N", 0, 1),  # north from bottom-left
        (0, 0, "S", 0, 0),  # south from bottom-left (out of bounds)
        (0, 0, "E", 1, 0),  # east from bottom-left
        (0, 0, "W", 0, 0),  # west from bottom-left (out of bounds)
        (0, 2, "N", 0, 2),  # north from top-left (out of bounds)
        (0, 2, "S", 0, 1),  # south from top-left
        (0, 2, "E", 1, 2),  # east from top-left
        (0, 2, "W", 0, 2),  # west from top-left (out of bounds)
        (2, 2, "N", 2, 2),  # north from top-right (out of bounds)
        (2, 2, "S", 2, 1),  # south from top-right
        (2, 2, "E", 2, 2),  # east from top-right (out of bounds)
        (2, 2, "W", 1, 2),  # west from top-right
        (2, 0, "N", 2, 1),  # north from bottom-right
        (2, 0, "S", 2, 0),  # south from bottom-right (out of bounds)
        (2, 0, "E", 2, 0),  # east from bottom-right (out of bounds)
        (2, 0, "W", 1, 0),  # west from bottom-right
    ],
)
def test_move(start_x, start_y, start_orientation, new_x, new_y):

    s = Simulation(2, 2)
    s.set_rover_start(start_x, start_y, start_orientation)
    s._set_rover_current_to_start()
    s.move()
    assert s.curr_x == new_x
    assert s.curr_y == new_y


def test_start_at_obstacle_fails_silently():

    s = Simulation(2, 2)
    s.obstacles.add((1, 1))
    s.set_rover_start(1, 1, "N")
    s.simulate(["R"])

    assert s.curr_x == -1
    assert s.curr_y == -1
    assert s.curr_o == "O"


def test_final_position_is_obstacle():

    s = Simulation(2, 2)
    s.set_rover_start(1, 1, "N")
    s.simulate(["M"])

    assert (1, 2) in s.obstacles


def test_second_rover_at_final_position_fails_silently():

    s = Simulation(2, 2)
    s.set_rover_start(1, 1, "N")
    s.simulate(["M"])

    assert (1, 2) in s.obstacles

    s.set_rover_start(1, 2, "N")
    s.simulate(["R"])

    assert s.curr_x == -1
    assert s.curr_y == -1
    assert s.curr_o == "O"
