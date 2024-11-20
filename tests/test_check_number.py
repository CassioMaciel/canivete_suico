import datetime
import pytest
from pytest import mark
import src


@mark.parametrize(
    'input, output',
    [
        (1, int(1)),
        ('1', int(1)),
        (1.0, int(1)),
        (2.0, int(2)),
        (3.00, int(3)),
    ]
)
def test_check_int_1(input, output):
    assert(src.check_int(input) == output)


@mark.parametrize(
'input, output',
    [
        (datetime.time(minute=5, second=10), int(1)),
        ('3.5', int(1)),
        (3.5, int(1)),
        ('joazinho', int(1)),
    ]
)
def test_check_int_error(input, output):
    with pytest.raises(TypeError) as excinfo:
        src.check_int(input)
    assert (
            str(excinfo.value) == 'The input should be integer'
    )

@mark.parametrize(
    'input,output',
    [
        (int(1), float(1)),
        ('3.5', float(3.5)),
        (3.5, float(3.5)),
    ]
)
def test_check_float_1(input, output):
    assert(src.check_float(input) == output)

@mark.parametrize(
'input',
    [
        ('joãozinho'),
        (datetime.time(minute=5, second=10)),

    ]
)
def test_check_float_error(input):
    with pytest.raises(TypeError) as excinfo:
        src.check_float(input)
    assert (
            str(excinfo.value) == 'The input should be of numeric type,'
                                  ' either int or float.'
    )

@mark.parametrize(
'input',
    [
        (2.5),
        (3.2),
        ('joãozinho'),
    ]
)
def test_check_int_error(input):
    with pytest.raises(TypeError) as excinfo:
        src.check_int(input)
    assert (
            str(excinfo.value) == "The input should be integer"
    )
