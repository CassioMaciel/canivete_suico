# pylint: disable=C0114
from typing import Any


def check_float(value: Any) -> float:
    """
    Checks if the input value is numeric and returns it as a float.

    Parameters:
    - value: Numeric value to be checked and converted to float.

    Returns:
    - float: Converted numeric value.

    Raises:
    - TypeError: If the input is not numeric (neither int nor float).
    """
    if isinstance(value, float):
        return value
    if isinstance(value, int):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
        except (ValueError, TypeError):
            pass
    raise TypeError(
        'The input should be of numeric type, either int or float.'
    )


def check_int(value: Any) -> int:
    """
    This function check if the input variable is int, and if not, try to
    convert the string or float to integer.
    :param value: Numeric value to be converted to int
    :return: integer value
    """
    a: int = 0
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except (ValueError, TypeError):
            pass
    if isinstance(value, float):
        a = int(value)
        if (a - value) == 0:
            return a

    raise TypeError(
            'The input should be integer'
        )
