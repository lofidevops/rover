import pytest
import rover


@pytest.mark.parametrize(
    "sample,expected", [("TEST", "TEST"), ("TEST ", "TEST"), ("Test", "TEST")]
)
def test_line_to_string(sample, expected):

    assert rover.line_to_string(sample) == expected


def test_true_for_even_value():

    assert rover.assert_even(2)


def test_exception_for_odd_value():

    with pytest.raises(ValueError):
        rover.assert_even(1)


@pytest.mark.parametrize(
    "line,output_x,output_y", [("1 1", 1, 1), ("1 10", 1, 10), ("10 1", 10, 1)]
)
def test_parse_grid_definition(line, output_x, output_y):

    assert output_x, output_y == rover.parse_grid_definition(line)


@pytest.mark.parametrize(
    "line",
    [
        "12",  # single value
        "1 2 3",  # too many values
        "1  3 4",  # too many spaces
        "a 2",  # bad x value
        "1 b",  # bad y value
    ],
)
def test_parse_grid_with_incorrect_values(line):

    with pytest.raises(ValueError):
        rover.parse_grid_definition(line)


@pytest.mark.parametrize(
    "line,grid_x,grid_y,output_x,output_y,output_orientation",
    [
        ("1 2 N", 3, 3, 1, 2, "N"),
        ("1 2 S", 3, 3, 1, 2, "S"),
        ("1 2 E", 3, 3, 1, 2, "E"),
        ("1 2 W", 3, 3, 1, 2, "W"),
    ],
)
def test_parse_rover_start(
    line, grid_x, grid_y, output_x, output_y, output_orientation
):

    x, y, o = rover.parse_rover_start(line, grid_x, grid_y)
    assert x == output_x
    assert y == output_y
    assert o == output_orientation


@pytest.mark.parametrize(
    "line,grid_x,grid_y",
    [
        ("3 2 N", 2, 2),  # y out of bounds
        ("1 3 N", 2, 2),  # x out of bounds
        ("a 1 N", 2, 2),  # bad x value
        ("1 b N", 2, 2),  # bad y value
        ("1 1 X", 2, 2),  # bad orientation value
    ],
)
def test_parse_rover_value_errors(line, grid_x, grid_y):

    with pytest.raises(ValueError):
        rover.parse_rover_start(line, grid_x, grid_y)


@pytest.mark.parametrize("line,output_list", [("", []), ("LRML", ["L", "R", "M", "L"])])
def test_parse_rover_command(line, output_list):

    assert rover.parse_rover_command(line) == output_list


@pytest.mark.parametrize("line", ["X", "XLL", "MXM", "RRX"])
def test_parse_rover_command_value_errors(line):

    with pytest.raises(ValueError):
        rover.parse_rover_command(line)
