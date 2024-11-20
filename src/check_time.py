# pylint: disable=C0114
import datetime
from typing import Any


def check_time(value: Any) -> datetime.time:
    """
    Checks if the input value is of type datetime.time.

    Parameters:
    - value: Value to be checked for its type.

    Returns:
    - datetime.time: If the input is of type datetime.time.

    Raises:
    - TypeError: If the input is not of type datetime.time.
    """
    if isinstance(value, datetime.time):
        return value
    raise TypeError('The input should be type datetime.time')
