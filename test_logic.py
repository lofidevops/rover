from logic import Simulation


def test_simulation_init():

    s = Simulation(1, 2)

    assert s.max_x == 1
    assert s.max_y == 2
    assert s.start_x is None
    assert s.start_y is None
    assert s.start_o is None


def test_set_rover_start():

    s = Simulation(1, 2)
    s.set_rover_start(3, 4, "N")

    assert s.max_x == 1
    assert s.max_y == 2
    assert s.start_x == 3
    assert s.start_y == 4
    assert s.start_o == "N"
