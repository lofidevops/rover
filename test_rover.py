import pytest
import rover


@pytest.mark.parametrize(
    "bytestring,plainstring", [(b"TEST", "TEST"), (b"Test", "TEST")]
)
def test_line_to_string(bytestring, plainstring):

    assert rover.line_to_string(bytestring) == plainstring
