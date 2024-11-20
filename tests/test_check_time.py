import datetime
import pytest
from pytest import mark
import src

@mark.parametrize(
    'input, output',
    [
        (datetime.time(minute=30, hour=4, second=00),
         datetime.time(minute=30, hour=4, second=00)),
    ]
)
def test_check_time(input, output):
    assert(src.check_time(input) == output)

@mark.parametrize(
'input, output',
    [
        ('joãozinho', int(1)),
        (10, int(1)),
        ('10/10/1990', int(1)),
        ('15:59:25', int(1)),

    ]
)
def test_check_time_error(input, output):
    with pytest.raises(TypeError) as excinfo:
        src.check_time(input)
    assert (
            str(excinfo.value) == 'The input should be type datetime.time'
    )