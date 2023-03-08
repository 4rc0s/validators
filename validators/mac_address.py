"""MAC Address."""
# -*- coding: utf-8 -*-

# standard
import re

# local
from .utils import validator


@validator
def mac_address(value: str):
    """Return whether or not given value is a valid MAC address.

    This validator is based on [WTForms MacAddress validator][1].

    [1]: https://github.com/wtforms/wtforms/blob/master/src/wtforms/validators.py#L482

    Examples:
        >>> mac_address('01:23:45:67:ab:CD')
        # Output: True
        >>> mac_address('00:00:00:00:00')
        # Output: ValidationFailure(func=mac_address, args={'value': '00:00:00:00:00'})

    Args:
        value:
            A string to validate.

    Returns:
        (Literal[True]):
            If `value` is a valid MAC address.
        (ValidationFailure):
            If `value` is an invalid MAC address.

    > *New in version 0.2.0*.
    """
    return re.match(r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", value)
