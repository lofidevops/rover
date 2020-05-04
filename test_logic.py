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
